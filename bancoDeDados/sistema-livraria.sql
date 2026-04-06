

-- Criação da tabela Clientes
CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    nomeCliente VARCHAR(255),
    emailCliente VARCHAR(255)
);

-- Criação da tabela Compras com referência à tabela Clientes
CREATE TABLE Compras (
    CompraID INT PRIMARY KEY,
    ClienteID INT,
    NomeLivro VARCHAR(255),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

-- Inserindo dados na tabela Clientes
INSERT INTO Clientes (ID, nomeCliente, emailCliente) VALUES 
(1, 'Maria Silva', 'maria.silva@email.com'),
(2, 'João Souza', 'joao.souza@email.com'),
(3, 'Ana Oliveira', 'ana.oliveira@email.com');

-- Inserindo dados na tabela Compras
INSERT INTO Compras (CompraID, ClienteID, NomeLivro) VALUES 
(101, 1, 'Quarto de Despejo'),
(102, 2, 'Dom Casmurro'),
(103, 3, 'Quarto de Despejo'),
(104, 1, 'A Hora da Estrela');
--
SELECT * FROM Clientes;
