# Operadores bitwise

Operado | Significado
---     | ---
&       | Operação **E** bit a bit
\|      | Operação **OU** bit a bit
^       | Operação **OU-exclusivo** bit a bit

> Nao confundir com operado logico.  
> Diferença entre **OU** e **OU-exclusivo** e que **OU-exclusivo** nao da verdadeiro para dois verdadeiros (true).

**Normalmente utilizado em programação de baixo nível**

# Exemplo

Testar de o sexto bit do numero e positivo (true, 1).
```java
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //int mask = 32; // bit (0010000) Cada bit equivale a 2 pois e possível 0 ou 1.
        int mask = 0b00100000; //Pode pagar os 0 antes do primeiro 1 se quiser.
        int n = sc.nextInt();

        if ((n & mask) != 0) {
            System.out.println("6th bit is true!");
        } else {
            System.out.println("6th bit is false!");
        }
    }
}
```

> Java aceita declarar numero de forma binaria se iniciando com `0b`, ou seja, o numero 32 ficaria `0b00100000;