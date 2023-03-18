import {
  useParams,
  useRouteMatch,
  generatePath,
  useHistory,
} from 'react-router-dom';
import data from '../../../server/db.json';
import * as S from './styles';

interface ParamsType {
  selectedProduct: string;
}

export const Production = () => {
  // const { selectedProduct } = useParams<{ selectedProduct: string }>();
  const { selectedProduct } = useParams<ParamsType>();
  const routeMatch = useRouteMatch();
  const history = useHistory();

  const selected = data.products.find(
    product => product.id.toString() === selectedProduct
  );

  const goToProduct = (id: number): void => {
    const urlToGo = generatePath(routeMatch.path, { selectedProduct: id });
    history.push(urlToGo);
  };

  return (
    <div>
      <S.Title>O que você vai fabricar hoje</S.Title>
      <S.ProductsContainer>
        {data.products.map(product => (
          <S.ProductContainer
            key={product.id}
            onClick={() => goToProduct(product.id)}
          >
            <S.ProductImage src={product.image} alt={product.name} />
            <h4>{product.name}</h4>
          </S.ProductContainer>
        ))}
      </S.ProductsContainer>
      <S.Text>{selected?.recipe}</S.Text>
    </div>
  );
};
