import styles from "./Form.module.css";

const formValidation = (event: React.FormEvent<HTMLFormElement>) => {
  event.preventDefault();
  const form = event.currentTarget;
  const Inputs = [form.username, form.password];
  // const formData = new FormData(form);
  // const username = formData.get("username");
  // const password = formData.get("password");

  Inputs.forEach( input => {
    if (input.value !== "") {
      input.classList.remove(styles.error);
    } else {
      input.classList.add(styles.error);
    }
  })
};

const Form = () => {
  return (
    <form method="POST" className={styles.container} onSubmit={formValidation}>
      <fieldset className={styles.group}>
        <legend className={styles.legend}>Login</legend>
        <label className={styles.label} htmlFor="username">Username:</label>
        <input className={styles.input} type="text" name="username" id="username" />
        <label className={styles.label} htmlFor="password">Password:</label>
        <input className={styles.input} type="password" name="password" id="password" />
      </fieldset>
      <button className={styles.button} type="submit">Login</button>
    </form>
  );
};

export default Form;
