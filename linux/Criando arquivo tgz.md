# Criando arquivo .tgz

Tags: #️⃣ Comandos, 👊 Compressão

# Comando usado

Para comprimirmos arquivos em tar.gz ou tgz, utilizamos o comando `tar` , diferente da compactação pelo comando `zip` onde e necessário a utilização do `-r` , ou seja, recursivo, para adicionar os subdiretórios, o comando `tar` por padrão já é recursivo.

Quando nos deparamos com arquivos do tipo `.tar.gz`, significa que dois processos ocorreram. O primeiro é o **empacotamento** dos arquivos no formato **`.tar`**. O segundo processo é a **compactação** no formato **gzip**.

O `tar` apenas une todos os arquivos em um só. Mas o `tar` não aplica algoritmos de compactação para que o arquivo resultante fique menor. Para isso utilizamos um outro formato, como o `gzip`.

A vantagem é que o `tar` consegue manter as permissões dos arquivos, bem como links diretos e simbólicos, sendo interessante por exemplo para realizar backups.

# Compactando arquivo

Comando usado para compactar o diretório desejado:

Compactando em `.tgz` 

`tar -cvzf nome_arquivo.tgz arquivo_ou_diretorio_a_ser_compactado`

Compactando em `.tar.gz` 

`tar -cvzf nome_arquivo.tar.gz arquivo_ou_diretorio_a_ser_compactado`

Onde:

`-c` : create a new archive

`-v` : verbosely list files processed

`-z` : filter the archive through gzip (indica que queremos compactar com gzip**)**

`-f` : use archive file or device archive (para que o comando crie o arquivo compactado)

<aside>
⚠️ Por padrão o `tar` é silencioso, ou seja, não e como o zip que imprimi mensagens sobre o processo, usamos o `-v` para ter esse feedback.

</aside>

# Descompactando arquivo

Para descompactar, basta utilizar o `-x` de extract no lugar do `-c`

`tar -xvzf nome_arquivo.tgz`

Para arquivo .`tar.gz`

`tar -xvzf nome_arquivo.tar.gz`