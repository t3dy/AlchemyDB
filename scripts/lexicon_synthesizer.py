import sqlite3
import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def synthesize_lexicon():
    config = load_config()
    db = Database(config.db_path)
    
    input_file = Path("data/synthesized_entries.json")
    if not input_file.exists():
        print(f"Synthesis file not found: {input_file}. Please run the miners and prepare the synthesis first.")
        return
    
    with open(input_file, "r", encoding="utf-8") as f:
        entries = json.load(f)
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        for entry in entries:
            # Entry expected to have: term, category, definition (following rich template)
            cursor.execute("""
                INSERT INTO lexicon (term, category, definition)
                VALUES (?, ?, ?)
                ON CONFLICT(term) DO UPDATE SET
                    category=excluded.category,
                    definition=excluded.definition
            """, (entry['term'], entry['category'], entry['definition']))
        conn.commit()
    
    print(f"Successfully synthesized {len(entries)} rich dictionary entries into the database.")

if __name__ == "__main__":
    synthesize_lexicon()
