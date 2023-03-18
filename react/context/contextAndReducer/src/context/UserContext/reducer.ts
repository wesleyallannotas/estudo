// export type ReducerAction = {
//   type: 'update_name' | 'update_id' | 'increment' | 'decrement';
//   payload: string;
// }; // Forma 1

// export type ReducerAction =
//   | { type: 'update_name'; newName: string }
//   | { type: 'update_id'; newId: string }
//   | { type: 'increment' }
// | { type: 'decrement' }; // Forma 2

export type ReducerAction =
  | { type: 'update_name'; payload: string }
  | { type: 'update_id'; payload: string }
  | { type: 'increment' | 'decrement' }; // Forma 3

export type ReducerState = { name: string; id: string; counter: number };

export const initialState: ReducerState = {
  name: '',
  id: '',
  counter: 0,
};

export function userReducer(state: ReducerState, action: ReducerAction) {
  switch (action.type) {
    case 'update_name':
      if (action.payload === 'teste')
        return { ...state, name: 'Usuário invalido!' };
      return { ...state, name: action.payload };
    case 'update_id':
      return { ...state, id: action.payload };
    case 'increment':
      return { ...state, counter: state.counter + 1 };
    case 'decrement':
      return { ...state, counter: state.counter - 1 };
    default:
      return state;
  }
}
