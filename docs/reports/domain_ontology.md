# AlchemyDB: Domain Ontology

This document defines the core concepts and entities within the AlchemyDB project, bridging the gap between raw data science and Digital Humanities research.

## Core Entities

### 1. Document
- **Definition**: A primary source (PDF, manuscript, record) or secondary study.
- **Attributes**: Title, Author, Year, Type (Manuscript, Print, Scholarly), Source (Path/URL).
- **Role**: The foundational unit of evidence.

### 2. Alchemist (Entity: Person)
- **Definition**: A historical figure, practitioner, or author involved in alchemical work.
- **Attributes**: Name, Pseudonyms, Active Dates, Traditions (e.g., Paracelsian, Hermetic).
- **Role**: Primary actor in the historical narrative.

### 3. Lexicon / Dictionary Entry
- **Definition**: Specialized terminology, symbols, or substances found within the texts.
- **Attributes**: Term, Meaning(s), Symbol (if applicable), Synonyms.
- **Role**: Decoding the "Gargon" and symbolic language of alchemy.

### 4. Alchemists List (Entity: Collection)
- **Definition**: A curated or extracted list of practitioners, often found within a specific document or across a tradition.
- **Role**: Identifying networks of relationship and influence.

## Data Science Principles in Context

- **Source Traceability**: Every entity extraction must link back to the exact passage (document + page/chunk) in the corpus.
- **Iterative Curation**: The system initially mines "candidates" using LLMs, which are then promoted to "verified" status by the human researcher (Alchemist/User).
- **Semantic Relationships**: Focus not just on tags, but on the *nature* of the link (e.g., "Alchemist A *cited* Alchemist B").

## Visibility & Validation
- **Dashboard Priority**: The dashboard must show the "Source-to-Entity" path clearly so the user can verify LLM extractions against the original text immediately.
