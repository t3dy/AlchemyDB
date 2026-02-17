import sqlite3
import json
from datetime import datetime
from scripts.db import Database
from scripts.config_loader import load_config

def populate_scholars():
    config = load_config()
    db = Database(config.db_path)
    
    scholars = [
        {
            "full_name": "William R. Newman",
            "tradition": "New Historiography / Chymistry",
            "lifespan": "Modern",
            "narrative": "A leading figure in the 'New Historiography' of alchemy, Newman's work focuses on the experimental and corpuscular nature of alchemical practice, particularly in the works of 'Geber' and Isaac Newton.",
            "milestones": [
                {"year": "1994", "event": "Published 'The Summa Perfectionis of Pseudo-Geber'"},
                {"year": "2006", "event": "Published 'Atoms and Alchemy'"},
                {"year": "2019", "event": "Published 'Newton the Alchemist'"}
            ],
            "primary_works": ["Newton the Alchemist", "Atoms and Alchemy", "The Summa Perfectionis of Pseudo-Geber"]
        },
        {
            "full_name": "Lawrence M. Principe",
            "tradition": "New Historiography / Chymistry",
            "lifespan": "Modern",
            "narrative": "A chemist and historian, Principe has pioneered the laboratory reconstruction of alchemical experiments, arguing for the term 'Chymistry' to describe the unified field of chemistry and alchemy in the 17th century.",
            "milestones": [
                {"year": "1998", "event": "Published 'The Aspiring Adept'"},
                {"year": "2013", "event": "Published 'The Secrets of Alchemy'"}
            ],
            "primary_works": ["The Secrets of Alchemy", "The Aspiring Adept"]
        },
        {
            "full_name": "Didier Kahn",
            "tradition": "New Historiography / Paracelsianism",
            "lifespan": "Modern",
            "narrative": "Kahn is a preeminent scholar of Paracelsianism and early modern French alchemy, known for his rigorous archival research and analysis of the philosophical and medical shifts in the 16th and 17th centuries.",
            "milestones": [
                {"year": "2007", "event": "Published 'Alchimie et paracelsisme en France'"}
            ],
            "primary_works": ["Alchimie et paracelsisme en France"]
        },
        {
            "full_name": "Barbara Obrist",
            "tradition": "New Historiography / Iconography",
            "lifespan": "Modern",
            "narrative": "Obrist specializes in the visualization of alchemical and cosmological concepts in medieval and early modern manuscripts, focusing on the intersection of art, science, and philosophy.",
            "milestones": [
                {"year": "1982", "event": "Published 'Les débuts de l'imagerie alchimique'"}
            ],
            "primary_works": ["Les débuts de l'imagerie alchimique"]
        },
        {
            "full_name": "Peter Forshaw",
            "tradition": "New Historiography / Christian Cabala",
            "lifespan": "Modern",
            "narrative": "Forshaw explores the intersections of alchemy, magic, and religion, with particular expertise in the works of John Dee and Heinrich Khunrath.",
            "milestones": [
                {"year": "2005", "event": "Detailed study of Khunrath's Amphitheatrum Sapientiae Eterna"}
            ],
            "primary_works": ["Curious Knowledge"]
        },
        {
            "full_name": "Allen Debus",
            "tradition": "New Historiography / Paracelsian Tradition",
            "lifespan": "1926-2009",
            "narrative": "A foundational historian of science who championed the study of the Paracelsian tradition as a vital component of the Scientific Revolution.",
            "milestones": [
                {"year": "1965", "event": "Published 'The English Paracelsians'"},
                {"year": "1977", "event": "Published 'The Chemical Philosophy'"}
            ],
            "primary_works": ["The Chemical Philosophy", "The English Paracelsians"]
        },
        {
            "full_name": "Tara Nummedal",
            "tradition": "New Historiography / Labor & Gender",
            "lifespan": "Modern",
            "narrative": "Nummedal examines the social and cultural history of alchemy, focusing on the practical labor of alchemists and the role of alchemy in early modern courts.",
            "milestones": [
                {"year": "2007", "event": "Published 'Alchemy and Authority in the Holy Roman Empire'"}
            ],
            "primary_works": ["Alchemy and Authority in the Holy Roman Empire"]
        },
        {
            "full_name": "Anke Timmerman",
            "tradition": "New Historiography / Manuscripts",
            "lifespan": "Modern",
            "narrative": "Specialist in alchemical manuscripts and verse, particularly in the Middle English tradition, her work bridges literary analysis and the history of science.",
            "milestones": [
                {"year": "2013", "event": "Published 'Verse and Transmutation'"}
            ],
            "primary_works": ["Verse and Transmutation"]
        },
        {
            "full_name": "Pamela Smith",
            "tradition": "New Historiography / Material Culture",
            "lifespan": "Modern",
            "narrative": "Smith's work explores the 'body of the artisan,' arguing that material knowledge and laboratory practice were foundational to the development of modern science.",
            "milestones": [
                {"year": "1994", "event": "Published 'The Business of Alchemy'"},
                {"year": "2004", "event": "Published 'The Body of the Artisan'"}
            ],
            "primary_works": ["The Body of the Artisan", "The Business of Alchemy"]
        }
    ]

    with db.get_connection() as conn:
        cursor = conn.cursor()
        
        for s in scholars:
            # 1. Add to Lexicon if not exists
            cursor.execute("""
                INSERT OR IGNORE INTO lexicon (term, category, definition)
                VALUES (?, 'Scholar', ?)
            """, (s['full_name'], s['narrative']))
            
            # 2. Get the entity_id
            cursor.execute("SELECT id FROM entities WHERE name = ?", (s['full_name'],))
            row = cursor.fetchone()
            if row:
                entity_id = row[0]
            else:
                # Create entity if it doesn't exist
                cursor.execute("INSERT INTO entities (name, entity_type, confidence) VALUES (?, 'Scholar', 1.0)", (s['full_name'],))
                entity_id = cursor.lastrowid
            
            # 3. Add to Biographies
            cursor.execute("""
                INSERT OR REPLACE INTO biographies 
                (entity_id, full_name, lifespan, tradition, narrative_summary, milestones_json, primary_texts_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                entity_id,
                s['full_name'],
                s['lifespan'],
                s['tradition'],
                s['narrative'],
                json.dumps(s['milestones']),
                json.dumps(s['primary_works'])
            ))
            
            print(f"Added scholar: {s['full_name']}")
            
        conn.commit()

if __name__ == "__main__":
    populate_scholars()
