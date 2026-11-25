USE controle_lab;

INSERT INTO equipamento (patrimonio, laboratorio, tipo) VALUES
('PAT-0003', 'Laboratório 1', 'Computador'),
('PAT-0004', 'Laboratório 1', 'Teclado'),
('PAT-0005', 'Laboratório 1', 'Mouse'),
('PAT-0006', 'Laboratório 1', 'Projetor'),
('PAT-0107', 'Laboratório 2', 'Computador'),
('PAT-0108', 'Laboratório 2', 'Monitor'),
('PAT-0109', 'Laboratório 2', 'Mouse'),
('PAT-0110', 'Laboratório 2', 'Teclado'),
('PAT-0211', 'Laboratório 3', 'Computador'),
('PAT-0212', 'Laboratório 3', 'Computador'),
('PAT-0213', 'Laboratório 3', 'Monitor'),
('PAT-0214', 'Laboratório 3', 'Impressora');

INSERT INTO chamado (equipamento_id, descricao_problema, status_resolucao) VALUES
(2, 'Monitor piscando e desligando sozinho.', 'Aberto'),
(4, 'Papel atolando em toda impressão.', 'Em andamento'),
(14, 'Computador não liga depois da queda de energia.', 'Aberto');
