# Report: PDF Mining Methodology & Tools

This report outlines the technical strategy and "skills" used to transform the 205 raw PDFs of the AlchemyDB corpus into structured database entries and narrative content.

## 1. The Mining Pipeline
Our methodology follows a tiered extraction approach:

### Tier 1: Structural Extraction
- **Tools**: `PyMuPDF` (fitz), `pdfplumber`.
- **Method**: Extracting raw text flows while preserving page headers and numbering. Metadata such as Author and Year are harvested from XMP metadata where available, or inferred from filename heuristics.

### Tier 2: Named Entity Recognition (NER) & Resoluton
- **Tools**: `spaCy` (en_core_web_md), custom regex heuristics.
- **Skills**:
    - **Entity Distillation**: Converting raw mentions (e.g., "J.J. Becher") into unique database IDs.
    - **Alias Mapping**: Handling pseudonyms (e.g., Starkey <-> Philalethes) using a relational lookup table.
    - **Confidence Scoring**: Assigning scores based on mention frequency and proximity to known alchemical terminology.

### Tier 3: Semantic Harvesting & Synthesis
- **Tools**: Python-based summarization heuristics, thematic keyword anchors.
- **Method**: 
    - Focusing on "Chunk 0" and "Chunk 1" to capture introductory arguments and copyright-free substantive text.
    - Filtering out boilerplate (e.g., "For private study only") using negative regex patterns.
    - Generating **Thematic Summaries**: 200-character snapshots that define the "why" of a text.

## 2. Generating Biographical Sketches
To create the "Who's Who" entries, we use a hybrid automated/curated workflow:
1. **Aggregated Mention Analysis**: Identifying every page where a scholar/alchemist is mentioned.
2. **Contextual Proximity**: Extracting 500-character windows around names to find "predicate" phrases (e.g., "...was a court projector involved in...").
3. **Automated Synthesis**: Collating milestones and primary works based on bibliographical patterns in the text segments.

## 4. Improving Database Entries
- **Feedback Loop**: Using scholarly reviews (e.g., Tribe on Smith, Nauert on Newman) to refine entity scores.
- **Dimensional Modeling**: Adding `knowledge_type` and `social_role` metadata to move beyond keyword matching to **Socio-Economic modeling**.

## 5. Skills Reference
Planned Python "skills" for the next iteration:
- `ner_resolver.py`: Unified entity resolution and alias management.
- `biography_synthesizer.py`: Automated markdown generation for scholar dossiers.
- `patronage_mapper.py`: Identifying links between entities and court-themed keywords.
