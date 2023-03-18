import { Checkout } from './components/Checkout';
import { useUser } from './context/UserContext';

function App() {
  const { state: userState, dispatch: userDispatch } = useUser();

  return (
    <div className="App">
      {userState.name && <h1>Bem vindo {userState.name}</h1>}
      {userState.id && <p>ID: {userState.id}</p>}
      <Checkout />
    </div>
  );
}

export default App;
