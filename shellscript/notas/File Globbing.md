# File Globbing

Tags: 📂 File Globbing

# Diferença File Globbing x Regex

Regex e expressão regular, o regex que conhecemos de todos as linguagens, tendo como função selecionar um padrão de texto.

File Globbing e uma forma do shell selecionar arquivos e diretório

File Globbing trabalha com arquivos, Regex trabalha com texto

## Asterisco “*”

Pode um nao ter algo no lugar do asterisco.

Asterisco onde ele estiver informa que no lugar dele pode ter qualquer string ou carácter, `*aula` qualquer arquivo que termine com aula `aula*` qualquer arquivo que inicie com aula, também podemos colocar asterisco antes de pois assim informando qualquer arquivo que tenha aula no meio do nome.

`ls -a Aula*` - Vai listar todos os arquivos que tem como inicio o nome Aula e pode ter qualquer coisa depois do asterisco.

## Colchetes [.]

Funciona como uma lista, onde colocamos os caracteres que aceitamos naquele espaço onde a lista de inicia.

`ls -l Aula[1234]` - Informamos qual caracteres queremos, ou seja, só exibira os arquivos que tiver o nome iniciado com Aula seguido com qualquer um dos caracteres que se encontra entre colchetes.

`ls -a Aula[12345]` ou `ls -a Aula[1-5]` - Duas formas validas de informar que queremos o arquivo com nome Aula seguido de um carácter entre 1 a 5

## Chaves {.}

Escolhemos as strings que queremos, por exemplo `ls -l {AULA, aula}` ele nao vai buscar apenas uma das string e sim as duas.

## Interrogação “?”

Interrogação exige que aja um caracater tem que ter apenas um e tem que ter.