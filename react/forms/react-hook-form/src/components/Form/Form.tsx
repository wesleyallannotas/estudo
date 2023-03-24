import { useForm, SubmitHandler } from "react-hook-form";
import styles from "./Form.module.css";

const onSubmit: SubmitHandler<Data> = (data) => console.log(data);

type Data = {
  username: string;
  password: string;
};

const Form = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Data>({
    mode: "all",
    delayError: 150,
  });

  // console.log(watch("username"));
  // console.log(watch("password"));

  return (
    <form
      method="POST"
      className={styles.container}
      onSubmit={handleSubmit(onSubmit)}
    >
      <fieldset className={styles.group}>
        <legend className={styles.legend}>Login</legend>
        <label className={styles.label} htmlFor="username">
          Username:
        </label>
        <input
          className={styles.input}
          id="username"
          {...register("username", {required: true, minLength: 3, maxLength: 20, pattern: /^[A-Za-z]+$/i, validate: (value:string) => value !== "admin" || "Nice try!"})}
        />
        {errors.username && (<span className={styles.error}>{errors.username.message || 'username is required'}</span>)}
        <label className={styles.label} htmlFor="password">
          Password:
        </label>
        <input
          className={styles.input}
          id="password"
          { ...register("password", { required: true, minLength: 5, maxLength: 20, validate: (value:string) => value !== "admin" || "Nice try!"}) }
        />
        {errors.password && (
          <span className={styles.error}>{errors.password.message || 'password is required'}</span>
        )}
      </fieldset>
      <button className={styles.button} type="submit">
        Login
      </button>
    </form>
  );
};

export default Form;
