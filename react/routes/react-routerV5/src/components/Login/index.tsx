export const Login = () => {
  const setToken = () => {
    localStorage.setItem('token', '1234567890');
  };

  return <button onClick={setToken}>Login</button>;
};
