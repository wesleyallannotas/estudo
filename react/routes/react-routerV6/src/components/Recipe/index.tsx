import { useParams } from 'react-router-dom';
import data from '../../../server/db.json';

type ParamsType = {
  selectedProduct: string;
};

export const Recipe = () => {
  const { selectedProduct } = useParams<ParamsType>();

  const selected = data.products.find(
    product => product.id.toString() === selectedProduct
  );

  return <p>{selected?.recipe}</p>;
};
