-- Criando Banco de Dados
CREATE DATABASE BD_LIVRARIA;

-- Selecionando o Banco de Dados
USE BD_LIVRARIA;

-- Criando Tabelas Minha Versão
CREATE TABLE CLIENTE(CODIGO INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
NOME VARCHAR(150) NOT NULL,
CEP INT,
CIDADE VARCHAR(50),
BAIRRO VARCHAR(50),
RUA VARCHAR(100),
NUMERO VARCHAR(10)
);

CREATE TABLE TELEFONE_CLIENTE(TELEFONE INT NOT NULL,
CLIENTE_CODIGO INT NOT NULL,
FOREIGN KEY (CLIENTE_CODIGO) REFERENCES CLIENTE(CODIGO),
PRIMARY KEY (TELEFONE, CLIENTE_CODIGO)
);

CREATE TABLE CLIENTE_JURIDICO(CNPJ BIGINT NOT NULL,
CLIENTE_CODIGO INT NOT NULL,
FOREIGN KEY (CLIENTE_CODIGO) REFERENCES CLIENTE(CODIGO),
PRIMARY KEY (CNPJ, CLIENTE_CODIGO)
);

CREATE TABLE CLIENTE_FISICO(CPF BIGINT NOT NULL,
CLIENTE_CODIGO INT NOT NULL,
FOREIGN KEY (CLIENTE_CODIGO) REFERENCES CLIENTE(CODIGO),
PRIMARY KEY (CPF, CLIENTE_CODIGO)
);

CREATE TABLE EDITORA(CODIGO INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
NOME_GERENTE VARCHAR(150) NOT NULL,
CEP INT,
CIDADE VARCHAR(50),
BAIRRO VARCHAR(50),
RUA VARCHAR(100),
NUMERO VARCHAR(10)
);

CREATE TABLE TELEFONE_GERENTE(TELEFONE INT NOT NULL,
EDITORA_CODIGO INT NOT NULL,
FOREIGN KEY (EDITORA_CODIGO) REFERENCES EDITORA(CODIGO)
);

CREATE TABLE LIVRO(ISBN BIGINT NOT NULL,
ASSUNTO VARCHAR(10) NOT NULL,
QUANTIDADE INT NOT NULL,
EDITORA_CODIGO INT NOT NULL,
FOREIGN KEY (EDITORA_CODIGO) REFERENCES EDITORA(CODIGO)
);

CREATE TABLE AUTOR(NOME VARCHAR(150) NOT NULL,
LIVRO_ISBN BIGINT NOT NULL,
FOREIGN KEY (LIVRO_ISBN) REFERENCES LIVRO(ISBN),
PRIMARY KEY (LIVRO_ISBN, NOME)
);

CREATE TABLE COMPRA(LIVRO_ISBN BIGINT NOT NULL,
CLIENTE_CODIGO INT NOT NULL,
DATA_COMPRA DATE,
FOREIGN KEY (LIVRO_ISBN) REFERENCES LIVRO(ISBN),
FOREIGN KEY (CLIENTE_CODIGO) REFERENCES CLIENTE(CODIGO),
PRIMARY KEY (LIVRO_ISBN, CLIENTE_CODIGO)
);

-- Inserindo Dados
-- Inserindo Clientes
INSERT INTO CLIENTE(NOME, CEP, CIDADE, BAIRRO, RUA, NUMERO)
VALUES ('Ailton Miranda Junior', 17700000, 'Osvaldo Cruz', 'Centro', 'Rua 15 de Novembro', '115');
INSERT INTO CLIENTE(NOME, CEP, CIDADE, BAIRRO, RUA, NUMERO)
VALUES ('Andressa Rosa de Lima', 17700000, 'Osvaldo Cruz', 'Alvorada', 'Rua Diamante', '20');
INSERT INTO CLIENTE(NOME, CEP, CIDADE, BAIRRO, RUA, NUMERO)
VALUES ('Valmir Miranda Neto', 17700000, 'Osvaldo Cruz', 'Jardim Beija Flor', 'Rua Francisco Antonio Gaudio', '200');
INSERT INTO CLIENTE(NOME, CEP, CIDADE, BAIRRO, RUA, NUMERO)
VALUES ('Carlos Aparecido da Silva', 17700000, 'Osvaldo Cruz', 'Centro', 'Rua Antonio Savino', '225A');
INSERT INTO CLIENTE(NOME, CEP, CIDADE, BAIRRO, RUA, NUMERO)
VALUES ('Matheus Celestiono', 19010000, 'Presidente Prudente', 'Centro', 'Rua Barão do Rio Branco', '250');

-- Inserindo Telefone de Clientes
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(35282115, 1);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(996518723, 1);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(35283133, 2);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(35291567, 3);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(998762314, 3);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(997657319, 4);
INSERT INTO TELEFONE_CLIENTE(TELEFONE, CLIENTE_CODIGO) VALUES(997658332, 5);

