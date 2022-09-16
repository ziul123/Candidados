-- Esses são os comandos para representar na álgebra relacional

-- Seleciona os politicos, o nome do cargo que trabalha e o nome do Orgao em que trabalha
SELECT politico.nome AS Nome, nomeCargo AS Cargo, orgao.nome AS Orgao FROM politico, exerceCargoEm, orgao WHERE CPF = politicoCPF AND codOrg = orgaoCodOrg;

-- Seleciona Nome, Âmbito, Município e Estado de cada politico
SELECT politico.nome AS Nome, ambito, municipio, estado FROM politico, exerceCargoEm, orgao, candidados.local
WHERE CPF = politicoCPF AND codOrg = orgaoCodOrg AND codLoc = localCodLoc;

-- Seleciona nome, descricao do projeto de lei e voto do politico nesse projeto
SELECT nome, descricao, voto FROM politico, politicoVotaProjetoLei, projetoLei
WHERE CPF = politicoCPF AND numProj = projetoLeiNumProj;

-- Seleciona nome do politico, nome e valor do beneficio
SELECT politico.nome AS Nome, beneficio.nome AS Beneficio, valor FROM politico, beneficio, politicoPossuiBeneficio
WHERE CPF = politicoCPF AND codBen = beneficioCodBen;

-- Seleciona nome do politico, nome do partido e data de filiacao
SELECT politico.nome AS Nome, partido.nome AS Partido, dataFiliacao FROM politico, partido, politicoPartido
WHERE CPF = politicoCPF AND numPart = partidoNumPart;
