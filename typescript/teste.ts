interface Person {
  id: number;
  name: string;
  age: number;
  isAdmin: boolean;
}

type PartPersonId<T> = {
  [P in keyof T]?: T[P];
} & { id: number };

const wesley: PartPersonId<Person> = {
  id: 473,
};
