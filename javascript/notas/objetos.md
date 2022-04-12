# Introdução
Similar a *array*, a diferença básica e que array e uma listagem numerada, e objeto e uma listagem nomeada.

# Sintaxe
Objeto e definido entre chaves, onde damos um nome da propriedade depois o valor.
```javascript
let carro = {
    nome:'fiat',
    modelo:'uno',
    peso:'800kg'
    ligado:false,
    ligar:function() {
        console.log("Ligando o"+this.modelo);
        this.ligado == true;
        console.log("vrum vrum");
    },
    acelerar:function() {
        if(this.ligado == true) {
            console.log("Riiiiiiihhhiii");
        }else {
            console.log(this.nome+" "+this.modelo+" nao esta ligado!");
        }
    }
}

console.log(carro['nome']);
// OU
console.log(carro.nome);
// Executando função ligar
carro.ligar();
```

# Entendendo o javascript
`document.getElementById('titulo').style.display = "block";`
document = objeto
getElementById = função dentro do objeto `document`, que me retorna um objeto
style = objeto dentro do objeto retornado
display = objeto dentro de display que alteramos o valor.
