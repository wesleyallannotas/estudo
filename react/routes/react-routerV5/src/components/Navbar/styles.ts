import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 60px;
  background-color: #f7f3e3;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.25);
`;

export const Item = styled(NavLink)`
  text-decoration: none;
  color: black;
  font-size: 2.4rem;
  &.active {
    text-decoration: none;
    color: #6f1a07;
    border-bottom-width: 1px;
    border-bottom-style: solid;
    border-bottom-color: #af9a64;
  }
`;
