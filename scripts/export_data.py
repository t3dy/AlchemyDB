import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def export_to_json(config):
    db = Database(config.db_path)
    output_path = Path(config.exports_path) / "docs.json"
    candidates_path = Path(config.exports_path) / "candidates.json"
    
    # Ensure exports directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with db.get_connection() as conn:
        conn.row_factory = sqlite3_row_factory
        cursor = conn.cursor()

        # 1. Export Documents
        cursor.execute("""
            SELECT 
                d.id, d.title, d.author, d.year, d.doc_type, d.created_at, d.updated_at,
                f.file_path, f.file_size, f.sha256, f.mtime
            FROM documents d
            LEFT JOIN document_files f ON d.id = f.document_id
        """)
        documents = cursor.fetchall()

        # 2. Export Candidates (Entities + Mentions)
        cursor.execute("""
            SELECT 
                e.id, e.name, e.entity_type, e.tradition, e.description, e.is_verified,
                em.id as mention_id, em.quote, em.document_id, em.confidence_score
            FROM entities e
            LEFT JOIN entity_mentions em ON e.id = em.entity_id
        """)
        candidates = cursor.fetchall()

    with open(output_path, "w") as f:
        json.dump(documents, f, indent=2)

    with open(candidates_path, "w") as f:
        json.dump(candidates, f, indent=2)
    
    print(f"Exported {len(documents)} documents to {output_path}")
    print(f"Exported {len(candidates)} candidates to {candidates_path}")

def sqlite3_row_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__ == "__main__":
    config = load_config()
    export_to_json(config)
