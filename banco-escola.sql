-- Criar tabela de autores
CREATE TABLE autores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

-- Criar tabela de livros
CREATE TABLE livros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    preco DECIMAL(10, 2),
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Inserir dados de exemplo
INSERT INTO autores (nome) VALUES ('Machado de Assis'), ('George Orwell');

INSERT INTO livros (titulo, preco, autor_id) VALUES 
('Dom Casmurro', 35.90, 1),
('1984', 42.00, 2),
('A Revolução dos Bichos', 29.90, 2);
