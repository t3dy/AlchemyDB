import fitz  # PyMuPDF
import sqlite3
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def extract_and_chunk(config):
    db = Database(config.db_path)
    chunk_size = config.chunk_size
    chunk_overlap = config.chunk_overlap

    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Get all documents that need processing (for now, just all document_files)
        cursor.execute("""
            SELECT df.document_id, df.file_path 
            FROM document_files df
            LEFT JOIN document_chunks dc ON df.document_id = dc.document_id
            WHERE dc.id IS NULL
        """)
        docs_to_process = cursor.fetchall()
        
        if not docs_to_process:
            print("No new documents to process for extraction.")
            return

        for doc_id, file_path in docs_to_process:
            print(f"Extracting text from: {Path(file_path).name}")
            try:
                doc = fitz.open(file_path)
                full_text = []
                page_offsets = [] # Track which page starts at which character index
                
                current_char_count = 0
                for page_num, page in enumerate(doc):
                    text = page.get_text()
                    full_text.append(text)
                    page_offsets.append((current_char_count, page_num + 1))
                    current_char_count += len(text)
                
                combined_text = "".join(full_text)
                words = combined_text.split()
                
                # Simple word-based chunking
                chunks = []
                for i in range(0, len(words), chunk_size - chunk_overlap):
                    chunk_words = words[i:i + chunk_size]
                    if not chunk_words:
                        break
                    
                    chunk_text = " ".join(chunk_words)
                    
                    # Estimate page number based on first few words of the chunk
                    # This is an approximation
                    first_word_index = combined_text.find(chunk_words[0])
                    page_num = 1
                    for offset, p_num in page_offsets:
                        if first_word_index >= offset:
                            page_num = p_num
                        else:
                            break
                    
                    chunks.append({
                        "document_id": doc_id,
                        "chunk_index": len(chunks),
                        "content": chunk_text,
                        "page_number": page_num,
                        "token_count": len(chunk_words) # Using word count as token proxy
                    })
                
                # Insert chunks into database
                for chunk in chunks:
                    cursor.execute("""
                        INSERT INTO document_chunks (document_id, chunk_index, content, page_number, token_count)
                        VALUES (?, ?, ?, ?, ?)
                    """, (chunk["document_id"], chunk["chunk_index"], chunk["content"], chunk["page_number"], chunk["token_count"]))
                
                print(f"Stored {len(chunks)} chunks for document {doc_id}")
                conn.commit()
                
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    config = load_config()
    extract_and_chunk(config)
