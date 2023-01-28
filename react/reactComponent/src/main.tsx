import React from 'react';
import ReactDOM from 'react-dom/client';
import { Counter } from './counter';
import { Text } from './text';
import './index.css';

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <>
    <Counter />
    <br />
    <br />
    <Text />
  </>
);
