# AlchemyDB: Prompt & Data Logic Analysis

This report evaluates the current methodology for entity extraction and proposes a refined data science framework for the AlchemyDB Digital Humanities project.

## 1. Critique: Prompt & Context Engineering

### Current Style: "The Search Party" Approach
Previous attempts focused on asking the LLM to "find" or "list" entities. While intuitive, this approach is prone to:
- **Hallucination Persistence**: If an LLM "identifies" an alchemist without a quote, the error is silent and permanent.
- **Context Loss**: Sending flat lists without the surrounding text makes human verification (the "Digital Humanities" standard) impossible.

### Recommended Shift: "The Specimen Procurement" Style
We must move from "search" to "extraction with evidence":
- **Constraint Engineering**: Prohibit the LLM from returning any entity that it cannot provide a direct, verbatim quote for.
- **Overlap Optimization**: Our 150-token overlap is excellent for names, but we should increase it for "Philosophy Extraction" where arguments span multiple pages.
- **Agentic Iteration**: Use a "Schema-First" prompt. Don't ask for a list; ask the LLM to populate a predefined JSON object.

---

## 2. Analysis: Documents & Dictionary Entries as Data Problems

### Documents: The Non-Linear Volume Problem
Documents are not just "files"; they are coordinate systems.
- **Data Problem**: How to map a 17th-century symbol on page 42 to a structured database entry while preserving the original layout context?
- **Solution**: Implement "Chunk-to-Coordinate" mapping. Store the `page_number` and `bbox` (bounding box) if possible, turning every extraction into a hyperlink back to the PDF.

### Dictionary Entries: The Evolving Ontology Problem
Alchemical terms (e.g., "Mercury") change meaning based on the author, century, and tradition.
- **Data Problem**: A "Flat List" fails to capture semantic drift.
- **Solution**: Dictionary entries must be **Versioned Polysemies**. 
    - Instead of `Term -> Definition`, use `Term -> [ {Tradition: Paracelsian, Meaning: X}, {Tradition: Hermetic, Meaning: Y} ]`.
    - This transforms the "Dictionary" from a list into a **Semantic Graph**.

### "List" vs. "Registry"
- **"List"** (User term): Historically implies a static, flat enumeration.
- **"Registry"** (Strategic term): Implies an active, relational authority file. We are building a **Registry of Practitioners**, where each "Alchemist" is a node connected to "Documents" (Evidence) and "Lexicons" (Logic).

---

## 3. The Visibility Solution
The "Dashboard" is not just a UI; it is the **Validation Layer**. By seeing the "Specimen Drawer" fill up with real-time quotes, we turn "Prompt Engineering" into "Knowledge Curation."