-- Inserindo Pessoa Fisica
INSERT INTO CLIENTE_FISICO(CPF, CLIENTE_CODIGO) VALUES(63474457276, 2);
INSERT INTO CLIENTE_FISICO(CPF, CLIENTE_CODIGO) VALUES(33583776526, 3);
INSERT INTO CLIENTE_FISICO(CPF, CLIENTE_CODIGO) VALUES(35252494118, 4);
INSERT INTO CLIENTE_FISICO(CPF, CLIENTE_CODIGO) VALUES(29418357330, 5);

-- Inserindo Pessoa Juridica
INSERT INTO CLIENTE_JURIDICO(CNPJ, CLIENTE_CODIGO) VALUES(19565413000141, 1);

-- Inserindo Editoras
INSERT INTO EDITORA(NOME_GERENTE, CEP, CIDADE, BAIRRO, RUA, NUMERO) 
VALUES('Carlos Abrantes', 17730000, 'Parapuã', 'Centro', 'Rua das Palmeiras', '125B');
INSERT INTO EDITORA(NOME_GERENTE, CEP, CIDADE, BAIRRO, RUA, NUMERO) 
VALUES('Marlon Brando', 17740970, 'Rinópolis', 'Centro', 'Avenida Rinópolis', '365');
INSERT INTO EDITORA(NOME_GERENTE, CEP, CIDADE, BAIRRO, RUA, NUMERO) 
VALUES('Alberto Camaroes', 11900971, 'Registro', 'Vila Cabral', 'Rua Amapá', '142D');
INSERT INTO EDITORA(NOME_GERENTE, CEP, CIDADE, BAIRRO, RUA, NUMERO) 
VALUES('Marta Arruda', 08694590, 'Suzano', 'Jardim Carmem', 'Rua Benedito Cardoso dos Santos', '450');
INSERT INTO EDITORA(NOME_GERENTE, CEP, CIDADE, BAIRRO, RUA, NUMERO) 
VALUES('Rose Vecchi', 13280975, 'Vinhedo', 'Distrito Industrial', 'Rua Comendador João Lucas', '101');

-- Inserindo Telefone Gerentes
INSERT INTO TELEFONE_GERENTE(EDITORA_CODIGO, TELEFONE) VALUES(1, 998764431);
INSERT INTO TELEFONE_GERENTE(EDITORA_CODIGO, TELEFONE) VALUES(2, 998956464);
INSERT INTO TELEFONE_GERENTE(EDITORA_CODIGO, TELEFONE) VALUES(3, 981765431);
INSERT INTO TELEFONE_GERENTE(EDITORA_CODIGO, TELEFONE) VALUES(4, 996533411);
INSERT INTO TELEFONE_GERENTE(EDITORA_CODIGO, TELEFONE) VALUES(5, 998775123);

-- Inserindo Livros
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9992158107, 'Historia', 12, 1);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9652153407, 'Historia', 25, 1);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9232158854, 'Ficção', 144, 2);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9941158896, 'Fantasia', 9, 2);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9475158900, 'Ação', 31, 3);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9983157566, 'Ação', 33, 3);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9122158989, 'Fantasia', 45, 4);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9877150098, 'Historia', 75, 4);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9911159002, 'Academico', 43, 5);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9933159977, 'Drama', 59, 5);
INSERT INTO LIVRO(ISBN, ASSUNTO, QUANTIDADE, EDITORA_CODIGO) VALUES(9732157777, 'Romance', 31, 5);

-- Inserindo Autores
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Augusto Silva', 9992158107);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Antonio Carlos', 9992158107);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Miranda Junior', 9652153407);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Alberto Norten', 9652153407);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Martin Carlos', 9232158854);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Arlindo Balbin', 9941158896);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Marcos Antonio', 9475158900);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Arlindo Gomes', 9983157566);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Martinho Gomes', 9122158989);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Marta Gomes Neto', 9877150098);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Marcia Silva', 9911159002);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Amando Pereira', 9933159977);
INSERT INTO AUTOR(NOME, LIVRO_ISBN) VALUES('Dandara Vecchi', 9732157777);

-- Inserindo Compras
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9992158107, 1, '2021-03-06');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9122158989, 1, '2021-05-12');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9652153407, 1, '2021-07-25');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9992158107, 2, '2021-03-21');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9732157777, 2, '2021-03-13');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9933159977, 2, '2021-03-22');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9911159002, 2, '2021-05-10');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9941158896, 3, '2021-03-01');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9732157777, 3, '2021-03-27');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9992158107, 4, '2021-07-12');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9232158854, 4, '2021-10-30');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9877150098, 5, '2021-03-03');
INSERT INTO COMPRA(LIVRO_ISBN, CLIENTE_CODIGO, DATA_COMPRA) VALUES(9941158896, 5, '2021-03-27');