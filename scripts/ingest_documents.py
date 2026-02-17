import os
import hashlib
import sqlite3
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
from scripts.config_loader import load_config
from scripts.db import Database

def get_sha256(file_path: Path) -> str:
    """Compute the SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Read in chunks to avoid memory issues with large files
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def ingest_documents(config_path: Optional[str] = None):
    config = load_config(config_path)
    db = Database(config.db_path)
    corpus_dir = Path(config.corpus_path)
    
    if not corpus_dir.exists():
        print(f"Error: Corpus directory {corpus_dir} does not exist.")
        return

    # Start a run record
    run_id = None
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO runs (config_snapshot, status) VALUES (?, ?)",
            (json.dumps(config.to_dict()), "running")
        )
        run_id = cursor.lastrowid
        conn.commit()

    print(f"Starting ingestion run {run_id}...")
    
    docs_added = 0
    docs_skipped = 0
    errors = 0
    
    # Iterate through PDF files
    for file_path in corpus_dir.rglob("*.pdf"):
        try:
            # We treat the file path relative to the corpus root for portability if needed, 
            # but usually absolute is safer in local-first. Let's use absolute for now.
            abs_path = str(file_path.absolute())
            file_stats = file_path.stat()
            size = file_stats.st_size
            mtime = datetime.fromtimestamp(file_stats.st_mtime).isoformat()
            
            # Compute hash for de-duplication
            file_hash = get_sha256(file_path)
            
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Check if hash already exists
                cursor.execute("SELECT document_id FROM document_files WHERE sha256 = ?", (file_hash,))
                result = cursor.fetchone()
                
                if result:
                    # Update path if it changed (optional, but good for tracking)
                    cursor.execute(
                        "UPDATE document_files SET file_path = ?, file_size = ?, mtime = ? WHERE sha256 = ?",
                        (abs_path, size, mtime, file_hash)
                    )
                    docs_skipped += 1
                else:
                    # Create new document
                    title = file_path.stem.replace("_", " ")
                    cursor.execute(
                        "INSERT INTO documents (title, doc_type) VALUES (?, ?)",
                        (title, "pdf")
                    )
                    doc_id = cursor.lastrowid
                    
                    # Create file entry
                    cursor.execute(
                        "INSERT INTO document_files (document_id, sha256, file_path, file_size, mtime) VALUES (?, ?, ?, ?, ?)",
                        (doc_id, file_hash, abs_path, size, mtime)
                    )
                    docs_added += 1
                
                conn.commit()
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            errors += 1

    # Finalize run record
    with db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE runs SET status = ?, message = ? WHERE id = ?",
            ("completed", f"Added: {docs_added}, Skipped: {docs_skipped}, Errors: {errors}", run_id)
        )
        conn.commit()

    print(f"Ingestion complete. Added: {docs_added}, Skipped: {docs_skipped}, Errors: {errors}")

if __name__ == "__main__":
    ingest_documents()
