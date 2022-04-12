# Principais Diretórios do Sistema.

Tags: 📁 Diretórios

### /root

É o equivalente ao /home do usuário root, ou seja, o administrador da maquina

### /opt

Onde alguns arquivos de fora podem ser instalados

### /sbin

Ficam muitos binários do sistema operacional, shutdown, programas para gerenciar disco, chegar disco entre outros.

### /bin

Ficam outros programas do sistema(binários também) como o BASH e outros shells, chmod chown para mexer nas permissões dos arquivos, mkdir para criar diretorios entre outros.

### /usr

Significa (U)nix (S)ystem (R)esources, onde fica os programas que instalamos

/lib = Bibliotecas instalas

/src = Caso instala código fonte junto

/include = Instala pacotes -dev que traz os arquivos de header em c ou c++ para quando você precisa compilar dependências

Antigamente tinha o /etc para arquivos de configuração mas hoje em dia acaba ficando tudo no /etc de fora ou em diretórios escondidos como o .config no home

### /var

Contem dados variáveis

/log = logs do sistema

/mail = Para emails

/run = Tem os PID que são os ID dos processos sendo executados

/cache = serve para alguns caches do sistema

### /proc

Se usar o comando `ps` que lista os processos dos aplicativos que estão em execução, eles tem um ID numérico, dentro do proc esses processos são representados como diretórios, onde podemos fuçar ali

### /tmp

Onde fica arquivos temporários que o sistema não garante que estará na próxima inicialização