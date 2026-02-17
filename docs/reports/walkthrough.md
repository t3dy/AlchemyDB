# Walkthrough - Visibility Sprint

This sprint has successfully established the foundaton for data visibility and domain-aligned entity tracking in AlchemyDB.

## 1. Domain-Aligned Schema
I updated the database with `migrations/0002_domain_entities.sql`, introducing:
- `entities`: For Alchemists and historical figures.
- `lexicon`: For symbolic and technical terminology.
- `entity_mentions`: To provide the "Evidence Trail" for every extraction.

## 2. Document Ingestion
I ran the updated ingestion script as a Python module:
```bash
python -m scripts.manage ingest
```
# Walkthrough: AlchemyDB - Chemical Synthesis & Dictionary Refinement

This walkthrough documents the successful implementation of the **Chemical Synthesis Roadmap**, which transitions AlchemyDB from a simple glossary to a rich Digital Humanities research engine. We have integrated advanced mining scripts and a "Dual-History" model to bridge alchemical theory with modern chemistry.

## 1. Chemical Synthesis Roadmap

We implemented a suite of 5 Python scripts to automate the extraction and synthesis of chemical knowledge from the scholarly corpus:

- [substance_miner.py](file:///c:/AlchemyDB/scripts/substance_miner.py): Extracts 1,600+ mentions of minerals and chemicals.
- [equipment_miner.py](file:///c:/AlchemyDB/scripts/equipment_miner.py): Extracts 1,200+ mentions of laboratory apparatus.
- [process_mapper.py](file:///c:/AlchemyDB/scripts/process_mapper.py): Maps 1,900+ alchemical processes to modern chemical analogs.
- [llm_scholarly_reader.py](file:///c:/AlchemyDB/scripts/llm_scholarly_reader.py): Aggregates context for LLM-assisted synthesis.
- [lexicon_synthesizer.py](file:///c:/AlchemyDB/scripts/lexicon_synthesizer.py): Populates the database with rich "Dual-History" profiles.

## 2. The "Dual-History" Model

We have refined key dictionary entries (e.g., **Vitriol**, **Antimony**, **Alembic**) to follow a multi-valent template:
1. **Core Definition**: Functional explanation.
2. **Alchemical Profile**: Theoretical and symbolic roles (e.g., the "Green Lion").
3. **Modern Chemical Profile**: Modern identity and reaction logic (e.g., oxidation).
4. **Synthesis**: Relational analysis bridging the two histories.

## 3. Analytical Synthesis & Reports

We produced three significant reports documenting our methodology and project trajectory:
- [Analytical Study: Laboratories of Art](file:///C:/Users/PC/.gemini/antigravity/brain/46767a98-75f1-47da-8677-1eb0212fcee/analytical_study_laboratories_of_art.md)
- [Database Improvement Roadmap](file:///C:/Users/PC/.gemini/antigravity/brain/46767a98-75f1-47da-8677-1eb0212fcee/database_improvement_roadmap.md)
- [DH & AI Engineering Critique](file:///C:/Users/PC/.gemini/antigravity/brain/46767a98-75f1-47da-8677-1eb0212fcee/dh_ai_engineering_critique.md)

---
- **Features**:
    - **Library Table**: View all ingested documents, their sizes, and status.
    - **Filterable Interface**: Search through the 205 documents instantly.
    - **Specimen Drawer (Preview)**: Placeholder for real-time entity discoveries during Phase 6.

### How to Access the Dashboard
The dev server is currently running locally. You can view it by navigating to:
**[http://localhost:5173/](http://localhost:5173/)**

## 8. The Alchemical Lexicon Browser (Phase 11)
Aligned with the vision of a "Beautiful Multimedia Dictionary," I've implemented the first version of the Lexicon interface:
- **Lexicon Tab**: A new primary navigation tab in the dashboard.
- **500-Term Dictionary**: Browse alchemists, substances, and texts with their definitions.
- **Frequency Analysis**: Integrated the results of the Broad Mining pass. You can see how many times each term is mentioned across your 205-PDF library.
- **Evidence Ready**: Each term is prepped for deeper study, linking directly to the over 16,000 mentions found in the corpus.

## 9. GitHub & Project Status
The entire project is now live on GitHub and fully synchronized:
- **Repository**: [https://github.com/t3dy/AlchemyDB](https://github.com/t3dy/AlchemyDB)
- **Latest Commit**: Implemented Multimedia Dictionary Lexicon and frequency analysis.
