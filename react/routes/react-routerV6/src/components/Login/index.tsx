import { useNavigate } from 'react-router';

export const Login = () => {
  const navigate = useNavigate();
  const setToken = () => {
    localStorage.setItem('token', '1234567890');
    navigate('/stock');
  };

  return <button onClick={setToken}>Login</button>;
};
