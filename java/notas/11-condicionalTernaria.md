# Expressão condicional ternaria

Estrutura opcional ao `if-else` quando se desejar decidir um **VALOR** com base em um condição

## Sintaxe

```java
(<condicao>) ? <valorSeVerdadeiro> : <valorSeFalso>
```
## Exemplos:
```java
(2 > 4) ? 50 : 80
// resultado: 80

(10 != 3) ? "Maria" : "Alex"
// resultado: "Maria"
```

```java
// Longo
double preco = 34.5;
double desconto;
if (preco < 20.0) {
    desconto = preco * 0.1;
} else {
    desconto = preco * 0.05;
}

// Simplificado
double preco = 34.5;
double desconto = (preco < 20.0) ? 0.1 : preco * 0.05;
```