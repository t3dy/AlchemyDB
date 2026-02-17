import React from 'react';
import { Link } from 'react-router-dom';
import biosData from './exports/biographies.json';

function WhosWhoView() {
    // Filter only scholars for this view
    const scholars = biosData.filter(bio => bio.tradition.includes('New Historiography'));

    return (
        <div className="whos-who-view">
            <header className="view-header">
                <h2>Who's Who: The New Historiography</h2>
                <div className="guide-box glass-panel">
                    <p><strong>Section Guide:</strong> This view features the <code>biographies</code> table, specifically filtered for modern alchemical historians. These entries represent the "New Historiography"—scholars who prioritize laboratory reconstruction, archival rigor, and the material reality of "Chymistry."</p>
                </div>
            </header>

            <div className="scholar-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(400px, 1fr))', gap: '2rem', marginTop: '2rem' }}>
                {scholars.map(scholar => (
                    <div key={scholar.entity_id} className="glass-panel scholar-card" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', borderTop: '2px solid #D4AF37' }}>
                        <h3 style={{ color: '#D4AF37', margin: '0 0 0.5rem 0', fontSize: '1.5rem' }}>{scholar.full_name}</h3>
                        <div style={{ fontSize: '0.8rem', color: '#D4AF37', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '1rem' }}>
                            {scholar.social_role || 'Scholar'} • {scholar.tradition}
                        </div>
                        <div style={{ fontSize: '0.9rem', color: '#888', marginBottom: '1.5rem', fontStyle: 'italic' }}>
                            Lifespan: {scholar.lifespan}
                        </div>

                        <p style={{ fontSize: '1rem', lineHeight: '1.6', color: '#f4ebd0', marginBottom: '1.5rem' }}>{scholar.narrative_summary}</p>

                        {scholar.knowledge_economy_role && (
                            <div style={{ background: 'rgba(212,175,55,0.05)', padding: '1rem', borderRadius: '4px', marginBottom: '1.5rem', borderLeft: '2px solid #D4AF37' }}>
                                <span style={{ fontSize: '0.7rem', color: '#D4AF37', textTransform: 'uppercase', display: 'block', marginBottom: '0.5rem' }}>Socio-Economic Role</span>
                                <span style={{ fontSize: '0.9rem', color: '#ccc' }}>{scholar.knowledge_economy_role}</span>
                            </div>
                        )}

                        <div style={{ marginTop: 'auto' }}>
                            <h4 style={{ fontSize: '0.8rem', color: '#D4AF37', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.5rem' }}>Primary Focus / Works</h4>
                            <ul style={{ fontSize: '0.85rem', color: '#ccc', paddingLeft: '1.2rem' }}>
                                {scholar.primary_texts.map((text, idx) => (
                                    <li key={idx} style={{ marginBottom: '0.4rem' }}>{text}</li>
                                ))}
                            </ul>
                        </div>

                        <Link
                            to={`/biography/${scholar.entity_id}`}
                            className="glass-button"
                            style={{ marginTop: '2rem', textAlign: 'center', textDecoration: 'none', display: 'block' }}
                        >
                            VIEW FULL DOSSIER
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default WhosWhoView;
