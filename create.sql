CREATE TABLE Politico(
	CPF CHAR(11) PRIMARY KEY,
	Nome VARCHAR(45) NOT NULL,
	Candidatura VARCHAR(45),
	DataNasc DATE NOT NULL,
	Foto MEDIUMBLOB NOT NULL
);


CREATE TABLE Partido(
	NumPart INT PRIMARY KEY,
	Nome VARCHAR(45) NOT NULL,
	VerbaAnual DECIMAL(15,2) NOT NULL,
	DataCriacao DATE NOT NULL,
	Logo MEDIUMBLOB NOT NULL
);


CREATE TABLE PoliticoPartido(
	PoliticoCPF CHAR(11),
	PartidoNumPart INT,
	DataFiliacao DATE,
	Cargo VARCHAR(45),
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	FOREIGN KEY (PartidoNumPart) REFERENCES Partido(NumPart),
	PRIMARY KEY (PoliticoCPF, PartidoNumPart, DataFiliacao)
);


CREATE TABLE Beneficio(
	CodBen INT AUTO_INCREMENT PRIMARY KEY,
	Nome VARCHAR(45) NOT NULL,
	Descricao VARCHAR(100),
	Valor DECIMAL(15,2) NOT NULL
);


CREATE TABLE PoliticoPossuiBeneficio(
	PoliticoCPF CHAR(11),
	BeneficioCodBen INT,
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	FOREIGN KEY (BeneficioCodBen) REFERENCES Beneficio(CodBen),
	PRIMARY KEY (PoliticoCPF, BeneficioCodBen)
);


CREATE TABLE ProjetoLei(
	NumProj INT PRIMARY KEY,
	Descricao VARCHAR(100) NOT NULL,
	DataCriacao DATE NOT NULL,
	Aprovacao ENUM('APROVADO','NÃO APROVADO')
);


CREATE TABLE PoliticoEscreveProjetoLei(
	PoliticoCPF CHAR(11),
	ProjetoLeiNumProj INT,
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	FOREIGN KEY (ProjetoLeiNumProj) REFERENCES ProjetoLei(NumProj),
	PRIMARY KEY (PoliticoCPF, ProjetoLeiNumProj)
);


CREATE TABLE PoliticoVotaProjetoLei(
	PoliticoCPF CHAR(11),
	ProjetoLeiNumProj INT,
	Voto VARCHAR(45),
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	FOREIGN KEY (ProjetoLeiNumProj) REFERENCES ProjetoLei(NumProj),
	PRIMARY KEY (PoliticoCPF, ProjetoLeiNumProj)
);


CREATE TABLE Local(
	CodLoc INT AUTO_INCREMENT PRIMARY KEY,
	Estado VARCHAR(45) NOT NULL,
	Municipio VARCHAR(45) NOT NULL
);


CREATE TABLE Orgao(
	CodOrg INT AUTO_INCREMENT PRIMARY KEY,
	Nome VARCHAR(45) NOT NULL,
	LocalCodLoc INT,
	FOREIGN KEY (LocalCodLoc) REFERENCES Local(CodLoc)
);


CREATE TABLE ExerceCargoEm(
	OrgaoCodOrg INT,
	PoliticoCPF CHAR(11),
	DataEleito DATE NOT NULL,
	NomeCargo VARCHAR(45) NOT NULL,
	Ambito VARCHAR(45) NOT NULL,
	TempoMandato INT NOT NULL,
	Salario DECIMAL(15,2) NOT NULL,
	FOREIGN KEY (OrgaoCodOrg) REFERENCES Orgao(CodOrg),
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	PRIMARY KEY (OrgaoCodOrg, PoliticoCPF, DataEleito)
);



CREATE TABLE Processo(
	NumProc INT PRIMARY KEY,
	Vara VARCHAR(45) NOT NULL,
	Andamento VARCHAR(45) NOT NULL,
	DataInicio DATE NOT NULL,
	Autor VARCHAR(45) NOT NULL,
	Resultado ENUM('CULPADO', 'INOCENTADO')
);


CREATE TABLE ProcessoPolitico(
	ProcessoNumProc INT,
	PoliticoCPF CHAR(11),
	FOREIGN KEY (ProcessoNumProc) REFERENCES Processo(NumProc),
	FOREIGN KEY (PoliticoCPF) REFERENCES Politico(CPF),
	PRIMARY KEY (ProcessoNumProc, PoliticoCPF)
);
