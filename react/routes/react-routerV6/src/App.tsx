import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Production } from './components/Production';
import { Stock } from './components/Stock';
import './App.css';
import { NotFound } from './components/NotFound';
import { ProtectedRoute } from './components/ProtectedRoute';
import { Login } from './components/Login';
import { Recipe } from './components/Recipe';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Navigate to={'/production'} />} />
          <Route path="/production" element={<Production />}>
            <Route path=":selectedProduct" element={<Recipe />} />
          </Route>
          <Route
            path="/stock"
            element={
              <ProtectedRoute>
                <Stock />
              </ProtectedRoute>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
