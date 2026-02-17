# Implementation Plan: Phase 18 - Chemical Synthesis

## Objective
To refine the AlchemyDB dictionary by implementing the "Dual-History Model" for substances, equipment, and processes. This involves distinguishing historical alchemical theory from modern chemical understanding and automating the extraction of this data from key scholarly texts.

## Proposed Changes

### 1. Database Schema
- No immediate schema changes required (Phase 16 added necessary metadata fields like `knowledge_type`). We will use the `lexicon` table's `definition` field to store the structured rich profiles.

### 2. Automation Strategy: The 5-Script Suite
We will develop the following Python utilities to assist in this synthesis:

1.  **`substance_miner.py`**: Extracts mentions of chemicals (Vitriol, Antimony, Nitre) from PDFs and cross-references them with IUPAC names.
2.  **`equipment_miner.py`**: Identifies laboratory apparatus (Alembic, Athannor, Retort) and their functional roles across different traditions.
3.  **`process_mapper.py`**: Maps historical processes (Calcination, Sublimation) to modern chemical analogs (Oxidation, Phase Change).
4.  **`llm_scholarly_reader.py`**: A specialized LLM script to "read" specific chapters of Principe and Newman to extract "Chemical Identifications" (e.g., "Newman identifies Philalethes' 'Green Lion' as...")
5.  **`lexicon_synthesizer.py`**: Compiles the extracted data into the "Rich Profile" format defined in the style guide and updates the database.

### 3. LLM Reading Methods
- **Target Texts**: 
    - Lawrence Principe, *The Secrets of Alchemy* / *The Aspiring Adept*.
    - William R. Newman, *Gehennical Fire* / *Promethean Ambitions*.
    - Barbara Obrist (text documents on alchemy and imagery).
- **Prompt Logic**: 
    - "Identify every instance where the author provides a modern chemical identification for an alchemical substance."
    - "Extract the experimental evidence used for this identification (e.g., color changes, weight measurements)."

## Verification Plan

### Automated Tests
- Verify that entries for "Vitriol" exist in both `(alchemical)` and `(modern chemistry)` forms in the exported JSON.
- Run build and check if the dashboard displays the rich profile sections correctly.

### Manual Verification
- Review the synthesized summaries for accuracy against the source material (Principe/Newman).
