USE candidados;

CREATE TABLE politico(
	CPF CHAR(11) PRIMARY KEY,
	nome VARCHAR(45) NOT NULL,
	candidatura VARCHAR(45),
	dataNasc DATE NOT NULL,
	foto MEDIUMBLOB
);


CREATE TABLE partido(
	numPart INT PRIMARY KEY,
	nome VARCHAR(45) NOT NULL,
	dataCriacao DATE NOT NULL,
	logo MEDIUMBLOB
);


CREATE TABLE politicoPartido(
	politicoCPF CHAR(11),
	partidoNumPart INT,
	dataFiliacao DATE,
	cargo VARCHAR(45),
	FOREIGN KEY (politicoCPF) REFERENCES politico(CPF),
	FOREIGN KEY (partidoNumPart) REFERENCES partido(numPart),
	PRIMARY KEY (politicoCPF, partidoNumPart, dataFiliacao)
);


CREATE TABLE beneficio(
	codBen INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(45) NOT NULL,
	valor DECIMAL(15,2) NOT NULL
);


CREATE TABLE politicoPossuiBeneficio(
	politicoCPF CHAR(11),
	beneficioCodBen INT,
	FOREIGN KEY (politicoCPF) REFERENCES politico(CPF),
	FOREIGN KEY (beneficioCodBen) REFERENCES beneficio(codBen),
	PRIMARY KEY (politicoCPF, beneficioCodBen)
);


CREATE TABLE projetoLei(
	numProj INT PRIMARY KEY,
	descricao VARCHAR(100) NOT NULL,
	dataCriacao DATE NOT NULL,
	aprovacao ENUM('APROVADO','NÃO APROVADO')
);


CREATE TABLE politicoEscreveProjetoLei(
	politicoCPF CHAR(11),
	projetoLeiNumProj INT,
	FOREIGN KEY (politicoCPF) REFERENCES politico(CPF),
	FOREIGN KEY (projetoLeiNumProj) REFERENCES projetoLei(numProj),
	PRIMARY KEY (politicoCPF, projetoLeiNumProj)
);


CREATE TABLE politicoVotaProjetoLei(
	politicoCPF CHAR(11),
	projetoLeiNumProj INT,
	voto VARCHAR(45),
	FOREIGN KEY (politicoCPF) REFERENCES politico(CPF),
	FOREIGN KEY (projetoLeiNumProj) REFERENCES projetoLei(numProj),
	PRIMARY KEY (politicoCPF, projetoLeiNumProj)
);


CREATE TABLE local(
	codLoc INT AUTO_INCREMENT PRIMARY KEY,
	estado VARCHAR(45) NOT NULL,
	municipio VARCHAR(45) NOT NULL
);


CREATE TABLE orgao(
	codOrg INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(45) NOT NULL,
	localCodLoc INT,
	FOREIGN KEY (localCodLoc) REFERENCES local(codLoc)
);


CREATE TABLE exerceCargoEm(
	orgaoCodOrg INT,
	politicoCPF CHAR(11),
	dataEleito DATE NOT NULL,
	nomeCargo VARCHAR(45) NOT NULL,
	ambito VARCHAR(45) NOT NULL,
	tempoMandato INT NOT NULL,
	salario DECIMAL(15,2) NOT NULL,
	FOREIGN KEY (orgaoCodOrg) REFERENCES orgao(codOrg),
	FOREIGN KEY (politicoCPF) REFERENCES politico(CPF),
	PRIMARY KEY (orgaoCodOrg, politicoCPF, dataEleito)
);



CREATE TABLE processo(
	numProc INT PRIMARY KEY,
	dataInicio DATE NOT NULL,
	autor VARCHAR(45) NOT NULL,
	resultado ENUM('CULPADO', 'INOCENTADO')
	politicoCPF CHAR(11),
	FOREIGN KEY ((politicoCPF) REFERENCES politico(CPF)
);


CREATE VIEW ultimoPartido AS
SELECT t1.politicoCPF, t1.partidoNumPart, partido.nome, t1.dataFiliacao, t1.cargo FROM politicoPartido AS t1
LEFT JOIN politicoPartido AS t2
ON t1.politicoCPF=t2.politicoCPF AND t1.dataFiliacao < t2.dataFiliacao
JOIN partido
ON t1.partidoNumPart=partido.numPart
WHERE t2.politicoCPF IS NULL;


CREATE VIEW ultimoCargo AS
SELECT t1.politicoCPF, t1.nomeCargo, t1.dataEleito, orgao.nome, t1.ambito, t1.salario, local.estado, local.municipio FROM exerceCargoEm AS t1
LEFT JOIN exerceCargoEm AS t2
ON t1.politicoCPF=t2.politicoCPF AND t1.dataEleito < t2.dataEleito
JOIN orgao
ON t1.orgaoCodOrg=orgao.codOrg
JOIN local
ON orgao.localCodLoc=local.codLoc
WHERE t2.politicoCPF IS NULL;


DELIMITER //
CREATE PROCEDURE politicosNoPartido (IN num INT)
BEGIN
		SELECT politico.nome, dataFiliacao, cargo FROM ultimoPartido
		JOIN politico
		ON politicoCPF=CPF
		WHERE partidoNumPart=num;
END //
DELIMITER ;
