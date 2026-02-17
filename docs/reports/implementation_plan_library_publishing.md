# Plan: Library, Who's Who, and GitHub Publishing

This plan covers the creation of the Library and Who's Who views, along with the necessary data harvesting and deployment steps.

## 1. Database & Data Harvesting
- **Migration**: Update `documents`, `lexicon`, and `entities` tables.
    - `documents`: Add `description` column.
    - `lexicon`: Add `category` column (to replace the bracketed prefix).
    - `entities`: Add `confidence` column.
- **Script (Mining)**: Generate short descriptions for all 205 PDFs using `document_chunks`.
- **Script (Scholars)**: Fix and run `populate_scholars.py` to add the "New Historiography" list.
- **Export**: Update `export_data.py` to include new fields in `docs.json`, `lexicon.json`, and `biographies.json`.

## 2. Dashboard Enhancements
- **Library Page**: A dedicated view for browsing the PDF collection with descriptions and metadata.
- **Who's Who Page**: A curated list of scholars with their profiles, filtered from the biographies table.
- **Onscreen Instructions**: A toggleable or persistent "Guide" component on each page explaining the data source and usage.
- **Navigation**: Update the header with links to "LIBRARY" and "WHO'S WHO".

## 3. GitHub Publishing
- **Configuration**: Set `base` in `vite.config.js`.
- **Build & Deploy**: Create a script to build the project and push the `dist` folder to GitHub Pages.
- **Data Persistence**: Ensure the `exports` directory (JSON data) is included in the build so the site works online.

## 4. Documentation & Logging
- **Project Log**: Add a comprehensive log of these changes.
- **README**: Verify and update the dashboard link.
- **Walkthrough**: Update with the new features and screenshots.
