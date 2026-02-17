import sqlite3
import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

EQUIPMENT = {
    "alembic": "Distillation head used for condensing vapors.",
    "retort": "Spherical vessel with a long downward-pointing neck used for distillation.",
    "furnace": "Heat source, often categorized by specialized types (Athannor, Wind Furnace).",
    "athannor": "Self-feeding furnace used for maintaining constant temperature in 'long works'.",
    "cucurbit": "The lower part of a distillation apparatus (the 'gourd').",
    "pelican": "A circulatory distillation vessel with two side arms for returning distillate.",
    "crucible": "Vessel used for high-temperature melting or calcination.",
    "mortar": "Used for grinding and pulverizing solid substances."
}

def mine_equipment():
    config = load_config()
    db = Database(config.db_path)
    
    findings = []
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        for term, default_def in EQUIPMENT.items():
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
                        "default_function": default_def,
                        "context": context,
                        "document_id": doc_id,
                        "page": page
                    })
    
    output_file = Path("data/equipment_findings.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(findings, f, indent=2)
    
    print(f"Mined {len(findings)} mentions. Results saved to {output_file}")

if __name__ == "__main__":
    mine_equipment()
