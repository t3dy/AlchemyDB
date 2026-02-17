import csv
import sqlite3
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def export_spreadsheets(config):
    db = Database(config.db_path)
    export_dir = Path("exports/spreadsheets")
    export_dir.mkdir(parents=True, exist_ok=True)
    
    with db.get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 1. Export Alchemists (Entities)
        cursor.execute("SELECT name, entity_type, tradition, description, is_verified FROM entities")
        alchemists = cursor.fetchall()
        write_csv(export_dir / "alchemists.csv", alchemists)

        # 2. Export Documents with status notes
        cursor.execute("""
            SELECT 
                d.id, d.title, d.author, d.year, d.doc_type,
                (SELECT COUNT(*) FROM document_chunks WHERE document_id = d.id) as chunk_count
            FROM documents d
        """)
        documents = cursor.fetchall()
        
        doc_rows = []
        for doc in documents:
            row = dict(doc)
            notes = []
            if not row["author"] or row["author"].lower() == "none":
                notes.append("Author identification needed")
            if row["chunk_count"] == 0:
                notes.append("Text extraction needed")
            else:
                notes.append(f"Extracted ({row['chunk_count']} chunks)")
            
            # Simple heuristic for "summarized" - since we don't have a summary field yet
            notes.append("Summary pending LLM pass")
            
            row["identification_notes"] = "; ".join(notes)
            doc_rows.append(row)
        
        write_csv(export_dir / "documents.csv", doc_rows)

        # 3. Export Dictionary Entries (Lexicon)
        cursor.execute("SELECT term, definition, is_verified FROM lexicon")
        lexicon = cursor.fetchall()
        write_csv(export_dir / "lexicon.csv", lexicon)

    print(f"Spreadsheets exported to {export_dir}")

def write_csv(path, rows):
    if not rows:
        print(f"No data for {path.name}")
        return
    
    fieldnames = rows[0].keys()
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row))

if __name__ == "__main__":
    config = load_config()
    export_spreadsheets(config)
