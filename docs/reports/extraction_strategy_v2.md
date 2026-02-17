# Extraction Strategy v2: Semantic Mining & Evidence Anchoring

This report outlines the methodology for identifying and extracting alchemical entities from the PDF corpus (205 documents).

## 1. The Methodological Shift
We are moving from a **Search-Based** approach to an **Extraction-Based** approach.
- **Search (v1)**: "Find the word 'Paracelsus' and show me the line."
- **Extraction (v2)**: "Identify any practitioners mentioned in this chunk, explain their tradition, and anchor the finding with a verbatim quote."

## 2. The 500-Term Seed Lexicon
To guide the LLM (and my own agentic mining), we are establishing a "Seed Lexicon" of 500 terms. This lexicon acts as a **Heuristic Filter**:
1. **Practitioners**: 100 figures from Zosimos to Paracelsus to 20th-century scholars (e.g., Jung, Newman).
2. **Texts**: 100 influential works (e.g., *Emerald Tablet*, *Mutus Liber*, *Theatrum Chemicum*).
3. **Substances**: 100 materials with both physical and allegorical meanings (e.g., *Aqua Regia*, *Cinnabar*, *Philosophical Mercury*).
4. **Allegories**: 100 symbolic motifs (e.g., *The Green Lion*, *The Ouroboros*, *The Alchemical Marriage*).
5. **Apparatus**: 100 tools and processes (e.g., *Athanor*, *Cucurbit*, *Circulation*).

## 3. Evidence Anchoring (The Golden Rule)
No entity is entered into the **Registry** unless it has an **Anchor**.
- **The Anchor**: A unique ID pointing to a `document_chunks` row and a verbatim quote.
- **Confidence Scoring**: 
    - **High (1.0)**: Direct name mention in a clear context.
    - **Medium (0.7)**: Allusive mention or synonym.
    - **Low (0.3)**: Speculative connection (Candidate status).

## 4. Extraction Pipeline
1. **Chunk Scan**: Scan the `document_chunks` table for keywords from the Seed Lexicon.
2. **Agentic Review**: I (Antigravity) parse the surrounding context to verify the entity's role.
3. **Database Insertion**: Update `entities`, `lexicon`, and `entity_mentions` with the findings.
4. **Dashboard Visualization**: New "Specimens" appear in the drawer for user curation.
