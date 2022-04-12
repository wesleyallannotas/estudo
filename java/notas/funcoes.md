# Funções

Representam um processamento que possui um significado
- Math.sqrt(double)
- System.out.println(String)

# Principais vantagens
- Modularização
- Delegação
- Reaproveitamento

# Dados de entrada e Saida
- Funções **podem** receber **dados de entrada** (parâmetros ou argumentos)
- Funções **podem ou nao** retornar uma Saida

> **Importante: Em orientação a objetos, funções em classes recebem o nome de "métodos"**

# Função ja conhecida
`public static void main(String[] args)` - função base de um arquivo *Java* executável.

# Sintaxe

- public - Disponível em outras **classes**
- static - Função possa ser chamada independente de se criar um objeto.
- int - **Tipo** de **dado retornado**
    - void - Quando a função executa uma ação mas nao retorna dado.
- (parametros) - Dentro dos parenteses os parâmetros que tal função ira receber.
    - Nome no parâmetro e ilustrativo, serve para referenciar dentro da função
- Entre chaves a logica da função 
```java
public static int nomeFuncao() {}
```

# Exemplo
```java
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter three numbers:");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int higher = max(a, b, c);
        showResult(higher);
        sc.close();
    }
    public static int max(int x, int y, int z) {
        int aux;
        if (x > y && x > z) {
            aux = x;
        } else if (y > z) {
            aux = y;
        } else {
            aux = z;
        }
        return aux;
    }
    public static void showResult(int value) {
        System.out.println("Higher = " + value);
    }
}
```