
import React from 'react';
import { Link } from 'react-router-dom';

const CodexLayout = ({ sidebar, content }) => {
    return (
        <div className="codex-container" style={{
            display: 'flex',
            height: '100vh',
            background: '#0a0a0a',
            color: '#e0e0e0',
            fontFamily: '"EB Garamond", serif'
        }}>
            {/* Left Sidebar: The Index */}
            <aside className="codex-sidebar" style={{
                width: '350px',
                borderRight: '1px solid #333',
                display: 'flex',
                flexDirection: 'column',
                background: '#111'
            }}>
                <div style={{ padding: '1.5rem', borderBottom: '1px solid #333' }}>
                    <h1 style={{
                        fontFamily: '"Cinzel", serif',
                        fontSize: '1.2rem',
                        color: '#D4AF37',
                        margin: 0,
                        letterSpacing: '2px'
                    }}>
                        ALCHEMY<span style={{ color: '#fff' }}>DB</span>
                    </h1>
                    <div style={{ fontSize: '0.7rem', color: '#666', marginTop: '0.2rem', textTransform: 'uppercase' }}>
                        The Digital Codex
                    </div>
                </div>

                <div style={{ flex: 1, overflowY: 'auto' }}>
                    {sidebar}
                </div>

                <div style={{ padding: '1rem', borderTop: '1px solid #333', fontSize: '0.8rem', color: '#666' }}>
                    <Link to="/" style={{ color: '#888', textDecoration: 'none', marginRight: '1rem' }}>Home</Link>
                    <Link to="/whos-who" style={{ color: '#888', textDecoration: 'none' }}>Scholars</Link>
                </div>
            </aside>

            {/* Main Stage: The Reader */}
            <main className="codex-content" style={{
                flex: 1,
                overflowY: 'auto',
                padding: '0'
            }}>
                <div style={{ maxWidth: '900px', margin: '0 auto', padding: '4rem' }}>
                    {content}
                </div>
            </main>
        </div>
    );
};

export default CodexLayout;
