import { Outlet } from 'react-router';
import data from '../../../server/db.json';
import * as S from './styles';

export const Production = () => {
  return (
    <div>
      <S.Title>O que você vai fabricar hoje</S.Title>
      <S.ProductsContainer>
        {data.products.map(product => (
          <S.ProductContainer to={`./${product.id}`} key={product.id}>
            <S.ProductImage src={product.image} alt={product.name} />
            <h4>{product.name}</h4>
          </S.ProductContainer>
        ))}
      </S.ProductsContainer>
      <Outlet />
    </div>
  );
};
