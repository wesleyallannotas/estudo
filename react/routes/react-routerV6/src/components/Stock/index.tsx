import { useLocation, useNavigate } from 'react-router-dom';
import { AiFillEyeInvisible, AiFillEye } from 'react-icons/ai';
import data from '../../../server/db.json';
import * as S from './styles';

interface ParamsType {
  selectedProduct: string;
}

export const Stock = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const showStock: boolean = queryParams.get('showStock') === 'true';

  const toggleStockVisibility = (): void => {
    navigate(`?showStock=${!showStock}`, { replace: true });
  };

  return (
    <div>
      <S.Title>
        Estoque de Produtos
        <S.ButtonVisibility onClick={toggleStockVisibility}>
          {showStock ? <AiFillEyeInvisible /> : <AiFillEye />}
        </S.ButtonVisibility>
      </S.Title>
      <S.StockContainer>
        {data.products.map(product => (
          <div key={product.id}>
            <h4>{product.name}</h4>
            <h5>{showStock ? product.stock : '-'}</h5>
          </div>
        ))}
      </S.StockContainer>
    </div>
  );
};
