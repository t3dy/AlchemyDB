import sqlite3
import re
from scripts.db import Database
from scripts.config_loader import load_config

def mine_broad(config):
    db = Database(config.db_path)
    
    with db.get_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # 1. Load Lexicon
        print("Loading lexicon...")
        cursor.execute("SELECT term, definition FROM lexicon")
        lexicon = {row["term"].lower(): row["term"] for row in cursor.fetchall()}
        
        # 2. Build Regex for broad matching
        # Sort terms by length descending to match longest phrases first
        sorted_terms = sorted(lexicon.keys(), key=len, reverse=True)
        # Escape terms and wrap in word boundaries
        pattern_str = r'\b(' + '|'.join(re.escape(term) for term in sorted_terms) + r')\b'
        lexicon_regex = re.compile(pattern_str, re.IGNORECASE)

        # 3. Get Chunks
        print("Fetching document chunks...")
        cursor.execute("SELECT id, document_id, content, page_number FROM document_chunks")
        chunks = cursor.fetchall()
        
        print(f"Scanning {len(chunks)} chunks for {len(lexicon)} terms...")
        
        mentions_added = 0
        entities_created = 0

        for chunk in chunks:
            content = chunk["content"]
            matches = lexicon_regex.findall(content)
            
            if matches:
                # Deduplicate matches in the same chunk
                unique_matches = set(match.lower() for match in matches)
                
                for match_lower in unique_matches:
                    term_display = lexicon[match_lower]
                    
                    # Ensure entity exists in entities table
                    cursor.execute("SELECT id FROM entities WHERE name = ?", (term_display,))
                    entity_row = cursor.fetchone()
                    
                    if not entity_row:
                        # Create entity as a candidate
                        # Determine entity type based on lexicon definition prefix if available
                        cursor.execute("SELECT definition FROM lexicon WHERE term = ?", (term_display,))
                        lex_def = cursor.fetchone()["definition"]
                        
                        entity_type = "candidate"
                        if "[Practitioner]" in lex_def: entity_type = "alchemist"
                        elif "[Text]" in lex_def: entity_type = "manuscript"
                        elif "[Substance]" in lex_def: entity_type = "substance"
                        elif "[Allegory]" in lex_def: entity_type = "theory"
                        elif "[Apparatus]" in lex_def: entity_type = "equipment"

                        cursor.execute("""
                            INSERT INTO entities (name, entity_type, tradition, description, is_verified)
                            VALUES (?, ?, ?, ?, 0)
                        """, (term_display, entity_type, "Unknown", lex_def))
                        entity_id = cursor.lastrowid
                        entities_created += 1
                    else:
                        entity_id = entity_row["id"]

                    # Extract context (quote) - roughly 15 words around the match
                    # For simplicity, we can use a regex search to find the specific instance and grab surrounding text
                    match_pos = content.lower().find(match_lower)
                    start = max(0, match_pos - 100)
                    end = min(len(content), match_pos + len(match_lower) + 100)
                    quote = content[start:end].strip()
                    if start > 0: quote = "..." + quote
                    if end < len(content): quote = quote + "..."

                    # Insert mention
                    cursor.execute("""
                        INSERT INTO entity_mentions (entity_id, document_id, quote, confidence_score)
                        VALUES (?, ?, ?, ?)
                    """, (entity_id, chunk["document_id"], quote, 0.8))
                    mentions_added += 1

            if mentions_added % 100 == 0 and mentions_added > 0:
                conn.commit() # Commit periodically

        conn.commit()
        print(f"Mining complete. Created {entities_created} entities and {mentions_added} mentions.")

if __name__ == "__main__":
    config = load_config()
    mine_broad(config)
