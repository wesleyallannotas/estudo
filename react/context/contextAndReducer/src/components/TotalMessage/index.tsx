import { useContext } from 'react';
import { useUser } from '../../context/UserContext';
import styles from './TotalMessage.module.css';

export const TotalMessage = () => {
  const { state: userState, dispatch: userDispatch } = useUser();

  return (
    <div className={styles.container}>
      <p>
        {userState.name && `Obrigado pela compra ${userState.name}.`} <br />{' '}
        Devido o valor ser maior que{' '}
        <span className={styles.money}>R$ 100,00</span> você ganhou um desconto
        de <span className={styles.discount}>5%</span>
      </p>
      <input
        className={styles.inputUsername}
        type="text"
        placeholder="Alterar nome do Checkout"
        onChange={e =>
          userDispatch({ type: 'update_name', payload: e.target.value })
        }
      />
      <input
        className={`${styles.inputId} ${styles.marginLeft}`}
        type="id"
        placeholder="ID"
        onChange={e =>
          userDispatch({ type: 'update_id', payload: e.target.value })
        }
      />
      <button
        className={`${styles.button} ${styles.marginLeft}`}
        onClick={() => userDispatch({ type: 'increment' })}
      >
        +
      </button>
      <button
        className={`${styles.button} ${styles.marginLeft}`}
        onClick={() => userDispatch({ type: 'decrement' })}
      >
        -
      </button>
    </div>
  );
};
