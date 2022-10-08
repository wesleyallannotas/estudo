USE AULA_EMPRESA;

-- Sintaxe
SELECT * FROM EMPREGADO;
SELECT * FROM EMPREGADO WHERE NUMERO_SEGURO_SOCIAL = NULL;
SELECT CODIGO, NOME FROM DEPENDENTE WHERE CODIGO= 5;
SELECT CODIGO, NOME FROM DEPENDENTE ORDER BY CODIGO;

SELECT NOME as 'Nome', NUMERO_SEGURO_SOCIAL as 'Seguro Social' 
FROM EMPREGADO
WHERE NUMERO_SEGURO_SOCIAL = 745;

SELECT *
FROM EMPREGADO
ORDER BY NUMERO_SEGURO_SOCIAL DESC;

SELECT NOME AS 'Nome', NUMERO_SEGURO_SOCIAL AS 'Seguro Social', SEXO AS 'Sexo', DATA_NASCIMENTO AS 'Data de Nascimento'
FROM EMPREGADO
WHERE NUMERO_DEPTO = 30 OR NUMERO_DEPPROJETO_ibfk_1TO = 25
ORDER BY SEXO DESC, NOME ASC;

SELECT *
FROM EMPREGADO
WHERE (SEXO = 'F' AND NUMERO_DEPTO = 30)
OR (SEXO = 'M' AND NUMERO_DEPTO = 31);

SELECT * FROM EMPREGADO
WHERE BAIRRO = 'Centro' AND RUA LIKE 'Rua%';

SELECT * FROM EMPREGADO
WHERE DATA_NASCIMENTO >= '2000-01-01' AND DATA_NASCIMENTO <= '2020-12-31';
-- Melhor Forma
SELECT * FROM EMPREGADO
WHERE DATA_NASCIMENTO BETWEEN '2000-01-01' AND '2020-12-31';

-- Para comparar com nulos se usa o IS
SELECT * FROM EMPREGADO WHERE NUMERO_SEGURO_SOCIAL_SUPERVISOR IS NULL;

-- Para comparar com nulos se usa o IS
SELECT * FROM EMPREGADO WHERE NUMERO_SEGURO_SOCIAL_SUPERVISOR IS NULL;
SELECT * FROM EMPREGADO WHERE NUMERO_SEGURO_SOCIAL_SUPERVISOR IS NOT NULL;

-- Elimina os iguais
SELECT DISTINCT BAIRRO FROM EMPREGADO;

-- União
SELECT NOME, DATA_NASCIMENTO FROM EMPREGADO
UNION
SELECT NOME, DATA_NASCIMENTO FROM DEPENDENTE
ORDER BY 1; -- Ordenar pela primeira coluna (no caso nome)

-- Funções Agregadas
/*
count: Contagem
max: Maior Valor
min: Menor valor
avg: Media
sum: Soma
*/

SELECT MIN(DATA_NASCIMENTO) FROM EMPREGADO;
SELECT MAX(DATA_NASCIMENTO) FROM EMPREGADO;
SELECT COUNT(NUMERO_SEGURO_SOCIAL) FROM ASSALARIADO;
SELECT AVG(SALARIO) FROM ASSALARIADO;
SELECT SUM(SALARIO) FROM ASSALARIADO;

SELECT NUMERO_DEPTO as 'Departamento', COUNT(*) as 'Funcionarios'
FROM EMPREGADO
GROUP BY NUMERO_DEPTO;

SELECT NUMERO_SEGURO_SOCIAL, COUNT(*) AS 'Quantidade'
FROM DEPENDENTE
GROUP BY NUMERO_SEGURO_SOCIAL
ORDER BY Quantidade;

SELECT NUMERO_DEPTO, COUNT(SEXO) AS 'QUANTIDADE_MULHERES'
FROM EMPREGADO
WHERE SEXO = 'F'
GROUP BY NUMERO_DEPTO
ORDER BY QUANTIDADE_MULHERES DESC;

SELECT NUMERO_SEGURO_SOCIAL, COUNT(*)
FROM DEPENDENTE
GROUP BY NUMERO_SEGURO_SOCIAL
HAVING COUNT(*) > 2
ORDER BY NUMERO_SEGURO_SOCIAL DESC;

-- `in`
SELECT NUMERO_SEGURO_SOCIAL, NOME, DATA_NASCIMENTO
FROM EMPREGADO
WHERE NUMERO_SEGURO_SOCIAL IN (SELECT NUMERO_SEGURO_SOCIAL FROM ASSALARIADO);

SELECT NUMERO_SEGURO_SOCIAL, NOME, DATA_NASCIMENTO
FROM EMPREGADO
WHERE NUMERO_SEGURO_SOCIAL NOT IN (SELECT NUMERO_SEGURO_SOCIAL FROM ASSALARIADO);

-- `exists`
SELECT * 
FROM DEPARTAMENTO DEPTO
WHERE EXISTS(SELECT  *
             FROM PROJETO
             WHERE NUMERO_DEPTO = DEPTO.NUMERO);
             
SELECT * FROM EMPREGADO EMP
WHERE EXISTS(SELECT * FROM PROJETO_EMPREGADO
             WHERE NUMERO_SEGURO_SOCIAL = EMP.NUMERO_SEGURO_SOCIAL);
             
-- Joins
-- `AS` pode ser omitido para apelidar tabela
SELECT E.NUMERO_SEGURO_SOCIAL, E.NOME, COUNT(D.NOME) AS QTD_DEPENDENTE, DP.NOME 
FROM EMPREGADO AS E
INNER JOIN DEPENDENTE AS D
ON E.NUMERO_SEGURO_SOCIAL = D.NUMERO_SEGURO_SOCIAL
INNER JOIN DEPARTAMENTO AS DP
ON E.NUMERO_DEPTO = DP.NUMERO
GROUP BY E.NUMERO_SEGURO_SOCIAL;

SELECT E.NUMERO_SEGURO_SOCIAL AS 'SEGURO', E.NOME AS 'EMPREAGO',
       D.NOME AS 'DEPENDENTE', DP.NOME AS 'DEPARTAMENTO'
FROM EMPREGADO AS E
LEFT JOIN DEPENDENTE AS D
ON E.NUMERO_SEGURO_SOCIAL = D.NUMERO_SEGURO_SOCIAL
INNER JOIN DEPARTAMENTO AS DP
ON E.NUMERO_DEPTO = DP.NUMERO;

SELECT * 
FROM EMPREGADO
CROSS JOIN DEPENDENTE;
-- Para cada empregado, vai fazer um join, com todos os dependentes



SELECT * FROM ASSALARIADO_HISTORICO;