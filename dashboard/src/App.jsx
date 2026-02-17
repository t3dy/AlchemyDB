import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom'
import Discovery from './Discovery'
import ProjectLog from './ProjectLog'
import CodexView from './CodexView'
import BiographyDetail from './BiographyDetail'
import LibraryView from './LibraryView'
import WhosWhoView from './WhosWhoView'
import HistoriographyView from './HistoriographyView'
import './App.css'

function AppContent() {
  const location = useLocation();
  const isCodex = location.pathname === '/lexicon';

  return (
    <div className="dashboard-container">
      {!isCodex && (
        <header className="main-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <div>
            <h1 style={{ margin: 0 }}>AlchemyDB <span style={{ color: '#888', fontSize: '1rem' }}>Discovery Dashboard</span></h1>
          </div>
          <nav style={{ display: 'flex', gap: '2rem' }}>
            <Link to="/" className="nav-link">DISCOVERY</Link>
            <Link to="/library" className="nav-link">LIBRARY</Link>
            <Link to="/lexicon" className="nav-link">DICTIONARY</Link>
            <Link to="/whos-who" className="nav-link">WHO'S WHO</Link>
            <Link to="/historiography" className="nav-link">HISTORIOGRAPHY</Link>
            <Link to="/docs" className="nav-link">PROJECT LOG</Link>
          </nav>
        </header>
      )}

      <Routes>
        <Route path="/" element={<Discovery />} />
        <Route path="/library" element={<LibraryView />} />
        <Route path="/lexicon" element={<CodexView />} />
        <Route path="/whos-who" element={<WhosWhoView />} />
        <Route path="/biography/:entityId" element={<BiographyDetail />} />
        <Route path="/historiography" element={<HistoriographyView />} />
        <Route path="/docs" element={<ProjectLog />} />
      </Routes>
    </div>
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  )
}

export default App
