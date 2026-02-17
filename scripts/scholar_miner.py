import sqlite3
import json
import re
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

# Markers that suggest a context is discussing the scholar's ideas, not just citing them
HISTORIOGRAPHY_MARKERS = [
    "argue", "thesis", "demonstrate", "shown by", "according to", "interpretation", 
    "analysis", "biography", "historian", "scholar", "work of", "study", 
    "decknamen", "laboratory", "reconstruction", "early modern", "chymistry"
]

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def score_context(text, term):
    score = 0
    lower_text = text.lower()
    for marker in HISTORIOGRAPHY_MARKERS:
        if marker in lower_text:
            score += 1
    return score

def scholar_mine(scholar_name, output_dir="data/historiography"):
    config = load_config()
    db = Database(config.db_path)
    
    # Handle variations (e.g., "Principe")
    surname = scholar_name.split()[-1]
    query_term = f"%{surname}%"
    
    print(f"Historiography Mining for scholar: '{scholar_name}' (Query: {surname})...")

    results = []
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Build Query
        sql = "SELECT content, document_id, page_number FROM document_chunks WHERE content LIKE ?"
        cursor.execute(sql, (query_term,))
        chunks = cursor.fetchall()
        
        print(f"Found {len(chunks)} raw chunks containing '{surname}'. Processing...")
        
        for content, doc_id, page in chunks:
            # Filter: Check if the full name (or close variant) is present if the surname is common?
            # For now, assume surnames like "Principe" or "Newman" are specific enough in this corpus.
            # But "Smith" (Pamela Smith) might be noisy.
            
            if scholar_name.split()[0].lower() not in content.lower() and len(scholar_name.split()) > 1:
                # If full name is "Lawrence Principe", but chunk only has "Principe", we might keep it 
                # but maybe give it a slight penalty or check for initials?
                # Actually, "Principe argues..." is common. Let's keep surname matches but rely on scoring.
                pass

            score = score_context(content, scholar_name)
            
            if score > 0: # Only keep if it has some academic marker
                 # Metadata fetch
                cursor.execute("SELECT title, author, year FROM documents WHERE id = ?", (doc_id,))
                doc_meta = cursor.fetchone()
                doc_title = doc_meta[0] if doc_meta else "Unknown Document"
                doc_author = doc_meta[1] if doc_meta else "Unknown Author"
                doc_year = doc_meta[2] if doc_meta else "Unknown Year"

                results.append({
                    "score": score,
                    "document": f"{doc_title} ({doc_year})",
                    "page": page,
                    "content": clean_text(content)
                })
            
    # Sort by score (descending)
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # Take top 20
    top_results = results[:20]
    
    # Output to file
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / f"{surname.lower()}_profile.txt"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"HISTORIOGRAPHY REPORT: {scholar_name.upper()}\n")
        f.write(f"Total Occurrences: {len(results)}\n")
        f.write(f"Top {len(top_results)} Academic Contexts Selected\n")
        f.write("="*80 + "\n\n")
        
        for i, res in enumerate(top_results):
            f.write(f"--- MATCH {i+1} (Score: {res['score']}) ---\n")
            f.write(f"Source: {res['document']}, Page {res['page']}\n")
            f.write(f"Content: {res['content']}\n")
            f.write("\n")
            
    print(f"Saved profile contexts to {file_path}")

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "Lawrence Principe"
    scholar_mine(name)
