import React from 'react';

function ProjectLog() {
    const logs = [
        {
            title: "Phase 18: Chemical Synthesis & Terminology Refinement",
            date: "2026-02-16",
            content: "Initiated the 'Chemical Synthesis' phase. Developed a Style Guide and Template for dual-history dictionary entries (alchemical vs. modern). Planned 5 specialized scripts for automated substance/process extraction.",
            tags: ["Synthesis", "Chemical", "Refinement"]
        },
        {
            title: "Phase 17: DH Synthesis & AI Engineering Report",
            date: "2026-02-16",
            content: "Synthesized meta-analysis on our Digital Humanities progress. Evaluated the transition from a 'Taxonomic Glossary' to a relational 'Scholarly Apparatus' using deep context engineering.",
            tags: ["Synthesis", "AI Engineering", "DH"]
        },
        {
            title: "Phase 16: Strategic Feedback & Socio-Economic Modeling",
            date: "2026-02-16",
            content: "Integrating insights from 'The Business of Alchemy' (Pamela H. Smith). Expanded schema to support 'Knowledge Type' and 'Social Roles'.",
            tags: ["Strategy", "Feedback", "Socio-Economic"]
        }
    ];

    return (
        <div className="project-log-view" style={{ animation: 'fadeIn 0.5s ease-out' }}>
            <header className="view-header">
                <h2 style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>Laboratory Log & Scholarly Reports</h2>
                <div className="guide-box glass-panel">
                    <p><strong>Section Guide:</strong> This log documents the evolution of AlchemyDB from a metadata registry into a multi-dimensional <strong>Scholarly Apparatus</strong>. Below are the deep analytical reports addressing recent scholarly feedback and chemical synthesis strategies.</p>
                </div>
            </header>

            <div style={{ display: 'grid', gridTemplateColumns: 'minmax(0, 1fr) 450px', gap: '3rem', marginTop: '2rem' }}>

                {/* Main Development Log */}
                <div className="log-list">
                    <h2 style={{ fontSize: '1.2rem', color: '#888', textTransform: 'uppercase', letterSpacing: '2px', marginBottom: '1.5rem' }}>Development Timeline</h2>
                    {logs.map((log, idx) => (
                        <div key={idx} className="glass-panel" style={{ padding: '2rem', marginBottom: '2rem', borderLeft: '5px solid #D4AF37', position: 'relative' }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                <h3 style={{ margin: 0, color: '#D4AF37', fontSize: '1.5rem' }}>{log.title}</h3>
                                <span style={{ fontSize: '0.9rem', color: '#666', background: 'rgba(0,0,0,0.3)', padding: '0.2rem 0.6rem', borderRadius: '4px' }}>{log.date}</span>
                            </div>
                            <p style={{ margin: '1.5rem 0', lineHeight: '1.7', fontSize: '1.05rem', color: '#F4EBD0' }}>{log.content}</p>
                            <div style={{ display: 'flex', gap: '0.75rem' }}>
                                {log.tags.map(tag => (
                                    <span key={tag} className="status-badge" style={{ background: 'rgba(212,175,55,0.1)', color: '#D4AF37', border: '1px solid rgba(212,175,55,0.2)' }}>{tag}</span>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>

                {/* Analytical Sidebar Reports */}
                <aside style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>

                    {/* Report: Chemical Synthesis Roadmap */}
                    <div className="glass-panel" style={{ padding: '2rem', borderTop: '4px solid #00A86B' }}>
                        <h3 style={{ marginTop: 0, color: '#00A86B' }}>Chemical Synthesis Roadmap</h3>
                        <div style={{ fontSize: '0.95rem', lineHeight: '1.6', color: '#ccc' }}>
                            <p><strong>Goal:</strong> Distinguishing 'Vitriol (alchemical)' from 'Ferrous Sulfate (modern)'. Bridge historical theory with material provenance.</p>
                            <ul style={{ paddingLeft: '1.2rem', marginTop: '1rem', display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                                <li>
                                    <strong style={{ color: '#00A86B' }}>Mining Strategy:</strong> Using LLM extraction from Principe, Newman, and Obrist to identify 'Chemical Syntheses'.
                                </li>
                                <li>
                                    <strong style={{ color: '#00A86B' }}>Automation Suite:</strong> Developing 5 scripts (SubstanceMiner, EquipmentMiner, ProcessMapper, etc.) to refresh the lexicon.
                                </li>
                            </ul>
                        </div>
                    </div>

                    {/* Report: DH & AI Engineering Report */}
                    <div className="glass-panel" style={{ padding: '2rem', borderTop: '4px solid #D4AF37' }}>
                        <h3 style={{ marginTop: 0, color: '#D4AF37' }}>DH & AI Engineering Report</h3>
                        <div style={{ fontSize: '0.95rem', lineHeight: '1.6', color: '#ccc' }}>
                            <p><strong>Critique:</strong> Transformation from 'Archive' to 'Apparatus'. Successful use of 'Rich Profile' templates to enforce domain-specific data models during mining. Highlighted the role of state management in context engineering.</p>
                        </div>
                    </div>

                    {/* Report: Study of 'Laboratories of Art' */}
                    <div className="glass-panel" style={{ padding: '2rem', borderTop: '4px solid #D4AF37' }}>
                        <h3 style={{ marginTop: 0, color: '#D4AF37' }}>Study: Laboratories of Art</h3>
                        <div style={{ fontSize: '0.95rem', lineHeight: '1.6', color: '#ccc' }}>
                            <p><strong>Learning:</strong> Shared material culture between alchemists and artisans (Uffizi, Casino di San Marco). Integrated 21 entries focusing on the 'Technics of Transformation'.</p>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    );
}

export default ProjectLog;
