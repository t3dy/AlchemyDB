import sqlite3
import json
from scripts.db import Database
from scripts.config_loader import load_config

def populate_scholarly_reviews_lexicon():
    config = load_config()
    db = Database(config.db_path)
    
    entries = [
        {"term": "Charles G. Nauert, Jr.", "category": "Scholar", "definition": "Historian of the Renaissance and author of reviews for 'The Business of Alchemy'. Provided critical context on the Holy Roman Empire's court culture."},
        {"term": "Keith Tribe", "category": "Scholar", "definition": "Historian of economic thought; reviewed 'The Business of Alchemy' in Isis, highlighting the alchemical-industrial links."},
        {"term": "Paula Findlen", "category": "Scholar", "definition": "Prominent historian of early modern science (e.g., 'Possessing Nature'). Her work on the culture of collecting and curiosity cabinets (Wunderkammern) overlaps with alchemical material culture."},
        {"term": "Renaissance Quarterly", "category": "Publication", "definition": "Interdisciplinary journal where 'The Business of Alchemy' was reviewed by Nauert, highlighting the scholarly reception of socio-economic alchemical history."},
        {"term": "Isis (Journal)", "category": "Publication", "definition": "Leading journal in the history of science where Keith Tribe and others reviewed the shift toward material and economic alchemical history."},
        {"term": "Vannoccio Biringuccio", "category": "Alchemist / Technologist", "definition": "Author of 'De la pirotechnia' (1540). Grouped alchemy within the 'arts of fire', bridging metallurgy and chemical theory."},
        {"term": "Artisanal Authority", "category": "Scholarly Framework", "definition": "Concept explored by Smith and others where hands-on material knowledge (the 'body of the artisan') claims its own epistemic status alongside textual learning."},
        {"term": "Knowledge Economy Role", "category": "Scholarly Framework", "definition": "The functional position of alchemical practice within a court or state's economic reform plans (e.g., Becher as a fiscal reformer)."},
        {"term": "Experimental Lineage", "category": "Scholarly Framework", "definition": "Tracking the evolution of specific laboratory practices (e.g., thermal analysis) across generations of practitioners (Dwight, Tschirnhaus, Böttger)."}
    ]

    with db.get_connection() as conn:
        cursor = conn.cursor()
        for e in entries:
            cursor.execute("""
                INSERT INTO lexicon (term, category, definition)
                VALUES (?, ?, ?)
                ON CONFLICT(term) DO UPDATE SET
                    category=excluded.category,
                    definition=excluded.definition
            """, (e['term'], e['category'], e['definition']))
        conn.commit()
    print(f"Populated {len(entries)} scholarly review entries into Lexicon.")

if __name__ == "__main__":
    populate_scholarly_reviews_lexicon()
