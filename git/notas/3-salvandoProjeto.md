# Salvar primeira versão de um projeto no github

Com ambient configurado:
- usuário: `git config --global user.name "Nome usuario"`
- email: `git config --global user.email "Ser email de cadastro do github"`
- Chave SSH: Gerada e configurada.

## Passo a Passo

```bash
git init    # Inicia o repositório Git
git add .   # Manda arquivos para area de Stage
git commit -m "Mensagem explicativa"    # Commit usando os arquivos so Stage
git remote add origin git@github.com:seuusuario/seurepositorio.git  # Associa repositório remoto com o local
git push -u origin master # Master caso seja o nome da branch principal
```
> `-u` salva referencia que apenas o `git push` redirecione para o`git push origin master`

### **(Opcional)** mudar o nome da Branch principal de `master` para `main`

```bash
git branch -M main
```

# Clonar repositórios

```bash
git clone git@github.com:seuUsuario/seuRepositorio.git # Usando SSH
git cline https://github.com/seuUsuaruio/seuRepositorio # Usando HTTPS
```