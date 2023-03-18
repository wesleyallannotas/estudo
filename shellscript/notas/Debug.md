# Debug

Tags: 🐞 Debug

# Padrão

Por padrão quando tem algum erro no nosso script o próprio shell exibi a linha e perto de qual comando esta, assim facilitando encontrar o erro

<aside>
⚠️ O problema e que ate o script cheguei no erro para exibir a mensagem, ele vai executar os comandos anteriores

</aside>

# Debug `bash -n`

E possivel testar o script em vez de executar de cara, usando o comando `bash -n script.sh` , assim percorrendo o script linha a linha sem executar e informando caso encontra erro

# Debug Manual

Por exemplo caso tenha um erro de logica nos mantendo preso em uma parte do script sem exibir mensagem de erro, assim podemos criar testes dentro do script para saber ate onde paramos.

> Depois podemos apenas comentar as linhas do test caso de certo.
> 

```bash
echo "[DEBUG] \$# = $#"
Comando
Comando
if [ test ]
then
	echo "[DEBUG] Entrei no if"
	Comando
	Comando
fi
```

# Debug `bash -x`

> Colocara um sinal de “+’ todo vez que executar um comando, quando tiver “++” e por que esta em um subshell
> 

# Debug `bash -v`

> Mostra antes o comando a ser executado e em seguida o resultado do comando
> 

# Debug `bash -xv`

> Utilizara o melhor dos dois comando resultando, uma pre visualização do código e em seguida ele sendo executado com os sinais de “+”
> 

# Debug dentro do script

> Debug dentro do código e definido um trecho onde quando executado o script em vez de realizar aquela parte do código naquela parte sairá um de debug sobre aquela parte
> 

Dentro do script iremos selecionar a partir de qual momento queremos realizar o debug e ali adicionaremos uma linha de comando `set -x`  ou `-xv` ou apenas `-v` e para terminar o debug utilizamos o mais(+) no lugar do menos(-) `set +x` ou `+xv` ou apenas `+v`

# Debug com execução passo a passo

Selecionaremos uma parte do texto onde o debug sera feito passo a passo, e iremos pressionando enter e ele executando parte por parte, ficando da seguinte forma dentro do nosso codigo

```bash
set -xv
trap read DEBUG # Comece a execusao passo a passo
Comando
Comando
if [ test ]
then
	Comando
	Comando
fi
trap "" DEBUG #Finalizando a execusao passo a passo
```