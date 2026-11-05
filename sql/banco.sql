CREATE DATABASE IF NOT EXISTS controle_lab
    DEFAULT CHARACTER SET utf8mb4;
USE controle_lab;

CREATE TABLE IF NOT EXISTS equipamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patrimonio VARCHAR(20) NOT NULL UNIQUE,
    laboratorio VARCHAR(30) NOT NULL,
    tipo VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS chamado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipamento_id INT NOT NULL,
    data DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    descricao_problema TEXT NOT NULL,
    status_resolucao ENUM('Aberto', 'Em andamento', 'Resolvido')
        NOT NULL DEFAULT 'Aberto',
    FOREIGN KEY (equipamento_id) REFERENCES equipamento(id)
);

INSERT INTO equipamento (patrimonio, laboratorio, tipo) VALUES
('PAT-0001', 'Laboratório 1', 'Computador'),
('PAT-0002', 'Laboratório 1', 'Monitor'),
('PAT-0105', 'Laboratório 2', 'Computador'),
('PAT-0106', 'Laboratório 2', 'Impressora'),
('PAT-0210', 'Laboratório 3', 'Projetor');

INSERT INTO chamado (equipamento_id, descricao_problema) VALUES
(3, 'PC 05 do laboratório 2 está sem internet.');
