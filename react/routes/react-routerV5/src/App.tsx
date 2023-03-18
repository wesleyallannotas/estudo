import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';
import { Navbar } from './components/Navbar';
import { Production } from './components/Production';
import { Stock } from './components/Stock';
import './App.css';
import { NotFound } from './components/NotFound';
import { ProtectedRoute } from './components/ProtectedRoute';
import { Login } from './components/Login';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Navbar />
        <Switch>
          <Route exact path="/">
            <Redirect to={'/production'} />
          </Route>
          <Route path="/production/:selectedProduct?">
            <Production />
          </Route>
          <ProtectedRoute path="/stock">
            <Stock />
          </ProtectedRoute>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="*">
            <NotFound />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
