import React from 'react';

function ProjectLog() {
    return (
        <div className="project-log-view">
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>

                {/* History Section */}
                <section className="glass-panel" style={{ padding: '2rem' }}>
                    <h2 style={{ color: '#D4AF37', borderBottom: '1px solid rgba(212, 175, 55, 0.3)', paddingBottom: '0.5rem' }}>V1: History & Learning Journey</h2>
                    <div className="log-content" style={{ lineHeight: '1.6', color: '#F4EBD0' }}>
                        <h3>The Genesis: From Folders to Coordinates</h3>
                        <p>AlchemyDB began as a collection of 205 orphaned PDFs. Our first mission was simple: don't lose the files. We built an inventory script to hash, deduplicate, and catalog every document.</p>

                        <h3>The Cognitive Pivot: The Evidence Trail</h3>
                        <p>The most significant leap in our design logic was the rejection of "Extract and Forget." In Digital Humanities, a name without a source is a hallucination.</p>
                        <ul>
                            <li><strong>The Design:</strong> We pivoted to a model where the Document Chunk is the primary unit of truth.</li>
                            <li><strong>The Logic:</strong> If we can't point to the exact paragraph where a practitioner appears, they don't exist in our Registry.</li>
                        </ul>

                        <h3>Aesthetic Logic: The "Arcane Modern" Theme</h3>
                        <p>Parchment and Glass: The use of semitransparent glass panels over dark backgrounds evokes the feeling of looking at a specimen through a microscope.</p>
                    </div>
                </section>

                {/* Multimedia Dictionary Concept Section */}
                <section className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #D4AF37' }}>
                    <h2 style={{ color: '#D4AF37', borderBottom: '1px solid rgba(212, 175, 55, 0.3)', paddingBottom: '0.5rem' }}>Multimedia Dictionary Concept</h2>
                    <div className="log-content" style={{ lineHeight: '1.6', color: '#F4EBD0' }}>
                        <p>Our vision is to transform AlchemyDB into a <strong>Beautiful Multimedia Dictionary</strong>. This isn't just a list of words; it's a living archive of the Hermetic tradition.</p>

                        <h4>The Lexicon Phase</h4>
                        <p>We've implemented a seed of 500 terms. Every term is hyperlinked to its <strong>Evidence Trail</strong> (mentions across the 205 PDFs). Soon, these will expand into:</p>
                        <ul>
                            <li><strong>Interactive Biographies:</strong> Detailed life stories of alchemists like Paracelsus or Jabir.</li>
                            <li><strong>Textual Summaries:</strong> Deep dives into manuscripts like the <em>Splendor Solis</em>.</li>
                            <li><strong>Spatial Atlas:</strong> Maps showing the geographic flow of alchemical knowledge.</li>
                        </ul>

                        <h4>How to Explore</h4>
                        <p>Use the <strong>LEXICON</strong> tab to search for substances, symbols, or practitioners. Watch for the 'MENTIONS' count—this shows you the term's "semantic weight" in your current library.</p>
                    </div>
                </section>

                {/* Instructions Section */}
                <section className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #D4AF37' }}>
                    <h2 style={{ color: '#D4AF37', borderBottom: '1px solid rgba(212, 175, 55, 0.3)', paddingBottom: '0.5rem' }}>Narrative System Instructions</h2>
                    <div className="log-content" style={{ lineHeight: '1.6', color: '#F4EBD0' }}>
                        <p>As a user or tester, your goal is not just to "search" but to "curate."</p>

                        <h4>1. The Discovery Dashboard</h4>
                        <p>The <strong>Library Table</strong> is your bird's-eye view. The <strong>Specimen Drawer</strong> is your active research desk where "Probabilities" appear.</p>

                        <h4>2. Working with Candidates</h4>
                        <p>Verify the <strong>Direct Quote</strong>. Does the text actually support the claim? Trace the <code>document_id</code> back to the source tradition.</p>

                        <h4>3. Storytelling with Data</h4>
                        <p>Look for <strong>Cross-Pollination</strong>. Find how an author like Agrippa citations earlier thinkers like Masha'allah. Find the secret protagonists of your study.</p>
                    </div>
                </section>

            </div>
        </div>
    );
}

export default ProjectLog;
