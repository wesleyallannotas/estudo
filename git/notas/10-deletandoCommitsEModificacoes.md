# Como deletar commits e também modificações nos arquivos

Voltar o projeto ao estado de um dado commit (deletar commits e alterações posteriores a esse commit)
```bash
git status

git reset --hard <codigo do cimmit>
```

Voltando o projeto ao estado do penúltimo commit:
```bash
git status

git reset --hard HEAD~1
```