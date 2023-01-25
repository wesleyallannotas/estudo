let user: IUser;

// Objeto
interface IUser {
  id: number;
  username: string;
  token: string;
  isAdmin?: boolean; // Opcional
}

// Declaration Merging
interface Point {
  x: number;
}
interface Point {
  y: number;
}

// Extensão
interface Dimension extends Point {
  z: number;
}

// Implementando Classe
class User implements IUser {
  /* Clase */
}

// Função
interface setValue {
  (newValeu: number): void;
}

const setId: setValue = newValue => (user.id = newValue);
