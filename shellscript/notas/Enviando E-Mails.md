# Enviando E-Mails

Tags: 📫 Mail

# Introdução

Muito utilizado em ambientes de produção e servidores, geralmente usado para notificar sobre acontecimentos, status entre outras possíveis funções de utilização

# `mail`

Sera utilizado o comando `mail` que e a forma mais comum de fazer esse envio, ele e um cliente de e-mail, pode ler mensagens internas do servidor, dos usuários internos e enviar mensagens SMTP (Necessário configurar um servidor de e-mail interno, postfix, sendmail)

<aside>
⚠️ Configurei o postfix para e-mail local, **preciso estudar configurar postfix** parece uma ferramenta interessante

</aside>

## Sintaxe básica para enviar e-mail

`mail -s "Assunto" destinatário < log.out`

`-s` - Subject, ou seja o assunto.

`destinatário` - e-mail ou caso seja interno apenas o nome do usuário.

`log.out` - Funciona como conteúdo do e-mail nao anexo, ou seja, vai pegar o conteúdo do arquivo

Assim logicamente concluímos que podemos mandar o conteúdo de qualquer arquivo via e-mail seguindo essa sintaxe.

### Pode ser usado com pipe “|”

Exemplo de uso vindo de um pipi - `echo "Teste de e-mail" | mail -s "testando mail" wesleydesktop@wesley.mail`

Assim e logico que com pipe podemos redirecionar qualquer resultado de um comando, podendo tratar, cortar fazer o que quiser e no fim via pipe mandar por e-mail.

## Aplicando comando `mail` dentro do script

Pratica muito utilizada e guardar o e-mail do destinatário dentro de uma variável e criar um arquivo dentro do `tmp`, ou seja, um arquivo temporário que durante o script era receber os logs, e no final mandar o log completo via mail e logo em seguida apagar esse arquivo temporário

```bash
#Variavel
ADMIN=wesley@wesley.mail

#Script
echo "$(date): Iniciando o Script" >> /tmp/msg_temp
Comando
Comando
Comando
Comando
Comando
echo "$(date): Script Finalizado" >> /tmp/msg_temp

#Enviando log
mail -s "Relatorio de Execusao do $0" $ADMIN < /tmp/msg_temp

#Apagando Arquivo Temporario
rm -f /tmp/msg_temp
```

### Utilizando variável para guardar log

Desta forma usamos o método de guardar o conteúdo do log dentro de uma variável separado por linhas então e necessário utilizar o `\n` que nada mais e do que a quebra de linha, em seguida executamos um `echo -e` a opção `-e` e necessário para executar as quebras de linhas. e via pipe esse resultado e enviado para o comando `mail` 

```bash
#Variavel
ADMIN=wesley@wesley.mail

#Script
CONTEUDO="$(date): Iniciando Script\n"
Comando
Comando
Comando
Comando
Comando
CONTEUDO="$CONTEUDO$(date): Fim do Sript\n"

#Enviando log
echo -e "$CONTEUDO" | mail -s "Relatorio do Script $0" $ADMIN
```

# Enviar e-mail via linha de comando

Existe algumas alternativas interessante ao `mail` para fazer esse trabalho algumas com opções ate mais interessante e que funciona melhor, os recomendados seria `mutt` e `sendemail` ambos possivel de instalar via apt.