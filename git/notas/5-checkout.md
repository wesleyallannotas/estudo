# `git checkout`

- Permite modificar temporariamente os arquivos do projeto ao estado de um dado commit ou branch
- Código do commit, **HEAD**
    - Cada commit possui um código, que pode ser utilizado para referenciar o commit
    - O ultimo commit do histórico do branch corrente também pode ser referenciado pela palavra **HEAD** usando `~N`, por exemplo:
        - `HEAD~1` - Penúltimo commit
        - `HEAD~2` - Antepenúltimo commit
- **Importante:** antes de fazer o checkout para voltar para HEAD, certifique-se de que não haja mudanças nos arquivos. Se você acidentalmente mudou alguma coisa, desfaça as modificações usando:
```bash
git reset           # Removo arquivos do stage
git clean -df
git checkout -- .   # Checkout para limpar modificações
```
> `git checkout` com o numero de identificação do commit na frente para mudar para tal commit, normalmente para se voltar a branch main/master de volta usando o nome dela `git checkout main`
>
> `git checkout` com o nome da branch muda para determinada branch