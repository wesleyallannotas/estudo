# Introdução

Entrada de dados e quando o **Usuário** informa dados para o programa, usando **dispositivos de Entrada**.  
Entrada de dados também e chamada de **Leitura**, pois o programa esta lendo dados.  

*Java* possui uma particularidade para entrada de dados, necessário a criação de um objeto de tipo *Scanner* da seguinte forma:  
```java
Scanner sc = new Scanner(System.in);
```
- Tipo da Variavel - Scanner
- Nome da Variavel - sc
- Forma de associar essa variavel com a entrada de dados padrão.

## Para funcionar

- Necessário importar a classe Scanner `import java.util.Scanner`
- faca `sc.close()` quando nao precisar mais do objeto `sc`

## Palavra

Texto sem espaços, suponha variavel tipo *String* declarada.
```java
String x;
x = sc.next();
```

## Valor inteiro.
```java
int x;
x = sc.nextInt();
```

## Valor com ponto flutuante.
```java
double x;
x = sc.nextDouble();
```
> Atenção: Para considerar separador de decimais como ponto. importar classe Locale e adicionar ao código `Locale.setDefault(Locale.US);` para deixar de utilizar a localidade do sistema como padrão e utilizar o padra US.

## Caractere especifico

Recebe como *String* e através do `charAt()` pega o carácter da string, por exemplo `charAt(0)` pega o primeiro carácter.
```java
char x;
x = sc.next().charAt(0);
```

## Ler texto ate **quebra de linha**

Quebra de linha seria a cada enter
> `next()` le apenas uma palavra.
```java
String x;
x = sc.nextLine();
```

### Quebra de linha pendente (ATENÇÃO)

```java
String s1,s2,s3;
int x;

x = sc.nextInt();
s1 = sc.nextLine();
s2 = sc.nextLine();
s3 = sc.nextLine();
```
Caso digita:
30 (aperte enter)
bom dia (aperte enter)
boa tarde (aperte enter)

Imprimira:  
30

Bom dia
Boa tarde

> Enter da uma quebra de linha, como demos enter para digitar o valor 30, ou seja, ficou pendente uma quebra de linha, quando passou para variavel `s1` ela consumiu a quebra de linha por isso a linha em branco

### Solução

Faca um `nextLine()` extra antes de fazer o `nextLine()` de seu interesse.
```java
String s1,s2,s3;
int x;

x = sc.nextInt();
sc.nextLine();
s1 = sc.nextLine();
s2 = sc.nextLine();
s3 = sc.nextLine();
```