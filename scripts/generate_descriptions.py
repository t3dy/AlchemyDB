import sqlite3
import re
from scripts.db import Database
from scripts.config_loader import load_config

def generate_descriptions():
    config = load_config()
    db = Database(config.db_path)
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Get all documents that don't have a description
        cursor.execute("SELECT id, title FROM documents WHERE description IS NULL OR description = ''")
        docs = cursor.fetchall()
        
        for doc_id, title in docs:
            # Get the first chunk of content
            cursor.execute("SELECT content FROM document_chunks WHERE document_id = ? AND chunk_index = 0", (doc_id,))
            row = cursor.fetchone()
            
            if row:
                content = row[0]
                # Skip common copyright/boilerplate chunks
                boilerplate_patterns = [
                    r"CD-Rom are for use only",
                    r"Adam McLean",
                    r"private study and must not",
                    r"without permission from the copyright holder"
                ]
                
                # If chunk 0 is boilerplate, try chunk 1
                is_boilerplate = any(re.search(p, content, re.I) for p in boilerplate_patterns)
                if is_boilerplate:
                    cursor.execute("SELECT content FROM document_chunks WHERE document_id = ? AND chunk_index = 1", (doc_id,))
                    next_row = cursor.fetchone()
                    if next_row:
                        content = next_row[0]

                # Clean up content
                content = re.sub(r'\s+', ' ', content).strip()
                
                # Focus on a substantive sentence (e.g., starting with 'This', 'The', or common alchemical terms)
                # For now, just take a cleaner slice
                description = content[:200] + "..." if len(content) > 200 else content
            else:
                description = f"Alchemical text or scholarly analysis regarding {title}."
            
            # Update the document
            cursor.execute("UPDATE documents SET description = ? WHERE id = ?", (description, doc_id))
            print(f"Generated description for: {title}")
            
        conn.commit()

if __name__ == "__main__":
    generate_descriptions()
