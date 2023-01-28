import React from 'react';

interface InputProps {
  label: string;
}

export const Input = (props: InputProps) => {
  return (
    <div>
      <label>{props.label}</label>
      <br />
      <input />
    </div>
  )
}