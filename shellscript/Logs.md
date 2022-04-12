# Logs

Tags: 📃 Log

- **Sumario**

# Introdução

Existem varias formas de se criar logs, des de simples a complexas vai variar da complexidade do nosso script, quanto mais complexo e mais interessante fazer um log mais completo

# Criando Log Simples

Podemos redirecionar a saída de sucesso com o sinal de maior `>` assim criando um log com o comando `./scripname.sh > log.ou` Porem com esse comando estamos redirecionando apenas a saída de sucesso para redirecionar a saída de erro adiciona o 2 antes do sinal de maior,

## Redirecionamento de Saída

Podemos redirecionar para arquivos diferentes a saída do nosso comando ou script, ficando da seguinte forma

`(ExecScript ou Comando) > log.out 2> errolog.out`

Para concatenar e **não apagar log anteriores** e necessário utilizar duplo sinal de maior

`(ExecScript ou Comando) >> log.out 2>> errolog.ou`

Redirecionar para o mesmo **arquivo** da **mesma forma** (Concatenar ou sobrescrever)

`(ExecScript ou Comando) >> log.out 2>&1`  Informando para redirecionar a saída de erro igual a saída de sucesso

### Problema com redirecionamento de saída

Redirecionando desta forma a mensagem de sucesso ou de erro nao sera exibida, assim sendo obrigado a consultar o log para ter acesso ao resultado.

## Redirecionando com `tee`

Cria o log e exibe o resultado, Podemos usar apenas com `tee` ou `tee -a` a diferença e que sem a opção  ele vai sobrescrever o arquivo ou seja igual a um sinal de maior, já com a opção `-a` ira concatenar no arquivo, ou seja, manter a logo anterior e adicionar o novo. 

<aside>
⚠️ Usando `tee`  alem de criar o log exibe o resultado do comando na tela.

</aside>

Redirecionando `(ExecScript ou Comando) | tee -a log.ou`

## Redirecionamento de Saída ou `tee`

Usamos redirecionamento de saída `>` `>>` quando nao queremos que exiba nada na tela, e usamos `tee` quando queremos exibir e ao mesmo tempo registar no log

# Criando Log dentro do Script

Uma ideia interessante e criar redirecionamentos para o log dentro do script, por exemplo a data e a hora de execução do script como no exemplo a baixo.

```bash
# Criar uma variavel para nao escrever o caminho toda hora
LOG="$HOME/Dev/Logs/log_interno.out"

# Script
echo "$(date) - Iniciando o Script" >> $LOG
comando qualquer
comando qualquer
comando qualquer
echo "Texto qualquer" | tee -a $LOG
comando qualquer
comando qualquer
comando qualquer
echo "$(date) - Fim do Script" >> $LOG
```

# Redirecionando de Saída Dentro do Script

Podemos fazer o redirecionamento de saí dentro do script através do `exec`

> Evita de toda hora que for executar o script ter que redirecionar a saída `(ExecScript ou Comando) >> log.out 2>&1`, iremos executar esse redirecionamento dentro do script
> 

<aside>
⚠️ Em linha de comando podemos omitir o 1 antes do sinal de maior para redirecionar de sucesso, com o `exec` **nao omitimos**

</aside>

```bash
# Criar uma variavel para nao escrever o caminho toda hora
LOG="$HOME/Dev/Logs/log_interno.out"

exec 1>> $LOG
exec 2>&1 # Informa que o redirecionamento da saida 2(erro) vai ser igual a saida 1(sucesso)

# Script
comando qualquer
comando qualquer
comando qualquer
comando qualquer

```

### Usando `exec` com `tee`

