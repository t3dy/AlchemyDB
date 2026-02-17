# Report: Database & Entry Improvement Roadmap

To move from a "Glossary" to a "Digitial Humanities Research Engine," we must refine our underlying metadata logic.

## 1. From Taxonomy to Actor-Network
Our current entries are "Static Profiles." We suggest transitioning to a **Relational Actor-Network** model.

### Improve Entry Depth:
- **Include Social Capital**: For every scholar (Newman, Principe, Smith), our entries should now track their **historiographical argument**. (e.g., "Newman argues for the corpuscularian nature of Starkey's alchemy").
- **Track Material Basis**: Link texts not just to authors, but to the **substances** they describe. A text on *Antimony* should be linked to the *art of glassmaking* and *pharmacy*.

## 2. Infrastructure Enhancements
### Advanced Metadata Fields:
- `patronage_chain`: Tracking who funded the work (e.g., The Medici, Emperor Leopold I).
- `experimental_provenance`: Linking a claim to a specific artisanal workshop or university laboratory.
- `identity_confidence`: For pseudonymous authors like Eirenaeus Philalethes, tracking the "weight of evidence" for their real-world identity.

## 3. Visualization Proposals
### The "Epistemic Slider":
A dashboard feature that allows users to toggle between:
- **Symbolic View**: Highlighting allegories (Kings, Queens, Dragons).
- **Artisanal View**: Highlighting processes (Calcination, Fusion).
- **Political View**: Highlighting economic reform and court projects.

## 4. Entry Refinement (Thick Description)
We will adopt the "Thick Description" methodology for new dictionary entries. 
- *Instead of*: "Nigredo = blackening."
- *We will have*: "Nigredo = The blackening stage. In the laboratory of the Uffizi, this corresponded to the oxidative phase of lead-based pigments, while in symbolic texts it represented the putrefaction of the soul."
