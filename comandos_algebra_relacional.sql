-- Esses são os comandos para representar na álgebra relacional

-- Seleciona os politicos, o nome do cargo que trabalha e o nome do Orgao em que trabalha
SELECT politico.nome AS np, nomeCargo AS cargo, orgao.nome AS no FROM politico, exerceCargoEm, orgao WHERE CPF = politicoCPF AND codOrg = orgaoCodOrg;

SELECT 