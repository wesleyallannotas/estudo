import styled from 'styled-components';

export const Title = styled.h3`
  padding: 1rem 0;
`;

export const StockContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-color: #fafafa;
  box-shadow: 0 0 2rem rgba(0, 0, 0, 0.2);
  & h4,
  & h5 {
    margin: 1rem 0;
  }
`;

export const ButtonVisibility = styled.button`
  background: none;
  cursor: pointer;
  margin-left: 0.5rem;
`;
