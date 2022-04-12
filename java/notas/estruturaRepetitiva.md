# `while` (enquanto)

**Estrutura de controle** que **repete** um bloco de comandos **enquanto** um **condicao** for verdadeira.  
Usado quando **nao** se sabe previamente a **quantidade de repetições** que sera realizado.  

## Sintaxe / Regra

- Regra:
    - `true` (verdadeiro) - Executa e volta.
    - `false` (falso) - Encerra o loop.
```java
while (<condicao>) {
    // Bloco de código.
}
```

## Exemplo
Programa que le números inteiros ate que um zero seja lido. Ao final mostra a some dos números lidos.
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x, total;

        total = 0;
        x = sc.nextInt();

        while (x != 0) {
            total += x;
            x = sc.nextInt();
        }
        
        System.out.printf("Total da soma: %.d", x);
        sc.close();
    }
}
```

# `for` (Para)

**Estrutura de controle** que **repete** um bloco de comandos **para** um certo **intervalo de valores**.  
Usado quando se **sabe** previamente a **quantidade de repetições**, ou o intervalo de valores.  
> Ótimo para fazer contagens seja progressiva ou regressiva

## Sintaxe / regra
```java
for (<inicio> ; <condicao> ; <incremento>) {
    // Bloco de comandos
}
```
- **Regas**
    - `inicio` - Executa somente na primeira vez
    - `condicao` - Para true (verdadeiro),executa e volta ; Para false (falso) Encerra o loop
    - `incremento` - Executa toda vez depois de voltar
> Incremento comumente utilizado `i++` e `i--`

## Exemplo
Programa que le um valor inteiro `N` e depois `N` números inteiros.  
Ao final, mostra a soma dos `N` números lidos.
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int qt, x, total;
        total = 0;

        System.out.println("Digite o numero de valor:");
        i = sc.nextInt();

        for (int i=0; i<qt; i++) {
            System.out.println("Digite um numero inteiro:");
            x = sc.nextInt();
            total += x;
        }
        System.out.println("Total:" + total);
        sc.close();
    }
}
```

# `do while` (Faca enquanto)

**Menos utilizada**, mas em **alguns casos** se encaixa **melhor** ao problema.  
O bloco de comando **executado pelo menos uma vez**, pois a **condicao verificada no final**  

## Sintaxe / Regra
```java
do {
    // Bloco de código
} while (<condicao>);
```
- **Regas**
    - `true` (verdadeiro) - Volta e executa novamente
    - `false` (falso) - Encerra o loop (Lembrando que executara pelo menos uma vez
    )

## Exemplo
Fazer um programa para ler uma temperatura em Celsius e mostrar o equivalente em
Fahrenheit. Perguntar se o usuário deseja repetir (s/n). Caso o usuário digite "s", repetir o programa.

$$
F = 9C/5+ 32
$$

```java
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    Locale.setDefault(Locale.US);
    Scanner sc = new Scanner(System.in);

    char resp;
    do {
        System.out.print("Digite a temperatura em Celsius: ");
        double C = sc.nextDouble();
        double F = 9.0 * C / 5.0 + 32.0;
        System.out.printf("Equivalente em Fahrenheit: %.1f%n", F);
        System.out.print("Deseja repetir (s/n)? ");
        resp = sc.next().charAt(0);
    } while (resp != 'n');

    sc.close();
    }
}
```