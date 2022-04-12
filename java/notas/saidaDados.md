# Exibir um texto qualquer

## Sem quebra de linha ao final:
```java
System.out.print("Bom Dia!")';
```

## Com quebra de linha ao final:
```java
System.out.println("Bom dia!");
```

## Formatado
`printf` por padrão pega o formato do sistema que o esta utilizando (Padrão do Brasil e virgula) para mudar para ponto e necessário a mudança do `Locale`
```java
double x = 10.35784;
System.out.printf("%.2f%n",x);
```
`%.2f` - Informa que quer delimitar duas casas decimais (Por padrão arredondara o numero, e adiciona virgula(,) como separador)     
`%n` - Quebra de linhas:

# Alterando `Locale`
`Locale` e uma classe (class) que ja vem no JDK, ou seja, e necessário que seja importada (import)
```java
import java.util.Locale;

// Dentro da Classe
Locale.setDefault(Locale.US);
```

# Concatenar
Regra geral para `print` e `println`  
elemento1 + elemento2 + elemento3 + ... + elementoN  
```java
System.out.println("RESULTADO = " + x + " METROS");
```

## Usando `printf`
Regra geral para `printf`  
"TEXTO1 %f TEXTO2 %f TEXTO3", variavel1, variavel2"  
`%f` - Ponto flutuante  
```java
System.out.printf("RESULTADO = %.2f Metros%n", x);
```
Adicionando na ordem as variáveis.

```java
String nome = "Maria";
int idade = 31;
double renda = 4000.0;
System.out.printf("%s tem %d anos e ganha R$ %.2f reais%n", nome, idade, renda);
```
- `%f` - Ponto Flutuante
- `%d` - Inteiro
- `%s` - Texto
- `%n` - Quebra de linha