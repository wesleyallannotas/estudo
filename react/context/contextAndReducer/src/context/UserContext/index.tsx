import { createContext, useContext, useReducer } from 'react';
import {
  userReducer,
  initialState,
  ReducerAction,
  ReducerState,
} from './reducer';

interface IUserContext {
  state: ReducerState;
  dispatch(action: ReducerAction): void;
}

type UserContextProps = {
  children: React.ReactNode;
};

const UserContext = createContext<IUserContext | undefined>(undefined);

export const UserProvider = ({ children }: UserContextProps) => {
  const [state, dispatch] = useReducer(userReducer, initialState);

  return (
    <UserContext.Provider value={{ state, dispatch }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => {
  const context = useContext(UserContext);

  if (!context) {
    throw new Error('useUser must be used within a UserProvider');
  }

  return context;
};
