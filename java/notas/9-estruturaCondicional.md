# Expressões Comparativas

Compara algo e retorna um *Boolean*

## Operadores Comparativos

Operador    | Significado
---         | ---
\>          | Maior
<           | Menor
\>=         | Maior **ou** igual
<=          | Menor **ou** igual
==          | Igual
!=          | Diferente
> "=" Atribuição "==" Comparador Igual

## Exemplo

```java
int x = 5;

x > 10; // resultado: false
x < 10; // resultado: true
x == 10; // resultado: false
x <= 10; // resultado: true
x >= 10; // resultado: false
```

# Expressões Logicas

Assim como expressões comparativas retorna um *Boolean*

## Operadores Comparativos

Operador    | Significado
---         | ---
&&          | **E**
\|\|        | **OU**
!           | **NAO**
- **E** - Todos Condições Verdadeiros
- **OU** - Pelo Menos Uma Condição Verdadeira
- **NAO** - Inverte a Condição


## Exemplo

```java
int x = 5;

x <= 20 && x == 10; // resultado: false
x <= 20 || x == 10; // resultado: true
!(x == 10);         // resultado: true;
!(x == 10 && x <= 20); // resultado true;
```

# Estrutura Condicional

**Estrutura de controle** onde executa determinado bloco de comando a partir de uma **condicao**.

# Sintaxe

## Simples:
**se** a **condicao** retornar verdadeira (true) executa o bloco de código, se nao pula.
```java
if (<condicao>) {
    // bloco de código
}
```
## Composta:
```java
if (<condicao>) {
    // Bloco de Código para true
} else {
    // Bloco de Código para false
}
```

## Encadeamento de estruturas condicionais
```java
if (<condicao>) {
    // Bloco de código para true
} else {
    if (<condicao>) {
        // Bloco de Código para true
    } else {
        // Bloco de Código para false
    }
}
```
> Possível simplificar o código subindo o "if" para frente do "else"

### Exemplo
```java
hora = sc.nextInt();

if (hora < 12) {
    System.out.println("Bom dia");
} else if (hora < 18) {
        System.out.println("Boa Tarde");
        } else {
        System.out.println("Boa Noite");
        }
```