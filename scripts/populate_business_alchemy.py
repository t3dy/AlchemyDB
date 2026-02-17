import sqlite3
import json
from pathlib import Path
from scripts.db import Database
from scripts.config_loader import load_config

def populate_business_alchemy():
    config = load_config()
    db = Database(config.db_path)
    
    entries = [
        {
            "full_name": "Pamela H. Smith",
            "type": "Scholar",
            "knowledge_type": "textual / artisanal / political-economic",
            "social_role": "academic philosopher / historian",
            "tradition": "Material Culture Studies / STS",
            "narrative": "Historian of early modern science specializing in artisanal knowledge and the political economy of alchemy. Her work reframed alchemy as embedded in court culture and economic reform.",
            "knowledge_economy_role": "Analyzing alchemy as a vehicle for social capital and economic reform.",
            "primary_works": ["The Business of Alchemy (1994)", "The Body of the Artisan (2004)"]
        },
        {
            "full_name": "Johann Joachim Becher",
            "type": "Alchemist / Political Economist",
            "knowledge_type": "experimental / political-economic",
            "social_role": "court projector",
            "tradition": "Court Alchemy / Mercantilism",
            "narrative": "Self-educated alchemist and court projector active in Mainz, Munich, and Vienna. Linked chemical knowledge to fiscal reform and promoted state-sponsored industry.",
            "knowledge_economy_role": "Advocating manufacturing and mercantilism through alchemical reputation.",
            "participation_type": "experimental / speculative",
            "primary_works": ["Physica subterranea", "Politischer Discurs"]
        },
        {
            "full_name": "Georg Ernst Stahl",
            "type": "Chemist / Theorist",
            "knowledge_type": "experimental",
            "social_role": "academic philosopher / chemist",
            "tradition": "Phlogiston Theory",
            "narrative": "Republished Becher's work and advanced phlogiston theory, creating a chemical lineage from Becher's subterranean physics.",
            "participation_type": "experimental",
            "primary_works": ["Repubished Becher's Physica Subterranea"]
        },
        {
            "full_name": "Gottfried Wilhelm Leibniz",
            "type": "Philosopher / Court Intellectual",
            "knowledge_type": "textual / political-economic",
            "social_role": "court intellectual / advisor",
            "tradition": "Rationalism",
            "narrative": "Engaged in alchemical-industrial speculation and tracked Becher's projects, showing that canonical rationalists were deep participants in alchemical-industrial schemes.",
            "participation_type": "advisory / speculative"
        },
        {
            "full_name": "George Starkey",
            "type": "Alchemist / Colonial Intellectual",
            "knowledge_type": "experimental",
            "social_role": "artisan / experimental chemist",
            "tradition": "Corpuscular Alchemy",
            "narrative": "Harvard-educated alchemist who became influential in London. Developed 'philosophical mercury' and was a major influence on Newton. Wrote under the pseudonym Eirenaeus Philalethes.",
            "participation_type": "experimental",
            "primary_works": ["The Marrow of Alchemy (as Philalethes)"]
        }
    ]

    with db.get_connection() as conn:
        cursor = conn.cursor()
        for e in entries:
            # 1. Update/Insert Entity
            cursor.execute("""
                INSERT INTO entities (name, entity_type, knowledge_type, social_role, participation_type, confidence)
                VALUES (?, ?, ?, ?, ?, 1.0)
                ON CONFLICT(name) DO UPDATE SET
                    entity_type=excluded.entity_type,
                    knowledge_type=excluded.knowledge_type,
                    social_role=excluded.social_role,
                    participation_type=excluded.participation_type
            """, (e['full_name'], e['type'], e.get('knowledge_type'), e.get('social_role'), e.get('participation_type')))
            
            entity_id = cursor.execute("SELECT id FROM entities WHERE name = ?", (e['full_name'],)).fetchone()[0]
            
            # 2. Update/Insert Biography
            cursor.execute("""
                INSERT INTO biographies (entity_id, full_name, tradition, narrative_summary, primary_texts_json, knowledge_economy_role)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(entity_id) DO UPDATE SET
                    tradition=excluded.tradition,
                    narrative_summary=excluded.narrative_summary,
                    primary_texts_json=excluded.primary_texts_json,
                    knowledge_economy_role=excluded.knowledge_economy_role
            """, (entity_id, e['full_name'], e['tradition'], e['narrative'], json.dumps(e.get('primary_works', [])), e.get('knowledge_economy_role')))

            # 3. Handle Aliases for George Starkey
            if e['full_name'] == "George Starkey":
                cursor.execute("INSERT OR IGNORE INTO entity_aliases (entity_id, alias_name, confidence) VALUES (?, 'Eirenaeus Philalethes', 1.0)", (entity_id,))

        conn.commit()
    print(f"Populated {len(entries)} rich profiles from 'The Business of Alchemy'.")

if __name__ == "__main__":
    populate_business_alchemy()
