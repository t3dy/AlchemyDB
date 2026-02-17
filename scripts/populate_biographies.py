import json
from scripts.db import Database
from scripts.config_loader import load_config

def populate_seed_biographies(config):
    db = Database(config.db_path)
    
    biographies = [
        {
            "entity_name": "Paracelsus",
            "full_name": "Theophrastus von Hohenheim",
            "lifespan": "1493–1541",
            "tradition": "Iatrochemistry, Paracelsianism",
            "narrative_summary": "A revolutionary physician and alchemist who rejected traditional Scholastic medicine in favor of a chemical approach to healing. He introduced the *Tria Prima* (Salt, Sulphur, Mercury) as the foundational principles of matter and health. His work often sought to synthesize alchemical practice with spiritual and theological insights.",
            "milestones": [
                {"year": "1493", "event": "Born in Einsiedeln, Switzerland."},
                {"year": "1515", "event": "Allegedly received doctorate in Ferrara, Italy."},
                {"year": "1527", "event": "Burned Avicenna's medical books in Basel, initiating his radical reforms."},
                {"year": "1530", "event": "Wrote Paramirum and Paragranum, defining his medical philosophy."},
                {"year": "1541", "event": "Died in Salzburg, leaving behind a massive corpus of texts."}
            ],
            "primary_texts": [
                "Opus Paramirum",
                "Astronomia Magna",
                "Archidoxis"
            ]
        },
        {
            "entity_name": "Michael Maier",
            "full_name": "Michael Maier",
            "lifespan": "1568–1622",
            "tradition": "Hermetic Alchemy, Rosicrucianism",
            "narrative_summary": "German physician, counselor, and alchemist to Rudolf II. Maier is best known for his emblem books, particularly *Atalanta Fugiens*, which integrated alchemy with mythology and music. He was a central figure in the intellectual circles of the 'Rosicrucian Enlightenment'.",
            "milestones": [
                {"year": "1568", "event": "Born in Rendsburg, Holstein."},
                {"year": "1608", "event": "Entered the service of Emperor Rudolf II in Prague."},
                {"year": "1617", "event": "Published Atalanta Fugiens, his most famous emblem work."},
                {"year": "1622", "event": "Died in Magdeburg."}
            ],
            "primary_texts": [
                "Atalanta Fugiens",
                "Arcana Arcanissima",
                "Symbola Aureae Mensae"
            ]
        },
        {
            "entity_name": "John Dee",
            "full_name": "John Dee",
            "lifespan": "1527–1608",
            "tradition": "Hermeticism, Neoplatonism, Enochian Magick",
            "narrative_summary": "Advisor to Queen Elizabeth I and a towering figure in the English Renaissance. Dee was a mathematician, astronomer, and alchemist who sought a unified understanding of the physical and spiritual worlds. His *Monas Hieroglyphica* is one of the most dense symbolic works in the Western Esoteric tradition.",
            "milestones": [
                {"year": "1527", "event": "Born in London."},
                {"year": "1564", "event": "Published Monas Hieroglyphica in Antwerp."},
                {"year": "1582", "event": "Refined his alchemical and magical collaborations with Edward Kelley."},
                {"year": "1583", "event": "Traveled to Europe to demonstrate his knowledge to Emperor Rudolf II."},
                {"year": "1608", "event": "Died at Mortlake in poverty."}
            ],
            "primary_texts": [
                "Monas Hieroglyphica",
                "Propeudeumata Aphoristica",
                "General and Rare Memorials pertayning to the Perfect Arte of Navigation"
            ]
        }
    ]

    with db.get_connection() as conn:
        cursor = conn.cursor()
        for bio in biographies:
            # Find the entity_id
            cursor.execute("SELECT id FROM entities WHERE name = ?", (bio["entity_name"],))
            entity_row = cursor.fetchone()
            
            if entity_row:
                entity_id = entity_row[0]
                cursor.execute("""
                    INSERT OR REPLACE INTO biographies 
                    (entity_id, full_name, lifespan, tradition, narrative_summary, milestones_json, primary_texts_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    entity_id,
                    bio["full_name"],
                    bio["lifespan"],
                    bio["tradition"],
                    bio["narrative_summary"],
                    json.dumps(bio["milestones"]),
                    json.dumps(bio["primary_texts"])
                ))
                print(f"Populated biography for {bio['entity_name']}")
            else:
                print(f"Warning: Entity '{bio['entity_name']}' not found in database. Skipping biography.")
        
        conn.commit()

if __name__ == "__main__":
    config = load_config()
    populate_seed_biographies(config)
