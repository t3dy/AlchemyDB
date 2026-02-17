# AlchemyDB: Design & Style Guide

This guide defines the visual and functional standards for the AlchemyDB project, ensuring a premium "Digital Humanities" experience.

## Visual Identity
- **Theme**: "Arcane Modern" - A blend of historical manuscript aesthetics (parchment, ink-stroke accents) with high-tech data science visualization (vibrant gradients, glassmorphism).
- **Primary Colors**: 
    - `#1A1A1A` (Deep Obsidian / Ink)
    - `#F4EBD0` (Parchment White)
    - `#D4AF37` (Alchemical Gold)
- **Typography**: 
    - Headings: Serif (e.g., "Playfair Display" or "Crimson Text") for historical weight.
    - Body: Sans-Serif (e.g., "Inter" or "Outfit") for readability.

## Entity Behavior & Logic
- **The "Traceability" Rule**: Every UI element representing an entity (Alchemist, Substance) must show a hover-card or tooltip with its "Evidence Count" (how many times it appears in the corpus).
- **Link Integrity**: Document IDs and Entity IDs must be persistent. Clicking an entity in a list should navigate to a "Deep Dive" view showing all occurrences.
- **Verification Loop**: Entities extracted by LLMs must be flagged as `[PROVISIONAL]` until marked as `[VERIFIED]` by the user.

## Agent Instructions (for Antigravity)
- **Prioritize Context**: When writing code for entity extraction, always prioritize capturing the *sentence around the entity* as context.
- **Avoid Generic Lists**: Instead of "List of Alchemists", use "Registry of Practitioners" and group them by "Tradition" or "Century".
- **Visual Feedback First**: Before implementing deep backend logic, create a "mock data" visualization to show the user how the results will look.

## Dashboard Principles
- **The "Library Table"**: A central view of all ingested documents with status indicators for (Ingested, Extracted, Indexed).
- **The "Specimen Drawer"**: A sidebar or modal that shows the "latest discoveries" (new entities found during extraction).
