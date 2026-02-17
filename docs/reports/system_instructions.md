# Narrative System: Instructions for the History Detective

Welcome to the AlchemyDB Research Suite. As a user or tester, your goal is not just to "search" but to "curate."

## 1. The Discovery Dashboard
The dashboard is split into two primary zones:
- **The Library Table**: This is your bird's-eye view. Use this to track ingestion status and file sizes. If a document is listed as "Ingested," its text is accessible to the miner.
- **The Specimen Drawer**: This is your active research desk. Every card in this drawer represents a "Probability."

## 2. Working with Candidates (The Specimen Drawer)
When you see a card in the Specimen Drawer, follow this workflow:
- **Identify**: Look at the name and tradition.
- **Verify**: Read the **Direct Quote**. Does the text actually support the claim that this person is an alchemist? 
- **Trace**: Check the `document_id`. You can find the full context of this quote in the source PDF (mapping tool coming soon).

## 3. Storytelling with the Data
To tell a story about alchemy, look for **Cross-Pollination**:
- **Lineage**: Find an author (e.g., Agrippa) and look for citations of earlier thinkers (e.g., Masha'allah).
- **Conflict**: Look for terms in the **Lexicon** that are defined differently across traditions.
- **The Invisible Hand**: Watch for "Historical Figures" who appear in alchemical texts but are rarely credited in mainstream history—these are the "secret protagonists" of your study.

## 4. Testing Protocols
As we build the next features, keep these questions in mind:
- **Precision**: Is the miner finding real names or just Latin fragments?
- **Utility**: Does the Specimen Drawer help you find something you *didn't* already know?
- **Flow**: Is the transition from "Document Metadata" to "Entity Evidence" intuitive?
