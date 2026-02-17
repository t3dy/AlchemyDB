# Implementation Plan - Phase 9: Strategic Mining & Vocabulary Expansion

This phase focuses on defining the "Dictionary" that will guide all future extraction passes. We aim to identify 500 core entities across multiple categories to create a comprehensive alchemical taxonomy.

## User Review Required

> [!IMPORTANT]
> I will populate the `lexicon` table with these 500 terms as "Candidates." You will be able to browse them in the dashboard and suggest adjustments to their definitions or traditions.

## Proposed Changes

### 1. Data Mining & Categorization
- **Agentic Mining**: I will use my internal knowledge of the alchemical tradition, cross-referenced with your specific PDF corpus (205 docs), to identify:
    - 100 Alchemists/Scholars
    - 100 Substances & Chemical Meanings
    - 100 Texts & Manuscripts
    - 100 Allegories & Theories
    - 100 Equipment & Processes
- **Storage**: Populate the `lexicon` table with these terms, definitions, and categories.

### 2. Extraction Strategy Report [NEW]
- **Document**: Create `extraction_strategy_v2.md` outlining the move from "Keyword Search" to "Semantic Extraction with Evidence."
- **Methods**: Define the "Confidence Scoring" logic for automated mining.

### 3. Dashboard Integration
#### [MODIFY] `dashboard/src/data/lexicon.json` [NEW]
- Export the 500 terms for the frontend.
#### [MODIFY] `dashboard/src/App.jsx`
- Add a "Lexicon Browser" tab to the dashboard.

## Verification Plan

### Automated
- `python -m scripts.manage export` -> Verify `lexicon.json` contains the full 500 items.
- SQLite query to check frequency of mentions for top terms.

### Manual
- Navigate to the "Lexicon" tab in the dashboard and verify the categorization is intuitive.
