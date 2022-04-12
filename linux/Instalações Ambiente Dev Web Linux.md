# Instalações Ambiente Dev Web Linux

Tags: 🗃️ Dotfiles

- **Sumario**

# Pacotes Instalados em Ordem.

1. build-essential
2. default-jdk
3. libssl-dev
4. exuberant-ctags
5. ncurses-term
6. ack-grep
7. silversearcher-ag
8. fontconfig
9. imagemagick
10. libmagicwand-dev
11. software-properties-commo
12. git
13. vim-gtk3
14. curl
15. ubuntu-restricted-extras (Codecs para videos)
16. dirmngr (Dependência asdf-nodejs)
17.  gpg (Dependência asdf-nodejs)
18.  gawk (Dependência asdf-nodejs

## Instalando

Iniciando as instalações no nosso ambiente dev, iniciamos com a instalação dos seguintes repositórios.

`sudo apt install build-essential default-jdk libssl-dev exuberant-ctags ncurses-term ack-grep silversearcher-ag fontconfig imagemagick libmagickwand-dev software-properties-common git curl`

# ASDF

Importante: Durante a instalação do ASDF e necessário adicionar uma linha de comando em um arquivo especifico dependendo o shell usado, apos isso e necessário da source nesse arquivo

Instalamos através de plugins do ASDF.

ruby, nodejs(necessário instalar dependências), golang, erlang(necessário instalar dependências), elixir, kotlin, rust, crystal

# Bancos de Dados

`sudo apt -y install postgresql-13 postgresql-contrib postgresql-server-dev-13 redis-server libhiredis-dev memcached libmemcached-dev`

Instalamos o postgres, redis, memcached

Um banco relacional descente, um nosql descente que faz p mínimo que precisamos, e um cache para quando não precisamos do redis como banco

## Importante uso do comando service

Tanto mongoDB, Postgresql, Redis, memcached, ate mesmo o docker vem com daemons que pode carregar sozinho depois do boot do sistema se tiver bastante memoria sobrando deixa ativado, caso não seja o caso, para derrubar ou restartar basta usar o comando service

Exemplo = `sudo service mongod stop` Para

`sudo service mongod restart` Reinicia

`sudo service mongod status` Mostra o status

`sudo service mongod disable` não carrega automaticamente apos o boot, assim sera necessário dar start toda vez que for utilizar

Através do usando o  `cat /etc/init.d/nomepastadobanco` por exemplo no caso do redis `cat /etc/init.d/redis-server` assim mostrara todos os comandos e o que ele faz quando e chamado.

Podemos usar `sudo /etc/init.d/redis-server status` para mostrar o status porem e bem mais simples utilizar o service.

# Instalando o Docker

Seguindo as instruções do site.

Ele cria um grupo de usuários chamado Docker e o usuário que vai gerenciar o docker que é o meu próprio, precisara estar nesse grupo.

Comandos = `sudo usermod -aG docker $USER` ($USER e o nosso usuário) (Necessário reboot)

Se tudo deu certo quando usarmos o comando `docker run hello-world` ele vai baixar a imagem de docker de uma aplicação que so imprime hello

### Configurando postgres com Docker

URL do tutorial = [https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198](https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198)

Citação interessante do site

> Desde o advento do Docker, raramente me encontro instalando software de desenvolvimento diretamente em minha máquina local. Sejam servidores de banco de dados (ou seja, Postgres), sistemas de cache (ou seja, Redis, Memcache) ou sistemas de mensagens (ou seja, Kafka) - quase sempre tento encontrar ou construir uma imagem docker apropriada para usar durante o desenvolvimento
> 

## Importe

Aprender usar docker compose para poder criar um mini cluster de containers que conseguem acessar uns aos outros.

# Criando Chave publica e privada.

Com criptografia assimétrica se usa de duas chaves, uma publica que iremos disponibilizar e uma secreta que no caso seria a chave privada, tudo que for criptografada pela chave privada só pode ser aberta pela publica e vice versa, ou seja, o que é criptografada por uma chave não pode ser aberta pela mesma, precisa da outra.

Existe alguns serviços que só funciona com o cadastro da sua chave publica exemplo github, gitlab, amazonaws, googleclound, azure entre outros.

Criando as chaves no nosso Linux

A maioria dos tutoriais vai mandar criar uma chave com algoritmo RSA, mas hoje em dia preferimos usar a ed25519 por ser mais segura

Comando = `ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/id_ed25519 -C “wesley.allansilva@gmail.com”`

Pedira umas passphrase, ou seja, uma frase secreta que você não vai esquecer.

Apos inserirmos a frase, ele criara dois arquivos

`~/.ssh/id_ed25519` = Contem chave secreta

`~/.ssh/id_ed25519.pub` = contem chave publica

Usando o comando cat antes do caminho a te o arquivo podemos ver o conteúdo.

## Dica para não precisar ficar digitando a frase secreta toda hora.

Comando = `ssh-add ~/.ssh/id_ed25519`

## Caso perder a chave privada

Gerar outro par e substituir todos os lugares a chave publica, pois quem tem a chave privada, tem acesso a tudo que você tinha acesso.

# tmux

tmux é um multiplexer de terminal, ou seja, você ganha a capacidade de ter múltiplas sessões de terminal, dentro de um único terminal, tmux são terminais virtuais, inicia com o comando `tmux` 

De inicio não tera nada demais, parecera um terminal normal.

Porem utilizando CRTL+B depois % = Abrira um terminal ao lado

CRTL+B  funciona como prefixo, apertamos ele depois um comando

CRTL+B  e depois CRTL+o navegas entre as janelas.

CRTL+B e Depois “ divide a tela em outra direção ao contrario do %.

Se fecharmos de uma vez o terminal e abrirmos de novo, basta utilizar o comando `tmux ls` que ele lista as sessões, assim com o comando `tmux attach-session -t numerosessao`  (Numero da sessão e o numero antes dos dois pontos)

Caso precisar se conectar via ssh em um servidor remoto e vai fazer algo que vai demorar abra o tmux primeiro se por acaso der pau na maquina local ou na usa conexão por alguma razão, você não vai perder nada que estava fazendo no servidor, basta reconectar quando puder e dar attach na session que ainda vai estar ativa.

## Fechando uma sessão

Se quiser mesmo fechar tudo que estava aberto em um sessão, basta usar o comando `tmux kill-session -t numerosessao`

# Instalando Codecs de Vídeo

`sudo apt install ubuntu-restricted-extras`

Os codecs de H264, mp3 e outros não são free softwares, então e necessário habilitar o que o ubuntu chama de repositórios restritos que faremos isso com o comando `c` Estes repositórios são considerados restritos pois na instalação base vem tudo que é código aberto, que é parte da filosofia do mundo de software livre que incita que deve boicotar tudo que não é código aberto ou usa licenças que não são de software livre.

# Google ou a versão aberta chromium

Pois com o desenvolvimento web é necessário ter certeza que nosso site funcionara corretamente no chrome ainda mais hoje que todos usam distribuições baseadas em chrome como navegador padrão.

Todas as ferramentas que usamos em nosso ambiente de desenvolvimento pode utilizar remotamente em um servidor via ssh.