# Implementation Plan - Phase 12: Biographies & Personnel Profiles

This phase focuses on transforming our "Candidates" into structured biographical profiles, creating the "Biographies" component of the Multimedia Dictionary.

## Proposed Changes

### 1. Database Schema Update
#### [NEW] `migrations/0004_biographies.sql`
- Create a `biographies` table:
    - `entity_id` (Reference to `entities.id`)
    - `full_name`
    - `lifespan` (e.g., 1493-1541)
    - `tradition` (e.g., Paracelsianism, Iatrochemistry)
    - `narrative_summary` (Markdown text)
    - `milestones` (JSON array of key dates/events)
    - `primary_texts` (JSON array of major works)

### 2. Personnel Profiling (Agentic Synthesis)
- **The Synthesis Loop**: I will sample the `entity_mentions` for top figures (starting with Paracelsus).
- **Strategy**: Cross-reference the mentions with internal historical knowledge to draft a comprehensive `narrative_summary` that highlights how the practitioner is discussed *within this specific library*.

### 3. Dashboard Integration
#### [MODIFY] `dashboard/src/LexiconView.jsx`
- Add an "Open Biography" button to cards that have a matching biography entry.
#### [NEW] `dashboard/src/BiographyDetail.jsx`
- Create a detailed profile view including:
    - Interactive Timeline (from milestones).
    - Evidence Gallery (randomly sampled quotes from `entity_mentions`).
    - Geographic Context (if detectable).

## Verification Plan

### Automated
- Run migrations and verify schema.
- Export `atlas.json` (as `biographies.json`) and verify JSON integrity.

### Manual
- Browse **Paracelsus** in the Lexicon and open his biography.
- Verify that the "Evidence Gallery" correctly pulls quotes from the actual `entity_mentions` table.
