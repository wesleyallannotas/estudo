# Loop For

Possível o uso de *for loop* e *for loop array*  

## Sintaxe *For Loop*

1. Criação de Variável Auxiliar  
   >Normalmente nomeada com uma letra apenas. (Geralmente `i`), responsável por ditar quantas vezes o código ira rodas.
2. Condição de parada
3. Incrementação da variável auxiliar.


```javascript
for(let i = 0; i < 50; i++) {
    
}
```

## Sintaxe *For Loop Array*

Roda o código em relação a quantidade de itens que tem no *array*

1. Criação de Variável Auxiliar  
    >Normalmente nomeada com uma letra apenas. (Geralmente `i`), responsável por ditar quantas vezes o código ira rodas.
2. *Array*

```javascript
let carros = ['Ferrari', 'Fusca', 'Palio', 'Corolla'];

for(let i in carros) {
    console.log(carros[i]);
}
```
> A variavel auxiliar recebe o valor do item da array, no caso acima o nome dos caros, por isso usando ela no console exibira o nome dos carros.

# Loop While
*while* significa enquanto, ou seja, enquanto a condição que colocarmos for satisfeita, rodara o loop

## Sintaxe

```javascript
let c = 1;
while(c < 10) {
    console.log(c);
    c++;
}
```