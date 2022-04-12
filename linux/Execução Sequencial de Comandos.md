# Execução Sequencial de Comandos

Tags: #️⃣ Comandos

# Pipe “|”

Pega a saída do comando anterior e joga como entrada do próximo comando

Exemplo

`cat alunos.txt | grep andre`

# Sequencial com “;”

Executa um comando de cada vez em sequencia escrita

Exemplo

`date ; echo Linux ; ls -a`

São executados de forma independente, caso algum comando de errado, na vez dele só ira aparecer uma imagem de erro e continuara a sequencia.

# Sequencial com “&&”

Com o uso do e comercial “&” ele só ira executar o próximo comando caso o atual de certo, diferente do “;” que segue a sequencia sem interromper.

Exemplo 

`cat aluno.txt && echo Linuz`

# Sequencial com “||”

Com o uso de duplo pipe, só executa o segundo comando se o primeiro der errado.

Exemplo

`cat aluno2.txt || echo erro`

Executara o comando echo apenas se o comando cat de erro, por exemplo nao existir esse arquivo.

# Comando entre parenteses ()

Como se cria-se um sub shell, executa-se o comando depois volta a resposta para nosso shell atual, por exemplo quero o `ls` do meu diretório anterior porem quero continuar do meu diretório ficaria.

`( cd .. ; ls -l )` - Traz o resultado como se eu realiza-se o comando porem eu nao sai do meu diretório atual.