# AlchemyDB: 20-Phase Project Roadmap (Revised)

## Phase 1-4: Foundation [x]
- [x] Project Structure & Config <!-- id: 1 -->
- [x] SQLite Schema v1 <!-- id: 7 -->
- [x] File Inventory Ingestion (Metadata) <!-- id: 10 -->

## Phase 5: Visibility Sprint - "The Specimen Drawer" [x]
- [x] Align SQL Schema with `domain_ontology.md` (Alchemists, Lexicon slots) <!-- id: 11 -->
- [x] Build "Discovery Dashboard" (Vite + React) <!-- id: 12 -->
- [x] Robust Export Script (SQLite -> JSON) <!-- id: 13 -->
- [x] Connect Dashboard to `exports/docs.json` <!-- id: 14 -->

## Phase 6: Interactive Extraction Loop [x]
- [x] Set up `PyMuPDF` for text extraction <!-- id: 15 -->
- [x] Implement chunking & storage for text <!-- id: 16 -->
- [x] Create initial specimens (Agentic Mining) <!-- id: 17 -->
- [x] Update Dashboard "Specimen Drawer" to show Candidates <!-- id: 18 -->

## Phase 7: Project Log & Manual (Dashboard v1.1) [/]
- [ ] Draft "History & Learning Journey" (V1) <!-- id: 20 -->
- [ ] Draft "Narrative System Instructions" <!-- id: 21 -->
- [ ] Implement Routing in Dashboard (Docs Page) <!-- id: 22 -->
- [ ] Create interactive project log UI <!-- id: 23 -->

## Phase 8: Hardening & Remote Sync [ ]
- [ ] Finalize local DB state and push to GitHub <!-- id: 24 -->
- [ ] Setup Relational Viewer instructions (DBeaver/DB Browser) <!-- id: 25 -->

## Phase 9: Strategic Mining & Vocabulary Expansion [x]
- [x] Broad-scan mining for 'Top 500' Alchemical Terms <!-- id: 26 -->
- [x] Categorize findings (Substances, Allegories, Authors, etc.) <!-- id: 27 -->
- [x] Draft 'Extraction Strategy' report <!-- id: 28 -->
- [x] Update Lexicon with Top 500 Candidates <!-- id: 29 -->
- [x] Push to GitHub (t3dy/AlchemyDB) <!-- id: 30 -->

## Phase 10: The Great Harvest [/]
- [ ] Implement Broad Mining Script (Lexicon Matcher) <!-- id: 31 -->
- [ ] Populate `entity_mentions` across 205 documents <!-- id: 32 -->
- [ ] Implement "Specimen Spotlight" in Dashboard <!-- id: 33 -->
- [ ] Export "Mentions Heatmap" for relational study <!-- id: 34 -->

## Phase 11: Lexicon & Taxonomy Browser [x]
- [x] Add 'Lexicon' tab to Dashboard <!-- id: 35 -->
- [x] Grouped view by Category (Substances vs. Paradoxes) <!-- id: 36 -->
- [x] Integrate Mention Frequency <!-- id: 37 -->

## Phase 12: Biographies & Personnel Profiles [x]
- [x] Identify top 10 alchemists by mention frequency <!-- id: 38 -->
- [x] Implement `biography` data structure in Database <!-- id: 39 -->
- [x] Generate "Seed Biographies" for top figures (Paracelsus, Jabir, etc.) <!-- id: 40 -->
- [x] Implement Biography Detail View in Dashboard <!-- id: 41 -->
- [x] Link mentions to specific biographical milestones <!-- id: 42 -->

## Phase 13: Textual Summaries & Critical Apparatus [/]
- [/] Draft 'Textual Summaries' strategy report <!-- id: 43 -->
- [ ] Implement `textual_summaries` table <!-- id: 44 -->
- [ ] Generate analysis for top 5 manuscripts <!-- id: 45 -->
- [ ] Integrate Summaries into Dashboard (Project Log) <!-- id: 46 -->

## Phase 14: Historiography & Scholar Dictionary [ ]
- [ ] Identify 'Who's Who' of Alchemical Scholars <!-- id: 47 -->
- [ ] Add Scholar category to Lexicon <!-- id: 48 -->
- [ ] Populate Scholar biographies (Kahn, Principe, etc.) <!-- id: 49 -->
- [ ] Create 'Historiography' view in Lexicon <!-- id: 50 -->
- [ ] Pushing final Phase 14 sync to GitHub <!-- id: 51 -->

## Phase 15: Feedback Integration & Publishing
- [x] Create migration `0005_schema_fixes.sql` <!-- id: 52 -->
- [x] Run migration and verify schema <!-- id: 53 -->
- [x] Create `scripts/generate_descriptions.py` <!-- id: 54 -->
- [x] Update `scripts/populate_scholars.py` with New Historiography list <!-- id: 55 -->
- [x] Update `scripts/export_data.py` with new fields <!-- id: 56 -->
- [ ] Fix dashboard build (JSON paths) <!-- id: 57 -->
- [ ] Create "Infrastructure Analysis & Roadmap" report <!-- id: 68 -->
- [ ] Create "Strategic Improvement Plan" report <!-- id: 69 -->
- [ ] Update `ProjectLog.jsx` with feedback reports <!-- id: 70 -->

## Phase 16: Socio-Economic Metadata (The Business of Alchemy)
- [ ] Create migration `0006_socio_economic_schema.sql` (knowledge_type, roles, patronage) <!-- id: 71 -->
- [ ] Create `scripts/populate_rich_profiles.py` from user feedback <!-- id: 72 -->
- [ ] Update `scripts/export_data.py` for new dimensions <!-- id: 73 -->
- [ ] Update `WhosWhoView.jsx` to show "Knowledge in Action" panels <!-- id: 74 -->

## Phase 18: Chemical Synthesis & Dictionary Refinement
    - [x] Create Dictionary Style Guide and Template
- [x] Create 5 Python scripts for chemical extraction:
    - [x] `substance_miner.py`
    - [x] `equipment_miner.py`
    - [x] `process_mapper.py`
    - [x] `llm_scholarly_reader.py`
    - [x] `lexicon_synthesizer.py`
- [x] Extract chemical substances, equipment, and processes from scholarly texts.
- [x] Generate synthesized "Dual-History" entries for key terms.
- [x] Update Project Log and Dashboard with new rich entries.
- [x] Create meta-critique on DH and Prompt Engineering.

## Phase 17: Dashboard Storytelling (Political Economy Mode)
- [ ] Implement "Political Economy Mode" toggle in Library/Discovery <!-- id: 75 -->
- [ ] Create Patronage Graph visualization <!-- id: 76 -->
- [ ] Final GitHub Pages deployment <!-- id: 77 -->

... (rest of phases)
