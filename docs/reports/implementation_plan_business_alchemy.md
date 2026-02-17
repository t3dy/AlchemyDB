# Plan: The Business of Alchemy Integration

This plan details the expansion of AlchemyDB to model alchemy as a multi-dimensional relational system (symbolic, material, political, economic).

## 1. Governance & Analysis (Phase 15)
- **Report 1: Infrastructure Analysis & Roadmap**
    - Contrast current "Symbolic/Thematic" focus with the "Socio-Economic" requirements.
    - Identify gaps in entity resolution and social capital tracking.
- **Report 2: Strategic Improvement Plan**
    - Actionable steps for Phase 16 and 17.
    - Design shift from "Dictionary = Definition" to "Dictionary = Actor + Theory + Patronage + Practice."

## 2. Relational Expansion (Phase 16)
- **Schema Update (`0006_socio_economic_schema.sql`)**:
    - `entities`: Add `knowledge_type`, `social_role`, `patronage_id`.
    - `lexicon`: Add `substance_nature` (alkali, acid, etc.) and `theoretical_lineage`.
    - `identity_aliases`: New table to link Starkey <-> Philalethes.
    - `patronage_networks`: New table for courts and princes.
- **Data Harvesting**:
    - Populate rich profiles for Becher, Smith, Stahl, Leibniz, etc.
    - Implement alias resolution logic in the mining pipeline.

## 3. Storytelling & Dashboard (Phase 17)
- **Multi-Mode Dictionary**:
    - Toggle between "Symbolic Mode" (Albedo, Rubedo) and "Political-Economic Mode" (Fiscal Reform, Court Projectors).
- **Relational Visualizer**:
    - Visualizing "Afterlives" of texts via republication graphs.
    - Mapping experimental substance flows (Antimony -> Newton).

## 4. Final Deployment
- Ensure all static assets are bundled for GitHub Pages.
- Update README with the final project synthesis.
