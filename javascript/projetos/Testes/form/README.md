O validador criada, ira interromper o evento de *submit* e validar os dados para seguir o envio do Formulario.  
```javascript 
// B7Validator e um objeto com varias funções
let B7Validator = {
    handleSubmit:(event)=>{
        event.preventDefault(); // Para o evento.
        let send = true;

        let inputs = form.querySelectorAll('input'); // Lista todos inputs

        B7Validator.clearErrors(); // Limpa os error

        for(let i=0;i<inputs.length;i++) {
            let input = inputs[i];
            let check = B7Validator.checkInput(input);
            if(check !== true) { // Se nao retornar true, mudo send para false e exibe msg de erro.
                send = false;
                B7Validator.showError(input, check);
            }
        }

        if(send) { // Envia o Formulario se send continuar com o valor true.
            form.submit();
        }
    },
    checkInput:(input) => {
        let rules = input.getAttribute('data-rules'); // Verifica se aquele input tem alguma regra.

        if(rules !== null) {
            rules = rules.split('|'); // Cria um array, utilizando como separador o pipe "|"
            for(let k in rules) {
                let rDetails = rules[k].split('='); // Mais um split usando como separador o "=", para pegar os valores.
                switch(rDetails[0]) {
                    case 'required':
                        if(input.value == '') {
                            return 'Campo não pode ser vazio.';
                        }
                    break;
                    case 'min':
                        if(input.value.length < rDetails[1]) {
                            return 'Campo tem que ter pelo menos '+rDetails[1]+' caractes';
                        }
                    break;
                    case 'email':
                        if(input.value != '') {
                            let regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                            if(!regex.test(input.value.toLowerCase())) {
                                return 'E-mail digitado não é válido!';
                            }
                        }
                    break;
                }
            }
        }

        return true; // Caso nao tenha regra, retorna true direto.
    },
    showError:(input, error) => {
        input.style.borderColor = '#FF0000';

        let errorElement = document.createElement('div'); // Criando div
        errorElement.classList.add('error'); // Adicionando classe
        errorElement.innerHTML = error; // Adicionando mensagem de erro dentro do elemento.

        input.parentElement.insertBefore(errorElement, input.ElementSibling);
        // parenteElement, voltou um elemento, neste caso label, insertBefore = inseri antes,e inseri o elemento errorElement no input, usando o ElementSibling para aparecer depois invés de antes.
    },
    clearErrors:() => { // Limpa os Error
        let inputs = form.querySelectorAll('input');
        for(let i=0;i<inputs.length;i++) {
            inputs[i].style = '';
        }

        let errorElements = document.querySelectorAll('.error');
        for(let i=0;i<errorElements.length;i++) {
            errorElements[i].remove();
        }
    }
};

// Selecionando Classe `b7validator`
let form = document.querySelector('.b7validator');
// Bloquei no envio para analisar e validar dados.
form.addEventListener('submit', B7Validator.handleSubmit);
// Monitora quando ocorre um evento de submit e realiza uma ação
```
