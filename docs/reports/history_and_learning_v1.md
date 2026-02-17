# V1: History & the Learning Journey

## The Genesis: From Folders to Coordinates
AlchemyDB began as a collection of 205 orphaned PDFs. Our first mission was simple: don't lose the files. We built an inventory script to hash, deduplicate, and catalog every document. But we soon realized that a list of filenames is a library without a librarian.

## The Cognitive Pivot: The Evidence Trail
The most significant leap in our design logic was the rejection of "Extract and Forget." In typical AI projects, an LLM extracts a name and you save it. In **Digital Humanities**, a name without a source is a hallucination.
- **The Design**: We pivoted to a model where the **Document Chunk** is the primary unit of truth. 
- **The Logic**: If we can't point to the exact paragraph where a practitioner appears, they don't exist in our Registry. This is the "Evidence Trail."

## Aesthetic Logic: The "Arcane Modern" Theme
We wanted the interface to reflect the tension between an 18th-century laboratory and a 21st-century data center.
- **Parchment and Glass**: The use of semitransparent glass panels over dark backgrounds evokes the feeling of looking at a specimen through a microscope.
- **The Golden Mean**: Alchemical gold (#D4AF37) is used exclusively for actionable items and status badges, signaling that the data has been "transmuted" into information.

## What We Learned
1. **Documents are Coordinate Systems**: A person doesn't just "exist" in a book; they exist at a specific page and paragraph. 
2. **Ambiguity is a Feature**: We embrace "Candidates." We don't need the system to be 100% correct immediately; we need it to be 100% transparent about what it *thinks* it found so the user can verify it.
