USE controle_lab;

CREATE TABLE IF NOT EXISTS usuario (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nome       VARCHAR(60) NOT NULL,
    login      VARCHAR(30) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    perfil     ENUM('Professor', 'Técnico', 'Administrador') NOT NULL
);

INSERT INTO usuario (nome, login, senha_hash, perfil) VALUES
('Professor Exemplo', 'professor', 'pbkdf2:sha256:1000000$cNZOvbEuovDmSDZL$d56ebf510ff438a9ccc7cb8bcc97a8ce0a1c81666be0fb413a750a6672b7fce1', 'Professor'),
('Técnico de Manutenção', 'tecnico', 'pbkdf2:sha256:1000000$LUuep4uV79fiiKq1$a767a07e7bfb3fda7a4170f69da4737f37d72b841aa08d2773d72d0b8565a64e', 'Técnico'),
('Administrador', 'admin', 'pbkdf2:sha256:1000000$Aa0zWeprdv06uUaH$3599e08c2ea11c0c18e0f8bf94464512be01bc09153566b24d1f24ced4ee8cb5', 'Administrador');
