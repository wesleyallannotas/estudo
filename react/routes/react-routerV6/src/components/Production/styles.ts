import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const Title = styled.h3`
  padding: 1rem 0;
`;

export const ProductsContainer = styled.div`
  display: flex;
  align-items: center;
  background-color: #fafafa;
  box-shadow: 0 0 2rem rgba(0, 0, 0, 0.2);
`;

export const ProductContainer = styled(Link)`
  padding-top: 0.3rem;
  text-decoration: none;
  cursor: pointer;
`;

export const ProductImage = styled.img`
  width: 50%;
  height: 50%;
  border-radius: 0.5rem;
`;
