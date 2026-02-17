# AlchemyDB: LLM Mining Strategy

This document outlines the approach for extracting structured historical data (Entities, Lists, Lexicon) from the PDF corpus using LLMs and Python.

## The "Alchemical Extraction" Pipeline

### 1. The Multi-Pass Extractor
Instead of one large prompt, we use specific specialized passes:
- **Pass 1: Entity Identification**: "Find all names of people and their associated traditions."
- **Pass 2: Relationship Extraction**: "For each person identified, find any mention of their masters, students, or colleagues."
- **Pass 3: Substance & Symbol Decoding**: "Identify alchemical substances and symbols mentioned in this section."

### 2. Context Window Management
- **Overlap Strategy**: We process documents in chunks with a 150-token overlap to ensure entities mentioned across page boundaries (e.g., "Albertus... [page break] ...Magnus") are captured correctly.
- **Reference Resolution**: When a pronoun appears ("He wrote..."), we include the preceding paragraph in the prompt context to help the LLM resolve the reference to the last named Alchemist.

### 3. Validation & The "Evidence" Trail
- **Strict JSON Output**: All LLM requests enforce a standard JSON schema for consistency.
- **Source Anchors**: The LLM must return the *exact quote* from the text where it found the entity. This quote is stored in the `entity_mentions` table.
- **Self-Correction Loop**: We can use a second LLM pass (the "Critic") to check if the extracted quotes actually support the extracted entity data.

## Strategies for "Alchemists Lists"
Rather than asking for a "list", we ask the LLM to:
1. "Audit the text for mentions of practitioners."
2. "Compile a registry of these individuals with supporting evidence."
3. "Assign a confidence score based on the clarity of the mention."

## Visibility Integration
The [Discovery Dashboard](file:///C:/Users/PC/.gemini/antigravity/brain/46767a98-75f1-47da-8677-1eb0212fc8ee/implementation_plan.md) will show these extractions as "Candidates" in real-time as the scripts run, allowing you to watch the "Specimen Drawer" fill up.
