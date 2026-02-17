import sqlite3
import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

PROCESSES = {
    "calcination": ["oxidation", "thermal decomposition"],
    "sublimation": ["solid-to-gas phase change"],
    "distillation": ["separation based on volatility"],
    "cibation": ["addition of liquid to a dry substance"],
    "fermentation": ["decomposition", "biochemical change"],
    "fixation": ["solidification of a volatile substance"],
    "multiplication": ["increasing the power or quantity"],
    "projection": ["the final transformative stage"]
}

def map_processes():
    config = load_config()
    db = Database(config.db_path)
    
    findings = []
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        for term, modern_analogs in PROCESSES.items():
            print(f"Mining term: {term}...")
            query = f"SELECT content, document_id, page_number FROM document_chunks WHERE content LIKE '%{term}%'"
            cursor.execute(query)
            chunks = cursor.fetchall()
            
            for chunk in chunks:
                content, doc_id, page = chunk
                idx = content.lower().find(term.lower())
                if idx != -1:
                    start = max(0, idx - 200)
                    end = min(len(content), idx + 200)
                    context = content[start:end]
                    
                    findings.append({
                        "term": term,
                        "modern_analogs": modern_analogs,
                        "context": context,
                        "document_id": doc_id,
                        "page": page
                    })
    
    output_file = Path("data/process_findings.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)
    
    print(f"Mined {len(findings)} mentions. Results saved to {output_file}")

if __name__ == "__main__":
    map_processes()
