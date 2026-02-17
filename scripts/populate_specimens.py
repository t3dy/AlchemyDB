from scripts.db import Database
from scripts.config_loader import load_config

def populate_specimens(config):
    db = Database(config.db_path)
    
    entities = [
        {"name": "Heinrich Cornelius Agrippa", "type": "alchemist", "tradition": "Hermetic", "description": "Author of De occulta philosophia, interested in the theory and practice of alchemy."},
        {"name": "Masha'allah ibn Athari", "type": "historical_figure", "tradition": "Persian-Jewish", "description": "8th-century astrologer and astronomer, associated with De elementis and Liber de Orbe."},
        {"name": "Avicebron (Solomon ibn Gabirol)", "type": "author", "tradition": "Neoplatonic", "description": "Author of Fons vitae, central to 12th-century cosmography."},
    ]
    
    lexicon = [
        {"term": "Hyle", "definition": "The 'ultimate superior things' or prime matter in medieval cosmography and alchemy."},
        {"term": "Natural Magic", "definition": "The practice of using hidden powers within nature, as discussed by Agrippa."},
    ]

    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        # Insert Entities
        for e in entities:
            cursor.execute("""
                INSERT INTO entities (name, entity_type, tradition, description, is_verified)
                VALUES (?, ?, ?, ?, ?)
            """, (e["name"], e["type"], e["tradition"], e["description"], 0)) # 0 = Candidate
            e_id = cursor.lastrowid
            
            # Add a mention for Agrippa (Doc 202)
            if "Agrippa" in e["name"]:
                cursor.execute("""
                    INSERT INTO entity_mentions (entity_id, document_id, quote, confidence_score)
                    VALUES (?, ?, ?, ?)
                """, (e_id, 202, "The study of Agrippa's works confirms his constant interest in the theory and practice of alchemy.", 1.0))

            # Add a mention for Masha'allah (Doc 205)
            if "Masha'allah" in e["name"]:
                cursor.execute("""
                    INSERT INTO entity_mentions (entity_id, document_id, quote, confidence_score)
                    VALUES (?, ?, ?, ?)
                """, (e_id, 205, "The same observation applies to two further fundamental treatises, Avicebron's Fons vitae and Domenico Gundisalvi's De processione mundi (ca. 1160).", 0.8))

        # Insert Lexicon
        for l in lexicon:
            cursor.execute("""
                INSERT OR IGNORE INTO lexicon (term, definition, is_verified)
                VALUES (?, ?, ?)
            """, (l["term"], l["definition"], 0))

        conn.commit()
        print("Specimens populated successfully.")

if __name__ == "__main__":
    config = load_config()
    populate_specimens(config)
