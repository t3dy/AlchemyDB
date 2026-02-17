import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def export_to_json(config):
    db = Database(config.db_path)
    exports_path = Path("dashboard/src/exports")
    exports_path.mkdir(parents=True, exist_ok=True)
    output_path = exports_path / "docs.json"
    candidates_path = exports_path / "candidates.json"
    lexicon_path = exports_path / "lexicon.json"
    atlas_path = exports_path / "atlas.json"
    biographies_path = exports_path / "biographies.json"
    
    # Ensure exports directory exists
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Export Documents
        cursor.execute("SELECT id, title, author, year, doc_type, description FROM documents")
        docs = [dict(zip(["id", "title", "author", "year", "doc_type", "description"], row)) for row in cursor.fetchall()]
        with open(output_path, "w") as f:
            json.dump(docs, f, indent=2)
        print(f"Exported {len(docs)} documents to {output_path}")
        
        # 2. Export Candidates (Rich Metadata)
        cursor.execute("SELECT id, name, entity_type, confidence, knowledge_type, social_role, participation_type FROM entities")
        entities = [dict(zip(["id", "name", "entity_type", "confidence", "knowledge_type", "social_role", "participation_type"], row)) for row in cursor.fetchall()]
        with open(candidates_path, "w") as f:
            json.dump(entities, f, indent=2)
        print(f"Exported {len(entities)} entities to {candidates_path}")

        # 3. Export Lexicon
        cursor.execute("SELECT id, term, definition, symbol_path, category, is_verified, theoretical_lineage FROM lexicon")
        lexicon = [dict(zip(["id", "term", "definition", "symbol_path", "category", "is_verified", "theoretical_lineage"], row)) for row in cursor.fetchall()]
        with open(lexicon_path, "w") as f:
            json.dump(lexicon, f, indent=2)
        print(f"Exported {len(lexicon)} lexicon terms to {lexicon_path}")

        # 4. Export Atlas (Rich Mentions / Highlights)
        cursor.execute("SELECT id, name, entity_type, description FROM entities WHERE confidence > 0.8")
        atlas = [dict(zip(["id", "name", "type", "description"], row)) for row in cursor.fetchall()]
        with open(atlas_path, "w") as f:
            json.dump(atlas, f, indent=2)
        print(f"Exported {len(atlas)} atlas entries to {atlas_path}")

        # 5. Export Biographies
        cursor.execute("SELECT entity_id, full_name, lifespan, tradition, narrative_summary, milestones_json, primary_texts_json, knowledge_economy_role FROM biographies")
        bios = []
        for row in cursor.fetchall():
            bio = dict(zip(["entity_id", "full_name", "lifespan", "tradition", "narrative_summary", "milestones_json", "primary_texts_json", "knowledge_economy_role"], row))
            bio["milestones"] = json.loads(bio["milestones_json"]) if bio["milestones_json"] else []
            bio["primary_texts"] = json.loads(bio["primary_texts_json"]) if bio["primary_texts_json"] else []
            del bio["milestones_json"]
            del bio["primary_texts_json"]
            bios.append(bio)
        with open(biographies_path, "w") as f:
            json.dump(bios, f, indent=2)
        print(f"Exported {len(bios)} biographies to {biographies_path}")

def sqlite3_row_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__ == "__main__":
    config = load_config()
    export_to_json(config)
