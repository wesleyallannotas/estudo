# Operadores de atribuição comutativa
Operadores  | Resultado
---         | ---
a += b;     | a = a + b;
a -= b;     | a = a -b;
a *= b;     | a = a * b;
a /= b;     | a = a / b;
a %= b;     | a = a % b;

## Problema exemplo
Uma operado de telefonia cobra R$ 50.00 por um plano básico que da direito a 100 minutos de telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para ler quantidade de minutos que uma pessoa consumia, dai mostra o valor a ser pago.
```java
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int minutos = sc.nextInt();

        double conta = 50.0;
        if (minutos > 100) {
            conta += (minutos - 100) * 2.0;
        }
        System.out.printf("Valor da conta = R$ %.2f%n", conta);

        sc.close();
    }
}
```