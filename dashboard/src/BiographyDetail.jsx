import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import biographiesData from './data/biographies.json'
import candidatesData from './data/candidates.json'

function BiographyDetail() {
    const { entityId } = useParams()
    const [bio, setBio] = useState(null)
    const [mentions, setMentions] = useState([])

    useEffect(() => {
        const foundBio = biographiesData.find(b => b.entity_id === parseInt(entityId))
        if (foundBio) {
            setBio(foundBio)
            // Filter mentions for this entity
            const foundMentions = candidatesData.filter(c => c.id === parseInt(entityId))
            setMentions(foundMentions)
        }
    }, [entityId])

    if (!bio) {
        return (
            <div className="glass-panel" style={{ textAlign: 'center', padding: '3rem' }}>
                <h2>Biography Not Found</h2>
                <Link to="/lexicon" className="nav-link">Return to Lexicon</Link>
            </div>
        )
    }

    const milestones = JSON.parse(bio.milestones_json || '[]')
    const primaryTexts = JSON.parse(bio.primary_texts_json || '[]')

    return (
        <div className="biography-detail">
            <Link to="/lexicon" style={{ color: '#D4AF37', textDecoration: 'none', fontSize: '0.9rem', marginBottom: '2rem', display: 'inline-block' }}>
                ← BACK TO LEXICON
            </Link>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '2rem' }}>
                <main>
                    <section className="glass-panel" style={{ padding: '2.5rem', marginBottom: '2rem' }}>
                        <header style={{ marginBottom: '2rem', borderBottom: '1px solid rgba(212, 175, 55, 0.3)', paddingBottom: '1rem' }}>
                            <h1 style={{ margin: 0, color: '#D4AF37', fontSize: '2.5rem' }}>{bio.full_name}</h1>
                            <div style={{ display: 'flex', gap: '2rem', marginTop: '0.5rem', opacity: 0.8 }}>
                                <span><strong>LIFESPAN:</strong> {bio.lifespan}</span>
                                <span><strong>TRADITION:</strong> {bio.tradition}</span>
                            </div>
                        </header>

                        <div className="bio-narrative" style={{ lineHeight: '1.8', fontSize: '1.1rem', color: '#F4EBD0' }}>
                            <p>{bio.narrative_summary}</p>
                        </div>
                    </section>

                    <section className="glass-panel" style={{ padding: '2rem' }}>
                        <h3 style={{ color: '#D4AF37', marginBottom: '1.5rem' }}>Timeline of Milestones</h3>
                        <div className="timeline" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', borderLeft: '2px solid rgba(212, 175, 55, 0.3)', paddingLeft: '1.5rem' }}>
                            {milestones.map((m, idx) => (
                                <div key={idx} className="timeline-item" style={{ position: 'relative' }}>
                                    <div style={{
                                        position: 'absolute',
                                        left: '-1.9rem',
                                        top: '0.2rem',
                                        width: '10px',
                                        height: '10px',
                                        background: '#D4AF37',
                                        borderRadius: '50%',
                                        boxShadow: '0 0 10px #D4AF37'
                                    }}></div>
                                    <div style={{ fontWeight: 'bold', color: '#D4AF37', marginBottom: '0.2rem' }}>{m.year}</div>
                                    <div style={{ opacity: 0.9 }}>{m.event}</div>
                                </div>
                            ))}
                        </div>
                    </section>
                </main>

                <aside>
                    <section className="glass-panel" style={{ padding: '1.5rem', marginBottom: '2rem' }}>
                        <h4 style={{ margin: '0 0 1rem 0', color: '#D4AF37', borderBottom: '1px solid #333', paddingBottom: '0.5rem' }}>PRIMARY TEXTS</h4>
                        <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
                            {primaryTexts.map((txt, idx) => (
                                <li key={idx} style={{ fontStyle: 'italic', color: '#bdbdbd' }}>• {txt}</li>
                            ))}
                        </ul>
                    </section>

                    <section className="glass-panel" style={{ padding: '1.5rem', borderLeft: '4px solid #D4AF37' }}>
                        <h4 style={{ margin: '0 0 1rem 0', color: '#D4AF37' }}>CORPUS EVIDENCE</h4>
                        <p style={{ fontSize: '0.8rem', opacity: 0.6, marginBottom: '1rem' }}>Verbatim mentions discovered in your PDF library.</p>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                            {mentions.slice(0, 5).map((m, idx) => (
                                <div key={idx} style={{
                                    padding: '1rem',
                                    background: 'rgba(0,0,0,0.3)',
                                    fontSize: '0.85rem',
                                    borderRadius: '4px',
                                    border: '1px solid rgba(255,255,255,0.05)'
                                }}>
                                    <div style={{ fontSize: '0.75rem', opacity: 0.5, marginBottom: '0.5rem' }}>DOC_ID: {m.document_id}</div>
                                    <div style={{ fontStyle: 'italic', color: '#ddd' }}>"{m.quote}"</div>
                                </div>
                            ))}
                        </div>
                    </section>
                </aside>
            </div>
        </div>
    )
}

export default BiographyDetail;
