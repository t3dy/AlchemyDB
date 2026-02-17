# Task: Library, Who's Who, and GitHub Publishing

## Phase 13: Library & Data Harvesting
- [ ] Create migration `0005_schema_fixes.sql` (add columns to `documents`, `lexicon`, `entities`) <!-- id: 52 -->
- [ ] Run migration and verify schema <!-- id: 53 -->
- [ ] Create `scripts/generate_descriptions.py` to populate `documents.description` <!-- id: 54 -->
- [ ] Fix and run `scripts/populate_scholars.py` <!-- id: 55 -->
- [ ] Update `scripts/export_data.py` with new fields <!-- id: 56 -->
- [ ] Run export and verify JSON outputs <!-- id: 57 -->

## Phase 14: Frontend - Library & Who's Who
- [ ] Create `dashboard/src/LibraryView.jsx` <!-- id: 58 -->
- [ ] Create `dashboard/src/WhosWhoView.jsx` <!-- id: 59 -->
- [ ] Implement `dashboard/src/GuideOverlay.jsx` for onscreen instructions <!-- id: 60 -->
- [ ] Update `dashboard/src/App.jsx` with routes and navigation <!-- id: 61 -->
- [ ] Style new components in `dashboard/src/index.css` <!-- id: 62 -->

## Phase 15: Deployment & GitHub Sync
- [ ] Configure `dashboard/vite.config.js` for GitHub Pages <!-- id: 63 -->
- [ ] Create `scripts/deploy_dashboard.py` (build and push to gh-pages) <!-- id: 64 -->
- [ ] Verify README link to dashboard <!-- id: 65 -->
- [ ] Add final report to `dashboard/src/ProjectLog.jsx` <!-- id: 66 -->
- [ ] Final sync to GitHub main branch <!-- id: 67 -->
