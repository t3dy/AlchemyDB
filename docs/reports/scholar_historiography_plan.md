# Plan: Alchemical Historiography & Scholar Dictionary

This plan outlines the "Who's Who" of alchemical scholarship to be integrated into the AlchemyDB Lexicon.

## Scholar Identification
We will populate the dictionary with two tiers of scholars:

### The "New Historiography" Core
These scholars represent the rigorous, evidence-based study of alchemy in the tradition of Newman and Principe.
- **William R. Newman**: Specialist in Geber, Boyle, and the experimental tradition.
- **Lawrence M. Principe**: Focus on "Chymistry" and the laboratory reality of alchemy.
- **Didier Kahn**: Expert in Paracelsianism and early modern chymistry.
- **Barbara Obrist**: Specialist in alchemical iconography and medieval cosmology.
- **Peter Forshaw**: Expert in Dee, Khunrath, and the intersection of alchemy and magic.
- **Allen Debus**: History of the Paracelsian tradition and science.
- **Tara Nummedal**: Expert on "Alchemy and Authority" and the role of practitioners.
- **Anke Timmerman**: Specialist in alchemical manuscripts and verse.
- **Pamela Smith**: Focus on "The Body of the Artisan" and material knowledge.

### Thematic & Dictionary Mining
A primary objective is to mine the books authored by these scholars within our library.
- **Dictionary Entries**: Extract precise terminology used in their analyses to define alchemical concepts.
- **Thematic Harvesting**: Map the core arguments of these scholars to the primary texts they discuss.

## Implementation Steps

### 1. Lexicon Categorization
- Add a `[Scholar]` tag to these entities in the `lexicon` table.
- Distinguish between "Practitioner" (historical alchemist) and "Scholar" (historiographer) in the `entity_type` field.

### 2. Scholarly Biographies
- Generate structured profiles for these scholars, focusing on their contribution to the field rather than laboratory milestones.
- Link them to the **Primary Texts** they edited or analyzed (e.g., linking Didier Kahn to Paracelsus's *Astronomia Magna*).

### 3. Historiography View
- Add a "Scholars" filter to the Lexicon Browser.
- Create a special "Historiographical Lens" section in the Biography view that explains *why* this scholar is important to our library.

## Verification
- Verify that filtering by "Scholar" in the Dashboard shows only modern researchers.
- Ensure the "Biographies" for scholars correctly list their academic works.
