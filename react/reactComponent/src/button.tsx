import React from "react";

interface ButtonProps {
  click: () => void;
}

export function ButtonInterno() {
  function showMessage() {
    window.alert('clicou!')
  }

  return (
    <button onClick={showMessage}>Clique!</button>
 )
}

export function ButtonProp(props: ButtonProps) {
  return (
    <button onClick={props.click}>Clique aqui!</button>
  )
}