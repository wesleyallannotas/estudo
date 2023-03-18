import { Total } from '../Total';
import styles from './Checkout.module.css';
import { useUser } from '../../context/UserContext';

export const Checkout = () => {
  const { state: userState } = useUser();
  return (
    <div className={styles.container}>
      <h1 className={styles.title} data-notify={userState.counter}>
        Checkout
      </h1>
      <Total />
    </div>
  );
};
