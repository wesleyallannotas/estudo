# Variáveis no Shell

Tags:  💲 Variáveis, #️⃣ Comandos

# Introdução

Muitas variáveis são carregadas no momento do login, e ficam disponíveis para o usuário e para o sistema utilizar.

# Verificando Variáveis Carregada

Com o comando `env` podemos verificar as variáveis carregadas, por exemplo encontramos a variável do nossa home, a variável que diz o nosso shell entre outros.

## Diferença entre env e set

`set` - Exibe as variáveis locais e variáveis exportadas

`env` - Exibe as variáveis exportadas, ou seja, para uma variável que criamos aparecer no `env` e necessário executar o `export`

# Como Referenciar uma variável “$”

Por exemplo para ver o que tem dentro da nossa varivel home utilizamos o `echo $HOME` com o Cifrão e o nome da variável estamos chamando ela.

# Declarar variável no shell

`VARIAVEL1=Valor` tem que ser junto sem espaços para funcionar

# Lendo Variável

Agora para verificar a variável usamos o echo e o cifrão mais o nome da variável para chamá-la. `echo $VARIAVEL1` exibira o valor da variável, ou seja, exibira “valor”, variável com valor com espaços e caracteres especiais e necessário proteger com dupla aspas, ou aspas simples, ou barra invertida antes de cada carácter que necessita de proteção, `VARTEST=”Curso de Shell”`

<aside>
⚠️ Importante lembrar que Duplas aspas “” e aspas simples ‘’ possui diferença nos caracteres que elas protegem, na pratica aspas simples protege tudo ate mesmo o cifrão “$” que usamos para chamar a variável, ou seja, protegemos variáveis com aspas duplas.

</aside>

# Exportar Variável

Quando declaramos uma variável dessa forma, ela e uma variável locas, nao e vista por outros shell nem pro shells filhos apenas por nossa sessão atual, importante que para iniciar com o sistema teremos que adicionar nossa variável me arquivos específicos do sistema, agora se nossa objetivo e exportar a variável que criamos podemos simplesmente usar o comando `export` assim ficando visível para os shells filhos do nosso atual

E possivel declarar a variável já executando o export `export TEST=testando`

## Como colocar resultado de comandos dentro de variáveis

Por exemplo sera usado o comando date com a opção de mostrar apenas a hora atual que seria `date +%H` para colocarmos o resultado dentro de uma variável, sera necessário colocar o valor da variável com o comando entre crases assim ficaria `HORA=`date +%H`` ou temos como opção também o formato `HORA=$(date +%H)`