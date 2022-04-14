# Introdução

Aprendemos que uma **classe** possui membros, sendo eles, **atributos** e **métodos**.

# Membros Estáticos

- Também chamados de membros de classe
    - Em oposição a membros de instancia
- Sao membros que **fazem sentido independentemente de objetos**. **Nao precisão de objeto para serem chamados**. Sao **chamados a partir do próprio nome da classe**.
- Aplicações comuns:
    - Classes utilitárias (Exemplo: `Math.sqrt()`, `Math` e o nome da **classe** nao de um objeto.)
    - Declaração de constantes
- Uma classe que **possui somente membros estáticos, pode ser uma classe estática também**. Esta classe **nao poderá ser instanciada.**

# Problema Exemplo

Fazer um programa para ler um valor numérico qualquer, e dai mostrar quanto seria o valor de uma circunferência e do volume de uma esfera para um raio daquele valor, informar também o valor de PI com duas casas decimais.

## Versão 1: Métodos da própria classe do programa

> Nota: Dentro de um método estático voce nao pode chamar membros de instância da mesma classe.  
>
> `final` - **Informa que e um constante.**  
>
> **Padrão de nome para constantes e tudo maiúsculo**  
> Exemplo: AREA_TOTAL 
```java
package application;

import java.util.Locale;
import java.util.Scanner;

public class Program {

    public static final double PI = 3.14159;

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner;

        System.out.print("Enter radius: ");
        double radius = sc.nextDouble();

        double c = circumference(radius);
        double v = volume(radius);

        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n", v);
        System.out.printf("PI value: %.2f%n", PI);

        sc.close();
    }
    
    public static double circumference(double radius) {
        return 2.0 * PI * radius;
    }
    
    public static double volume(double radius) {
        return 4.0 * PI * radius * radius * radius / 3.0;
    }
}
```

## Versão 2 : Classe `Calculator` com membros de instancia

> Como os membros nao sao estáticos, se torna **obrigatório instanciar o objeto**
```java
// Classe Calculator
package util;

public class Calculator {
    public final double PI = 3.14159;

    public double circumference(double radius) {
        return 2.0 * PI * radius;
    }
    
    public double volume(double radius) {
        return 4.0 * PI * radius * radius * radius / 3.0;
    }
}

// Classe Program
package application;

import java.util.Locale;
import java.util.Scanner;
import util.Calculator;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner;
        Calculator calc = new Calculator();

        System.out.print("Enter radius: ");
        double radius = sc.nextDouble();

        double c = calc.circumference(radius);
        double v = calc.volume(radius);

        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n", v);
        System.out.printf("PI value: %.2f%n", calc.PI);

        sc.close();
    }
}
```

## Versão 3 : Classe `Calculator` com método estático.
> Nao e necessário criar um objeto calc, pois os membros sao estáticos
>
> Chamamos os membros através do nome da Classe.
```java
// Classe Calculator
package util;

public class Calculator {
    public static final double PI = 3.14159;

    public static double circumference(double radius) {
        return 2.0 * PI * radius;
    }
    
    public static double volume(double radius) {
        return 4.0 * PI * radius * radius * radius / 3.0;
    }
}

// Classe Program
package application;

import java.util.Locale;
import java.util.Scanner;
import util.Calculator;

public class Program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner;

        System.out.print("Enter radius: ");
        double radius = sc.nextDouble();

        double c = Calculator.circumference(radius);
        double v = Calculator.volume(radius);

        System.out.printf("Circumference: %.2f%n", c);
        System.out.printf("Volume: %.2f%n", v);
        System.out.printf("PI value: %.2f%n", Calculator.PI);

        sc.close();
    }
}
```

# Quando utilizar estático ou instancia

Por exemplo no problema do triangulo, cada triangulo possui sua area.  
`Area()` e uma **operação concernente** ao objeto, cada triangulo possui sua area  
Assim fica claro que a operação de instancia, pois **cada objeto** vai ter seu **comportamento especifico**.

Ja no caso da calculadora, os **valores dos cálculos nao mudam** para calculadores diferentes, ou seja, sao **cálculos estáticos** (Fixos, nao mudam), vale ressaltar que o valor de PI também e estático