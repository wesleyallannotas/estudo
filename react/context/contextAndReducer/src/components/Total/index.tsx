import { TotalMessage } from '../TotalMessage';
import styles from './Total.module.css';

export const Total = () => {
  return (
    <div className={styles.container}>
      <div className={styles.containerTitle}>
        <h2 className={styles.title}>Total</h2>
        <p className={styles.money}>
          <span>R$</span> 100,00
        </p>
      </div>
      <TotalMessage />
    </div>
  );
};
