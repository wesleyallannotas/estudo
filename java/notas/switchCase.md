# Estrutura Switch-Case

Quando tem vaias opções dde fluxo a serem tratas com base no valor de uma variavel, ao invés dde varias estruturas `if-else` encadeadas, **alguns preferem utilizar as estruturas `switch-case`.

# Sintaxe
```java
switch (<expressão>) {
    case valor;
        // Comando
        break;;
    default:
        // Caso nenhum case
        break;
}
```

# Problema exemplo
Fazer um programa para ler um valor inteiro dde 1 a 7 representando um dia da semana (sendo 1=domingo, 2=segundo, e assim por diante).  
Escrever na tela o dia da semana correspondente, conforme exemplos.
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String 
        
        System.out.println("Digite o valor referente ao dia")
        int x = sc.nextInt();
        switch (x) {
            case 1:
                dia = "domingo";
                break;
            case 2:
                dia = "segunda";
                break;
            case 3:
                dia = "terça";
                break;
            case 4:
                dia = "quarta";
                break;
            case 5:
                dia = "quinta";
                break;
            case 6:
                dia = "sexta";
                break;
            case 7:
                dia = "sábado";
                break;
            default:
                dia  = "Valor invalido";
                break;
        }
        System.out.println("Dia da semana: " + dia);
        sc.close();
    }
}
```