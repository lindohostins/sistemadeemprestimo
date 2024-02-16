-- Criação da tabela de usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

-- Criação da tabela de jogos
CREATE TABLE jogos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    categoria VARCHAR(50) NOT NULL,
    FOREIGN KEY (categoria) REFERENCES categorias(nome)
);

-- Criação da tabela de categorias
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Inserção de categorias
INSERT INTO categorias (nome) VALUES
('Esportes'),
('Ação'),
('Luta'),
('RPG');

-- Inserção de usuários
INSERT INTO usuarios (nome, email, senha) VALUES
('Usuário 1', 'usuario1@example.com', 'senha123'),
('Usuário 2', 'usuario2@example.com', 'senha456');

-- Inserção de jogos
INSERT INTO jogos (titulo, descricao, categoria) VALUES
('FIFA 22', 'Simulador de futebol', 'Esportes'),
('NBA 2K22', 'Simulador de basquete', 'Esportes'),
('GTA V', 'Ação e aventura em mundo aberto', 'Ação'),
('Call of Duty: Warzone', 'Battle Royale de tiro em primeira pessoa', 'Ação'),
('Street Fighter V', 'Jogo de luta', 'Luta'),
('Mortal Kombat 11', 'Jogo de luta com personagens icônicos', 'Luta'),
('The Witcher 3: Wild Hunt', 'RPG de mundo aberto com história rica', 'RPG'),
('Skyrim', 'RPG épico de mundo aberto', 'RPG');
