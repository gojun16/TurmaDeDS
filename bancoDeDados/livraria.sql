-- 1. Criação da tabela LIVROS
CREATE TABLE LIVROS (
    ID_LIVRO INT PRIMARY KEY,
    CATEGORIA VARCHAR(50),
    AUTORIA VARCHAR(100),
    NOME_LIVRO VARCHAR(150),
    EDITORA VARCHAR(100),
    PREÇO DECIMAL(10, 2)
);

-- 2. Inserindo valores fora de ordem
INSERT INTO LIVROS 
(CATEGORIA, AUTORIA, NOME_LIVRO, EDITORA, ID_LIVRO, PREÇO)
VALUES
('Biografia' ,	'Malala Yousafzai', 'Eu sou Malala'       , 'Companhia das Letras', 11, 22.32),
('Biografia' ,	'Michelle Obama'  , 'Minha história'      , 'Objetiva'            ,	12,	57.90),
('Biografia' ,	'Anne Frank'      , 'Diário de Anne Frank', 'Pe Da Letra'         , 13, 34.90);

-- 3. Exibir a tabela completa
SELECT * FROM LIVROS;
