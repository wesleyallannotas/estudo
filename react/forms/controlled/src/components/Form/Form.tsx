import { useState } from "react";
import styles from "./Form.module.css";

const usernameValidator = (value: string) => {
  if (value.length > 3) return true;
  return false;
};

const emailValidator = (value: string) => {
  if (value.length > 5) return true;
  return false;
};

type InputState = {
  value: string;
  isValid: boolean;
  isTouched: boolean;
};

const initialInputState: InputState = {
  value: "",
  isValid: false,
  isTouched: false,
};

const Form = () => {
  const [username, setUsername] = useState<InputState>(initialInputState);
  const [password, setPassword] = useState<InputState>(initialInputState);

  return (
    <form method="POST" className={styles.container}>
      <fieldset className={styles.group}>
        <legend className={styles.legend}>Login</legend>
        <label className={styles.label} htmlFor="username">
          Username:
        </label>
        <input
          className={
            username.isTouched && !username.isValid
              ? styles.invalid + " " + styles.input
              : styles.input
          }
          type="text"
          name="username"
          id="username"
          value={username.value}
          onBlur={() => setUsername({ ...username, isTouched: true })}
          onChange={(e) =>
            setUsername({
              value: e.target.value,
              isValid: usernameValidator(e.target.value),
              isTouched: true,
            })
          }
        />
        <label className={styles.label} htmlFor="password">
          Password:
        </label>
        <input
          className={
            password.isTouched && !password.isValid
              ? styles.invalid + " " + styles.input
              : styles.input
          }
          type="password"
          name="password"
          id="password"
          value={password.value}
          onBlur={() => setPassword({ ...password, isTouched: true })}
          onChange={(e) =>
            setPassword({
              value: e.target.value,
              isValid: emailValidator(e.target.value),
              isTouched: true,
            })
          }
        />
      </fieldset>
      <button className={styles.button} type="submit">
        Login
      </button>
    </form>
  );
};

export default Form;
