import sqlite3
import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

# Common alchemical substances and their suspected modern counterparts (for heuristic)
SUBSTANCES = {
    "vitriol": ["ferrous sulfate", "copper sulfate", "sulfuric acid"],
    "nitre": ["potassium nitrate", "saltpeter"],
    "antimony": ["stibnite", "antimony trisulfide"],
    "cinnabar": ["mercury(II) sulfide"],
    "aqua fortis": ["nitric acid"],
    "aqua regia": ["nitro-hydrochloric acid"],
    "sal ammoniac": ["ammonium chloride"],
    "spirit of salt": ["hydrochloric acid"],
    "oil of vitriol": ["concentrated sulfuric acid"],
    "butter of antimony": ["antimony trichloride"],
    "fixed nitre": ["potassium carbonate"],
    "sugar of lead": ["lead(II) acetate"]
}

def mine_substances():
    config = load_config()
    db = Database(config.db_path)
    
    findings = []
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        for term, modern_options in SUBSTANCES.items():
            print(f"Mining term: {term}...")
            # Case-insensitive search in chunks
            query = f"SELECT content, document_id, page_number FROM document_chunks WHERE content LIKE '%{term}%'"
            cursor.execute(query)
            chunks = cursor.fetchall()
            
            for chunk in chunks:
                content, doc_id, page = chunk
                # Find the position of the term
                idx = content.lower().find(term.lower())
                if idx != -1:
                    start = max(0, idx - 200)
                    end = min(len(content), idx + 200)
                    context = content[start:end]
                    
                    findings.append({
                        "term": term,
                        "modern_options": modern_options,
                        "context": context,
                        "document_id": doc_id,
                        "page": page
                    })
    
    # Save findings for lexical synthesis
    output_file = Path("data/substance_findings.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)
    
    print(f"Mined {len(findings)} mentions. Results saved to {output_file}")

if __name__ == "__main__":
    mine_substances()