Com o `exec` nao e apenas usar o pipe para redirecionar para o próximo comando, neste caso temos que utilizar [**Process Substitution](http://tldp.org/LDP/abs/html/process-sub.html)** ficando da seguinte forma dentro do script `exec 1>> >(tee -a "$LOG")` , Basicamente a saída do comando `exec 1>>` sera redirecionada para o comando `tee -a “$LOG”` , Substituição de comando.

# Usando gerenciador de log do Linux

E possivel configurar o script para gerar log que serão administrados pelo gerenciador de logs do Linux

## rsyslog

Podemos ver as configurações como **root** entrando em `/etc/rsyslog.d/50-default.conf`

> Se olharmos no arquivo veremos * no campo destinado a priority, lembrando que em ordem e `facility.priority` o asterisco(*) representa todos.
> 

<aside>
⚠️ Pode variar um pouco entra as distribuições

</aside>

### Facility (O criador da mensagem)

**Sistema interno do linux** = auth, authpriv, cron, daemon, kern, lpr, mail, mark, news, security (same as auth), syslog, user, uucp

**Administrador e Usuários** = local0 ate local7

### Priority (Urgência/Importância da Mensagem)

**Em ordem crescente de criticidade** = debug, info, notice, warning, warn (same as warning), err, error (Same as err), crit, alert, emerg, panic (Same as emerg) 

### Criando config para scripts

> Para os nossos Sripts vamos fazer uma configuração e ao invés de usar um facility interno usaremos os destinados ao Adm e Users.
> 

Dentro do diretório `/etc/rsyslog.d` o rsyslog lê todos esses arquivos então pode ser criado um arquivo nesse diretório para configurar o log dos scripts, no caso criei scripts.conf

Dentro do arquivo adicionei a linha `local0.*   /var/log/scripts.log` ou seja, vou gerar um log dentro do `/var/log/` para tudo quer for associado ao facility local0 (Pode ser o diretório que quiser eu escolhe esse)

<aside>
⚠️ Necessário reiniciar rsyslog apos alterar configurações, para reiniciar `systemctl restart rsyslog` através do comando `ps axu | grep rsyslog` podemos conferir através da data se foi reiniciado

</aside>

### Criando arquivo manualmente

Não e necessário o rsyslog já cria, porem se achar necessário pode criar, dentro do diretório podemos criar o arquivo através do comando `touch` 

Acertando as permissões, no caso deixarei igual as permissões do arquivo syslog através do comando `chown syslog:adm nomescript.log`

## logger

> `logger` vai obter alguns parâmetros e vai jogar os logs para o syslog tratar
> 

Exemplo de teste do comando `logger -p local0.err "Teste Mensagem de Erro"`  estou mandando uma mensagem para o syslog através do `logger` depois informamos que o facility `local0` esta mandando uma mensagem com a priority `err` e em seguida a mensagem, no nosso caso uma mensagem de teste.

Sera escrito dentro do arquivo: `Jan 30 12:56:36 wesleypc wesleydesktop: Teste de Mensagem de Erro`

<aside>
⚠️ E possivel criar diferentes arquivos para diferentes priority por exemplo um log para os `debug` e um log para os `err` Para fazer isso basta informar na configuração, vale lembrar que no exemplo assim colocando o asterisco(*) escolhemos todos, ou seja, todo tipo de priority vai para o mesmo arquivo.

</aside>

### Colocando tags para facilitar busca

Podemos colocar tags no `logger` com a propriedade `-t`  **basicamente sera substituído o nome do usuário pela tag digitada.**

Exemplo de teste `logger -p local0.err -t [tag] "Testando o Uso de Tag"`

Sera escrito dentro do arquivo: `Jan 30 13:06:50 wesleypc [tag]: Testando o Uso de Tags`

### Como usar dentro do script

Vamos usar o comando `logger`

```bash
# Forma 1, Pegand saida de um comando
echo "Iniciando Script" | logger -p local0.warn -t [$0]
# Forma 2, Direta
logger -p local0.warn -t [$0] "Iniciando Script"

# Script
comando qualquer
comando qualquer
comando qualquer
comando qualquer

```

<aside>
❓ Dentro do shell script e sabido que cifrão($) que e usado para chamar uma variável seguido de um numero, são os paramentos digitados na execução do script, são registrados a partir do `$1` , porem o `$0` traz o que digitamos para executar o script, por exemplo se estiver no diretório do script `./nomescript` se estiver na diretório anterior `./diretorio/nomescript.sh` e assim por diante.

</aside>

### Usando `logger` com `tee`

Caso queria usar o resultado de um comando do script que ira aparecer na tela, e ao mesmo tempo que ele deve aparecer você quer registrar via logger, então teremos que utilizar o `tee`

```bash
# Script
sort "~/arquivos/alunos.txt" | tee -a >(logger -p local0.warn -t [$0])
```