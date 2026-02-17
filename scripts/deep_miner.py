import sqlite3
import json
import re
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

# Words that suggest a context is "theoretically significant" rather than just a passing mention
SIGNIFICANCE_MARKERS = [
    "symbol", "allegory", "philosoph", "principle", "mercury", "salt", "king", "queen", 
    "dragon", "lion", "stage", "color", "nature", "stone", "work", "art", "secret", 
    "meaning", "represents", "signifies", "called"
]

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def score_context(text, term):
    score = 0
    lower_text = text.lower()
    for marker in SIGNIFICANCE_MARKERS:
        if marker in lower_text:
            score += 1
    return score

def deep_mine(term, output_dir="data/deep_mining"):
    config = load_config()
    db = Database(config.db_path)
    
    print(f"Deep Mining for term: '{term}'...")
    
    # Handle variations (e.g., Sulfur/Sulphur)
    search_term = term
    if term.lower() == "sulfur":
        query_term = "%sulfur%"
        alt_query_term = "%sulphur%"
    else:
        query_term = f"%{term}%"
        alt_query_term = None

    results = []
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Build Query
        sql = "SELECT content, document_id, page_number FROM document_chunks WHERE content LIKE ?"
        params = [query_term]
        
        if alt_query_term:
            sql += " OR content LIKE ?"
            params.append(alt_query_term)
            
        cursor.execute(sql, params)
        chunks = cursor.fetchall()
        
        print(f"Found {len(chunks)} raw chunks containing '{term}'. Processing...")
        
        for content, doc_id, page in chunks:
            # Find all occurrences in this chunk
            # Simple approach: if found, take the whole chunk (since chunks are usually 1000 chars)
            # Better approach: find indices and extract window? 
            # Our chunks are likely paragraphs or pages, so taking the whole chunk might be good context.
            # Let's take the whole chunk but score it.
            
            score = score_context(content, term)
            
            # Metadata fetch (optional: get document title)
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
    
    # Take top 20 most significant contexts
    top_results = results[:20]
    
    # Output to file
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    file_path = out_path / f"{term.lower().replace(' ', '_')}_context.txt"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"DEEP MINING REPORT: {term.upper()}\n")
        f.write(f"Total Occurrences: {len(results)}\n")
        f.write(f"Top {len(top_results)} Significant Contexts Selected\n")
        f.write("="*80 + "\n\n")
        
        for i, res in enumerate(top_results):
            f.write(f"--- MATCH {i+1} (Score: {res['score']}) ---\n")
            f.write(f"Source: {res['document']}, Page {res['page']}\n")
            f.write(f"Content: {res['content']}\n")
            f.write("\n")
            
    print(f"Saved top contexts to {file_path}")

if __name__ == "__main__":
    import sys
    term = sys.argv[1] if len(sys.argv) > 1 else "Sulfur"
    deep_mine(term)
