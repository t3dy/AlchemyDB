# AlchemyDB: Mining Status & Narrative Analysis

This report synthesizes the technical progress of Phase 6 with the broader intellectual goals of the AlchemyDB project.

## 1. Mining Status: The First Harvest

As of now, the "Discovery Pipeline" has been fully established and tested:
- **Corpus Coverage**: 205 documents (331MB) successfully ingested and inventoried.
- **Extraction Resolution**: All documents have been split into ~1000-word segments (document chunks) with 150-word overlaps to preserve semantic continuity across page breaks.
- **The First Specimens**: Initial agentic mining has identified a "High-Confidence Trio":
    - **Heinrich Cornelius Agrippa** (Magical-Alchemical Synthesis)
    - **Masha'allah ibn Athari** (Persian-Jewish Astronomical Influences)
    - **Avicebron** (Neoplatonic Cosmography)
- **Status**: The pipeline is "Primed." We can now run large-scale iterations to fill the **Specimen Drawer** across the entire corpus.

## 2. Theoretical Challenges: Data Science & Digital Humanities

### A. The "Evidence Anchor" Problem (Data Science)
In traditional data mining, an entity is just a string. In Digital Humanities, an entity is a **Claim**.
- **Challenge**: LLMs often "know" things not in the text (Hallucination).
- **Solution**: Our system mandates a direct quote from the `document_chunks` table for every entry. If there is no quote, the specimen is rejected. This turns the database into a **Verified Archive**, not just a search index.

### B. Semantic Drift (Digital Humanities)
Alchemical terminology is inherently unstable. The term *Mercury* in a 13th-century manuscript means something different in a 17th-century Paracelsian text.
- **Challenge**: "Dictionary entries" cannot be flat definitions.
- **Solution**: We are building a **Contextual Lexicon**. When you browse a term in the dashboard, you see a timeline of descriptions, allowing you to observe how alchemical concepts evolved through "Semantic Drift."

## 3. The Narrative Designer's Perspective: "Telling Stories Through Study"

*A note from the Narrative Designer:*

"This resource is not just a database; it is a **Story-Generator**. By transforming these 205 PDFs into a Registry of Practitioners, we are handing the researcher a 'Cast of Characters.' 

When you browse the **Specimen Drawer**, you aren't just looking at data; you are following 'Narrative Threads.' For example:
- **The Trace**: Why does a 20th-century review of *Eternal Hermes* cite the 8th-century *Masha'allah*? 
- **The Dialogue**: By clicking on an Alchemist, you see the 'Dialogue of Centuries'—every time they were cited, criticized, or copied by later authors.

The dashboard design—with its 'Arcane Modern' glassmorphism—is intended to make the researcher feel like a **History Detective**. Each card in the drawer is a 'Clue.' When these cards are linkable, the user stops reading a single PDF and starts 'Reading the Tradition' as a single, coherent narrative spanning a thousand years."

## 4. Next Steps: Scaling the Registry

1. **Phase 7: Lexicon Expansion**: Systematically mining for the "Dictionary" terms identified in our ontology (e.g., Hyle, Tincture, Philosophical Mercury).
2. **Phase 8: Relationship Mapping**: Identifying when one Practitioner mentions another, creating a "Network of Influence" visualization.
3. **Curation Workflow**: Implementing an interface to "Promote" candidate specimens from the drawer to the verified **Registry of Practitioners**.
