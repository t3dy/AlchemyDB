import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Discovery from './Discovery'
import ProjectLog from './ProjectLog'
import LexiconView from './LexiconView'
import './App.css'

function App() {
  return (
    <Router>
      <div className="dashboard-container">
        <header className="main-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <div>
            <h1 style={{ margin: 0 }}>AlchemyDB <span style={{ color: '#888', fontSize: '1rem' }}>Discovery Dashboard</span></h1>
          </div>
          <nav style={{ display: 'flex', gap: '2rem' }}>
            <Link to="/" className="nav-link">DISCOVERY</Link>
            <Link to="/lexicon" className="nav-link">LEXICON</Link>
            <Link to="/docs" className="nav-link">PROJECT LOG</Link>
          </nav>
        </header>

        <Routes>
          <Route path="/" element={<Discovery />} />
          <Route path="/lexicon" element={<LexiconView />} />
          <Route path="/docs" element={<ProjectLog />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
