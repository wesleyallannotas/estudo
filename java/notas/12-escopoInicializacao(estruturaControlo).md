- **Escopo de uma variavel** - E a região do programa onde a variável e valida, ou seja, onde ela pode ser referenciada
- **Inicialização variavel** - Uma variavel nao pode ser usada se nao for iniciada
- **Escopo de métodos em outro arquivo**

Caso variavel seja declarada porem **nao inicializada** exibira erro, pois como citado acima a variavel tem que ser iniciada.

# Exemplo escopo

Variavel com escopo dentro da condicao if
```java
public class program {
    public static void main(String[] args) {
        double price = 400.00;

        if (price < 200.00) {
            double discount = price * 0.1;
        }
        
        System.out.println(discount);
        // resultado: Error, pois o escopo da variável se limita a dentro da condicao "if"
    }
}
```
> Toda estrutura tem seu escopo

## Resolvendo problema

```java
public class program {
    public static void main(String[] args) {
        // Inicializando fora.
        double price = 400.00;
        double discount = 0;

        if (price < 200.00) {
            discount = price * 0.1;
        }
        
        System.out.println(discount);
    }
}
    //  Vale se atentar que a variavel foi iniciada recebendo o valor de 0, caso nao fosse iniciada fora da estrutura `if` também exibiria erro

    // Inicializando dentro
public class program {
    public static void main(String[] args) {
        double price = 400.00;
        double discount;

        if (price < 200.00) {
            discount = price * 0.1;
        } else {
            discount = 0;
        }
        
        System.out.println(discount);
    }
    // O compilador e inteligente o suficiente para entender a inicialização dentro da estrutura.
}
```
.