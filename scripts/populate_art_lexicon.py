import sqlite3
import json
from scripts.db import Database
from scripts.config_loader import load_config

def populate_art_lexicon():
    config = load_config()
    db = Database(config.db_path)
    
    entries = [
        {"term": "Chrysopoeia", "category": "Process", "definition": "The art of making gold through transmutation or coloration. Materials: Lead, copper, mercury, sulfur compounds, metallic salts. Processes: Calcination, sublimation, projection."},
        {"term": "Argyropoeia", "category": "Process", "definition": "The making of silver from base metals. Materials: Copper alloys, lead, white mineral powders. Processes: Surface whitening, alloying, cementation."},
        {"term": "Purple Dyeing (Porphyropoeia)", "category": "Art Material", "definition": "Production of purple coloration in textiles. Materials: Murex dyes, vegetal substitutes, mordants. Processes: Immersion dyeing, fixation, oxidation."},
        {"term": "Artificial Gem Production", "category": "Art Material", "definition": "Coloring crystal quartz or glass to imitate precious stones. Materials: Silica, metallic oxides, copper, iron. Processes: High-temperature fusion."},
        {"term": "Glassmaking (Cristallo)", "category": "Art Material", "definition": "Production of clear or colored glass imitating rock crystal. Materials: Silica sand, potash, soda ash. Processes: Furnace melting, annealing."},
        {"term": "Porcelain Manufacture (Hard-Paste)", "category": "Art Material", "definition": "Production of high-fired ceramic bodies. Materials: Kaolin, feldspar, quartz. Processes: High-temperature kiln firing, glaze chemistry."},
        {"term": "Metallogenetic Theory", "category": "Theory", "definition": "Theories explaining how metals form within the earth. Key Insight: Sulfur-mercury principles; subterranean 'cooking'."},
        {"term": "Assaying", "category": "Process", "definition": "Testing purity of gold or silver using touchstones, cupels, or acids. Connects fraud detection and expertise."},
        {"term": "Cupellation", "category": "Process", "definition": "Refinement process separating precious metals from lead via oxidative heating in bone ash cupels."},
        {"term": "Distillation", "category": "Process", "definition": "Separation of substances through vaporization and condensation using alembics, cucurbits, and retorts."},
        {"term": "Sublimation", "category": "Process", "definition": "Transformation of solids into vapor and recondensation. Key EPistemic Role: Purfication or spiritual ascent."},
        {"term": "Calcination", "category": "Process", "definition": "Heating substances (metals, minerals) in open-air furnaces to drive off volatile components."},
        {"term": "Cementation", "category": "Process", "definition": "Surface transformation of metals via mineral packing and prolonged furnace exposure."},
        {"term": "Fireworks Manufacture", "category": "Art Material", "definition": "Controlled explosive chemistry using saltpeter, sulfur, and charcoal. Overlaps with alchemical language."},
        {"term": "Mineral Dye Production", "category": "Art Material", "definition": "Manufacturing pigments/dyes from mineral salts (iron oxides, copper salts) via grinding and washing."},
        {"term": "Handstein", "category": "Art Material", "definition": "Ornamental mineral specimen displaying metal veins; embodied metallogenetic knowledge."},
        {"term": "Furnace (Fornax)", "category": "Apparatus", "definition": "Core laboratory instrument enabling material transformation. Types: Melting furnace, distillation furnace, porcelain kiln."},
        {"term": "Fonderia", "category": "Space", "definition": "Medici workshop combining pharmacy, metallurgy, and art production. A court-sponsored hybrid lab."},
        {"term": "Kunst- und Werckhaus", "category": "Space", "definition": "Proposed centralized workshop combining chemical laboratories with manufactures (dyes, textiles, acids)."},
        {"term": "Iatrochemistry", "category": "Theory", "definition": "Chemical medicine tradition derived from Paracelsus; focuses on mineral remedies and extracts."},
        {"term": "Laboratories of Art", "category": "Scholarly Framework", "definition": "Framework arguing that early modern labs and workshops shared material cultures, personnel, and practices. Entangles alchemy with luxury goods."}
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
    print(f"Populated {len(entries)} art-alchemical entries into Lexicon.")

if __name__ == "__main__":
    populate_art_lexicon()
