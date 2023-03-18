import * as S from './styles';

export const Navbar = () => {
  return (
    <S.Container>
      <S.Item to="/production">Produção</S.Item>
      <S.Item to="/stock">Estoque</S.Item>
    </S.Container>
  );
};
