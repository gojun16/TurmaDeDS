

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
