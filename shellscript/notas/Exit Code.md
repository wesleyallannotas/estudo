# Exit Code

Tags: ❌ Exit Code

# Introdução

Todo shell script vai ter um código de saída, dando certo ou errado, esses códigos de saída vão de 0 - 255, 0 significa um sucesso e qualquer outro numero e equivalente a um erro especifico, para exibir esse Exit code no terminal basta digitar `$?` que ele exibira o exit code do comando anterior, mesmo dentro de um script o resultado que estará gravado dentro desse comando, sera o ultimo comando do shell script, ou seja, se o penúltimo der certo e o ultimo errado, dentro de `$?` estará o valor do erro.

## Usando no script

Com `exit` podemos interromper o scrpit e sair dele, se colocar um numero na frente ele ignora o que aconteceu de verdade caso deu erro ou nao e qual foi o erro, e ira guardar aquele valor como exit code

E possivel coloca dentro de uma variável `RETUR_CODE=$?`