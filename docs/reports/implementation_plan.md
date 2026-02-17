# Implementation Plan - Phase 10: The Great Harvest

This phase initiates a broad-scale mining operation across the entire PDF corpus (205 documents) using the 500-term seed lexicon.

## User Review Required

> [!NOTE]
> This process will generate a large number of "Candidates" in the Specimen Drawer. I will implement a basic frequency-based relevance score to ensure the most prominent findings appear first.

## Proposed Changes

### 1. Mining Engine
#### [NEW] `scripts/mine_broad.py`
- Load all `term` strings from the `lexicon` table.
- Iterate through `document_chunks`.
- Perform case-insensitive keyword matching.
- For every match, check if the entity exists in `entities` (create if not).
- Insert a record in `entity_mentions` with the `quote` (context around the match) and `confidence_score`.

### 2. CLI Integration
#### [MODIFY] `scripts/manage.py`
- Add the `mine` command to trigger the broad mining script.

### 3. Visibility (Dashboard)
#### [MODIFY] `scripts/export_data.py`
- Update to ensure the `candidates.json` export handles the increased volume and performs basic sorting by confidence/frequency.

## Verification Plan

### Automated Tests
- `python -m scripts.manage mine` -> Verify that `entity_mentions` table count increases significantly.
- `python -m scripts.manage export` -> Ensure JSON files are valid and contain matching specimens.

### Manual Verification
- Refresh the dashboard and browse the **Specimen Drawer** to verify that candidates from different documents (not just 202 and 205) are appearing with correct quotes.
