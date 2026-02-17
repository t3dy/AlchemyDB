# Report: Strategic Improvement Plan

Based on the core insights from *The Business of Alchemy* (Smith) and *Gehennical Fire* (Newman), we propose the following strategic enhancements to the AlchemyDB ecosystem.

## 1. Relational Schema Refinement (The "Actor" Model)
We will move beyond biographical data to model **functional roles**.

- **Knowledge Type Encoding**: Add a `knowledge_type` field to entities:
    - `textual`: Primary focus on philology and manuscript tradition.
    - `artisanal`: Focus on material manipulation and workshop practice.
    - `experimental`: Systematic laboratory reconstruction.
    - `political-economic`: Alchemy as economic policy or court capital.

- **Role Taxonomy**: Categorize practitioners by their social function:
    - `{court projector, artisan, academic philosopher, experimental chemist}`.

- **Identity Resolution**: Implement an `entity_aliases` table to handle pseudonymous writing (e.g., Starkey ↔ Philalethes) with `authorship_confidence_score` metadata.

## 2. Dashboard Storytelling Architecture
The dashboard will evolve from a search engine into a **Scholarly Apparatus**.

- **Thematic Toggles**: Users can view the same text/entity through different lenses:
    - `Symbolic Mode`: Focus on spiritual/alchemical allegories.
    - `Political-Economic Mode`: Focus on patronage, economic reform, and court utility.

- **Lineage Graphs**: Visualizing not just "Hermetic Chains" but "Chemical Lineages" (e.g., Becher → Stahl → Phlogiston Theory).

## 3. Data Population Strategy
We will immediately ingest "Rich Profiles" for the following anchor figures from the scholarship:
- **Pamela H. Smith (Scholar)**: Framing knowledge as social capital.
- **Johann Joachim Becher (Projector)**: Alchemy as economic reform.
- **Georg Ernst Stahl (Theorist)**: The Becher-Stahl lineage and Phlogiston.
- **George Starkey / Eirenaeus Philalethes (The Practitioner)**: Handling colonial origins and pseudonymous influence.

## 4. Measuring Progress
Our success metric will be the degree to which we can answer questions like:
- *"How did Becher's chemical claims support the Austrian court's mercantilist policies?"*
- *"What is the material provenance of the Antimony mentioned in Newton's manuscripts?"*
