let user: TUser;

// Union
type UserId = number | string | undefined;
type Fruit = 'melao' | 'abacaxi' | 'uva';

// Tupla
type UserAndId = [user: string, Id: number];
type UserAndId2 = [string, number];

// Objetos
type TUser = {
  id: number;
  username: string;
  token: string;
  isAdmin?: boolean; // Opcional
};

// Funções
type setValue = (newValeu: number) => void;
const setId: setValue = newValue => (user.id = newValue);

// Declaration Merging
type PointX = {
  x: number;
};
type PointY = {
  x: number;
};

// Intersecção
type Point = PointX & PointY & { z: number };

// Mapped Types #1
type FruitCount = {
  [key in Fruit]: number;
};
const fruits: FruitCount = {
  melao: 2,
  abacaxi: 3,
  uva: 4,
};

// Mapped Types Partial
interface Person {
  id: number;
  name: string;
  age: number;
  isAdmin: boolean;
}
const personPartial: Partial<Person> = {
  id: 12,
  name: 'Wesley',
  age: 25,
};

// Mapped Types Readonly
const personReadonly: Readonly<Person> = {
  id: 15,
  name: 'Carlos',
  age: 32,
  isAdmin: false,
};
