USE AULA_EMPRESA;

-- Sintaxe
GRANT DIREITOS ON OBJETOS TO USUARIO;
-- Permissão usuario1
GRANT SELECT ON EMPREGADO TO usuario1;
-- Permissões usuario2
GRANT SELECT, UPDATE, DELETE, INSERT on EMPREGADO TO usuario2;

-- Sintaxe
REVOKE DIRETOS ON OBJETOS FROM USUARIO;
-- Revogando usuario1
REVOKE SELECT ON EMPREGADO FROM usuario1;
-- Revogando usuario2
REVOKE DELETE ON EMPREGADO FROM usuario2;