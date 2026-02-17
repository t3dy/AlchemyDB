# AlchemyDB

A local-first digital humanities archive for alchemical and esoteric studies.

## Architectural Outline

- **Corpus Layer**: `pdf/` (Immutable corpus of PDF documents)
- **Relational Database**: SQLite (Metadata and relations)
- **Extraction Pipeline**: `scripts/` (Python scripts for data extraction)
- **Export Layer**: `exports/` (Generated JSON data)
- **Dashboard**: [Access Local Dashboard](http://localhost:5173/) (Requires `npm run dev` in the `dashboard` directory)

## Development Philosophy

- **Reproducibility**: All data generation should be reproducible from the source corpus and scripts.
- **Provenance**: clear lineage of data.
- **Run-based Extraction**: Data is regenerated, not manually edited.

## Note

The `pdf/` directory is treated as a read-only immutable corpus.
