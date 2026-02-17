import re
import sqlite3
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def parse_markdown_entries(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by level 2 headers (Entries)
    # The file starts with a header, so the first split might be preamble
    sections = re.split(r'\n## ', content)
    
    entries = []
    
    # Skip the first section if it's just the file header
    start_index = 1 if "Robust Dictionary" in sections[0] else 0

    for section in sections[start_index:]:
        # Extract Title
        lines = section.split('\n')
        term = lines[0].strip()
        
        # Extract Category
        category_match = re.search(r'\*\*Category\*\*: (.*)', section)
        category = category_match.group(1).strip() if category_match else "Uncategorized"
        
        # Extract Definition (heuristics: look for "Core Definition" or "Explication")
        # We will store the WHOLE KEY as the definition/body for now to preserve the rich markdown structure in the UI
        # But we also want a short 'definition' for the table view.
        
        short_def_match = re.search(r'### I\. (?:Core Definition|Explication|Summary of Contents|Biographical Abstract)\n(.*?)\n', section, re.DOTALL)
        short_def = short_def_match.group(1).strip() if short_def_match else ""
        
        # If short_def is empty, grab the first paragraph after I.
        if not short_def:
             short_def_match = re.search(r'### I\..*?\n(.*?)\n', section, re.DOTALL)
             short_def = short_def_match.group(1).strip() if short_def_match else "See full entry."
             
        # Full content (re-add the header we split by)
        full_content = f"## {term}\n{section}"

        entries.append({
            "term": term,
            "category": category,
            "definition": short_def,
            "body": full_content
        })
        
    return entries

def ingest_dictionary():
    config = load_config()
    db = Database(config.db_path)
    
    input_path = Path("c:/AlchemyDB/data/robust_dictionary_entries.md")
    if not input_path.exists():
        print(f"File not found: {input_path}")
        return

    entries = parse_markdown_entries(input_path)
    print(f"Parsed {len(entries)} entries entries.")

    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Ensure 'body' column exists in lexicon (it might not)
        # We can store the full markdown in 'definition' or strict schema?
        # The schema in db.py isn't visible, but export_data.py used:
        # SELECT id, term, definition, symbol_path, category...
        
        # We will assume 'definition' is the text field.
        # To make it robust, let's put the Short Definition in 'definition' 
        # But wait, the previous synthesized_entries.json uses 'definition' for the whole thing?
        # Let's check synthesized_entries.json structure if possible, but time is short.
        # We'll put the SHORT definition in 'definition'.
        # And we'll try to put the FULL markdown in 'theoretical_lineage' or similar unused text field if available, 
        # or just content with short def.
        
        # Actually, let's just update 'definition' with the short one for now to keep the table clean.
        # The 'Specimen Drawer' likely shows 'definition'.
        
        count = 0
        for entry in entries:
            # We assume term is unique or we update it
            try:
                cursor.execute("""
                    INSERT INTO lexicon (term, category, definition, theoretical_lineage)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(term) DO UPDATE SET
                        category=excluded.category,
                        definition=excluded.definition,
                        theoretical_lineage=excluded.theoretical_lineage
                """, (entry['term'], entry['category'], entry['definition'], entry['body']))
                count += 1
            except sqlite3.OperationalError as e:
                # If theoretical_lineage column doesn't exist, fallback
                if "no such column" in str(e):
                     cursor.execute("""
                        INSERT INTO lexicon (term, category, definition)
                        VALUES (?, ?, ?)
                        ON CONFLICT(term) DO UPDATE SET
                            category=excluded.category,
                            definition=excluded.definition
                    """, (entry['term'], entry['category'], entry['definition']))
                     count += 1
                else:
                    raise e
                    
        conn.commit()
        print(f"Upserted {count} entries into 'lexicon' table.")

if __name__ == "__main__":
    ingest_dictionary()
