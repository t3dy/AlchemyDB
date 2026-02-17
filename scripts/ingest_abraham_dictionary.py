"""
Ingest Abraham-style dictionary entries into the database.

This script parses the abraham_dictionary_entries.md file and ingests
the prose-based entries into the lexicon table.
"""

import re
import sqlite3
from pathlib import Path
from scripts.db import Database

def parse_abraham_entries(file_path):
    """Parse Abraham-style prose entries from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by entry separators (## Term)
    sections = re.split(r'\n## ', content)
    
    entries = []
    for section in sections:
        if not section.strip() or section.startswith('#'):
            continue
            
        lines = section.split('\n')
        term = lines[0].strip()
        
        # The entire section is the full entry
        full_content = f"## {term}\n{section}"
        
        # Extract first sentence as short definition
        # Remove markdown formatting and get first sentence
        text_only = re.sub(r'\*\*(.*?)\*\*', r'\1', section)  # Remove bold
        text_only = re.sub(r'\*(.*?)\*', r'\1', text_only)    # Remove italics
        text_only = re.sub(r'\n+', ' ', text_only)             # Remove newlines
        
        # Get first sentence (up to first period followed by space or end)
        first_sentence_match = re.search(r'^[^.]+\.(?:\s|$)', text_only)
        short_def = first_sentence_match.group(0).strip() if first_sentence_match else text_only[:200] + "..."
        
        # Determine category from content
        category = "Uncategorized"
        if any(word in term.lower() for word in ['mercury', 'sulphur', 'salt', 'antimony', 'vitriol', 'cinnabar']):
            category = "Substance"
        elif any(word in term.lower() for word in ['alembic', 'athanor', 'apparatus', 'egg', 'furnace']):
            category = "Apparatus"
        elif any(word in term.lower() for word in ['nigredo', 'albedo', 'rubedo', 'stone', 'philosopher']):
            category = "Concept"
        elif any(word in section.lower() for word in ['born', 'physician', 'alchemist', 'philosopher', 'died']):
            category = "Practitioner"
        elif any(word in term.lower() for word in ['turba', 'rosarium', 'emerald', 'tablet']):
            category = "Text"
        
        entries.append({
            "term": term,
            "category": category,
            "definition": short_def,
            "body": full_content
        })
    
    return entries

def ingest_abraham_dictionary():
    """Ingest Abraham-style dictionary entries into the database."""
    file_path = Path("data/abraham_dictionary_entries.md")
    
    if not file_path.exists():
        print(f"Error: {file_path} not found")
        return
    
    print(f"Parsing entries from {file_path}...")
    entries = parse_abraham_entries(file_path)
    print(f"Parsed {len(entries)} entries.")
    
    db = Database("alchemydb.db")
    
    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        count = 0
        for entry in entries:
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
    ingest_abraham_dictionary()
