import { useState } from 'react';

export const Counter = () => {
  const [counter, setCounter] = useState<number>(0);
  function add() {
    setCounter(prevState => prevState + 1);
  }
  function subtract() {
    setCounter(prevState => prevState - 1);
  }
  return (
    <>
      <h3>{counter}</h3>
      <button onClick={add}>Add</button>
      <button onClick={subtract}>Remove</button>
    </>
  );
};
