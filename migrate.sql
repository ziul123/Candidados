-- politico

INSERT INTO politico VALUES("58999956024", "Ana", "Senadora", "2002-06-11", LOAD_FILE("/var/lib/mysql-files/mulher1.jpeg")); -- 10 PCB
INSERT INTO politico VALUES("63630773036", "Sofia", "Deputada Federal", "1993-08-11", LOAD_FILE("/var/lib/mysql-files/mulher2.jpeg")); -- 12 PEM 
INSERT INTO politico VALUES("54572974039", "Luiz", "Vereador", "2001-09-07", LOAD_FILE("/var/lib/mysql-files/homem1.jpeg")); -- 13 PLB
INSERT INTO politico VALUES("77976787071", "Carlos", NULL, "1974-01-13", LOAD_FILE("/var/lib/mysql-files/homem2.jpeg")); -- 07 UNE
INSERT INTO politico VALUES("08569069057", "Victor", "Vereador", "2001-12-12", LOAD_FILE("/var/lib/mysql-files/homem3.jpeg")); -- 15 PLT
INSERT INTO politico VALUES("24309074022", "Hugo", NULL, "1997-11-19", LOAD_FILE("/var/lib/mysql-files/homem4.jpeg")); -- 23 PAF
INSERT INTO politico VALUES("35306870066", "Lucas", "Deputado Distrital", "2003-10-31", LOAD_FILE("/var/lib/mysql-files/homem5.jpeg")); -- 55 PTU
INSERT INTO politico VALUES("07429018076", "Henrique", "Deputado Estadual", "1995-02-15", LOAD_FILE("/var/lib/mysql-files/homem6.jpeg")); -- 10 PCB
INSERT INTO politico VALUES("43973086087", "Eduardo", "Deputado Federal", "1976-04-12", LOAD_FILE("/var/lib/mysql-files/homem7.jpeg")); -- 12 PEM
INSERT INTO politico VALUES("98030829060", "Thiago", "Vereador", "2000-04-01", LOAD_FILE("/var/lib/mysql-files/homem8.jpeg")); -- 13 PLB
INSERT INTO politico VALUES("96826773007", "Luiza", "Vereadora", "1998-05-29", LOAD_FILE("/var/lib/mysql-files/mulher3.jpeg")); -- 13 PLB
INSERT INTO politico VALUES("18621276038", "Sara", "Deputada Estadual", "1988-07-06", LOAD_FILE("/var/lib/mysql-files/mulher4.jpeg")); -- 07 UNE
INSERT INTO politico VALUES("83063484008", "Eduarda", NULL, "2001-06-06", LOAD_FILE("/var/lib/mysql-files/mulher5.jpeg")); -- 15 PLT

-- partido

INSERT INTO partido VALUES(10, "PCB", "1980-06-01", NULL);
INSERT INTO partido VALUES(12, "PEM", "1993-01-31", NULL);
INSERT INTO partido VALUES(13, "PLB", "1997-09-03", NULL);
INSERT INTO partido VALUES(07, "UNE", "1988-08-02", NULL);
INSERT INTO partido VALUES(15, "PLT", "1963-02-02", NULL);
INSERT INTO partido VALUES(23, "PAF", "2004-04-30", NULL);
INSERT INTO partido VALUES(55, "PTU", "2009-03-20", NULL);

-- politicoPartido

INSERT INTO politicoPartido VALUES("58999956024", 10, "2017-10-19", "Presidente");
INSERT INTO politicoPartido VALUES("63630773036", 12, "2014-08-08", "Secretaria");
INSERT INTO politicoPartido VALUES("54572974039", 13, "2000-09-10", "Vice-presidente");
INSERT INTO politicoPartido VALUES("77976787071", 07, "1993-01-15", "Membro");
INSERT INTO politicoPartido VALUES("08569069057", 15, "1994-03-13", "Membro");
INSERT INTO politicoPartido VALUES("24309074022", 23, "2005-12-29", "Presidente");
INSERT INTO politicoPartido VALUES("35306870066", 55, "2010-11-29", "Membro");
INSERT INTO politicoPartido VALUES("07429018076", 10, "2000-10-10", "Vice-presidente");
INSERT INTO politicoPartido VALUES("43973086087", 12, "1999-02-02", "Membro");
INSERT INTO politicoPartido VALUES("98030829060", 13, "2006-09-12", "Membro");
INSERT INTO politicoPartido VALUES("96826773007", 13, "2007-07-09", "Presidente");
INSERT INTO politicoPartido VALUES("18621276038", 07, "1990-01-29", "Presidente");
INSERT INTO politicoPartido VALUES("83063484008", 15, "2001-08-20", "Membro");

-- beneficio

INSERT INTO beneficio VALUES(1, "Auxilio Moradia", 5000.00);
INSERT INTO beneficio VALUES(2, "Auxilio Terno", 400.00);
INSERT INTO beneficio VALUES(3, "Auxilio Transporte", 1000.00);
INSERT INTO beneficio VALUES(4, "Auxilio Doença", 10000.00);
INSERT INTO beneficio VALUES(5, "Auxilio Alimentacao", 500.00);
INSERT INTO beneficio VALUES(6, "Auxilio Pensao", 2000.00);
INSERT INTO beneficio VALUES(7, "Auxilio Mudanca", 6500.00);

-- politicoPossuiBeneficio

INSERT INTO politicoPossuiBeneficio VALUES("58999956024", 1);
INSERT INTO politicoPossuiBeneficio VALUES("63630773036", 2);
INSERT INTO politicoPossuiBeneficio VALUES("54572974039", 3);
INSERT INTO politicoPossuiBeneficio VALUES("77976787071", 4);
INSERT INTO politicoPossuiBeneficio VALUES("08569069057", 5);
INSERT INTO politicoPossuiBeneficio VALUES("24309074022", 6);
INSERT INTO politicoPossuiBeneficio VALUES("35306870066", 7);
INSERT INTO politicoPossuiBeneficio VALUES("07429018076", 1);
INSERT INTO politicoPossuiBeneficio VALUES("43973086087", 2);
INSERT INTO politicoPossuiBeneficio VALUES("98030829060", 3);
INSERT INTO politicoPossuiBeneficio VALUES("96826773007", 4);
INSERT INTO politicoPossuiBeneficio VALUES("18621276038", 5);
INSERT INTO politicoPossuiBeneficio VALUES("83063484008", 6);
INSERT INTO politicoPossuiBeneficio VALUES("58999956024", 7);

-- projetoLei

INSERT INTO projetoLei VALUES(1, "Proibir o cigarro eletronico", "2022-07-19", "APROVADO");
INSERT INTO projetoLei VALUES(2, "Legalizar Cannabis Sativa", "2022-09-14", "NÃO APROVADO");
INSERT INTO projetoLei VALUES(3, "Adição dos produtos de higiene menstrual no SUS", "1994-10-04", "APROVADO");
INSERT INTO projetoLei VALUES(4, "Castração de animais de rua", "2021-12-27", "APROVADO");
INSERT INTO projetoLei VALUES(5, "Reforma da regularização da armamentação", "2020-08-10", "NÃO APROVADO");
INSERT INTO projetoLei VALUES(6, "Incentivo para artistas de rua", "1992-02-28", "APROVADO");
INSERT INTO projetoLei VALUES(7, "Restauração da mata da Araucária", "2022-01-12", "NÃO APROVADO");

-- politicoEscreveProjetoLei
INSERT INTO politicoEscreveProjetoLei VALUES("58999956024", 1);
INSERT INTO politicoEscreveProjetoLei VALUES("07429018076", 2);
INSERT INTO politicoEscreveProjetoLei VALUES("96826773007", 3);
INSERT INTO politicoEscreveProjetoLei VALUES("18621276038", 4);
INSERT INTO politicoEscreveProjetoLei VALUES("83063484008" ,5);
INSERT INTO politicoEscreveProjetoLei VALUES("35306870066", 6);
INSERT INTO politicoEscreveProjetoLei VALUES("98030829060", 7);

-- politicoVotaProjetoLei
INSERT INTO politicoVotaProjetoLei VALUES("58999956024", 2, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("63630773036", 1, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("54572974039", 3, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("77976787071", 4, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("08569069057", 6, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("24309074022", 5, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("35306870066", 7, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("07429018076", 3, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("43973086087", 1, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("98030829060", 4, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("96826773007", 7, "SIM");
INSERT INTO politicoVotaProjetoLei VALUES("18621276038", 5, "NÃO");
INSERT INTO politicoVotaProjetoLei VALUES("83063484008", 4, "SIM");

-- local
INSERT INTO local VALUES(1, "DF", "Brasilia");
INSERT INTO local VALUES(2, "BA", "Itabuna");
INSERT INTO local VALUES(3, "RJ", "Rio de Janeiro");
INSERT INTO local VALUES(4, "SP", "São Paulo");
INSERT INTO local VALUES(5, "MG", "Belo Horizonte");

-- orgao
INSERT INTO orgao VALUES(1, "Senado", 1);
INSERT INTO orgao VALUES(2, "Camara dos Deputados", 1);
INSERT INTO orgao VALUES(3, "Camara Municipal de Itabuna", 2);
INSERT INTO orgao VALUES(4, "Camara Estadual do Rio de Janeiro", 3);
INSERT INTO orgao VALUES(5, "Camara Municipal de São Paulo", 4);
INSERT INTO orgao VALUES(6, "Camara Estadual de Minas Gerais", 5);

-- exerceCargoEm
INSERT INTO exerceCargoEm VALUES(1, "58999956024", "2018-10-30", "Senador", "Federal", 8, 30000.00);
INSERT INTO exerceCargoEm VALUES(2, "63630773036", "2018-10-30", "Deputado Federal", "Federal", 4, 29000.99);
INSERT INTO exerceCargoEm VALUES(3, "54572974039", "2020-10-30", "Vereador", "Municipal", 4, 20000.00);
INSERT INTO exerceCargoEm VALUES(4, "77976787071", "2020-10-30", "Deputado Estadual", "Estadual", 4, 25000.50);
INSERT INTO exerceCargoEm VALUES(5, "08569069057", "2020-10-30", "Vereador", "Municipal", 4, 20000.00);
INSERT INTO exerceCargoEm VALUES(6, "24309074022", "2020-10-30", "Deputado Estadual", "Estadual", 4, 20000.00);
--INSERT INTO exerceCargoEm VALUES(1);
--INSERT INTO exerceCargoEm VALUES();
--INSERT INTO exerceCargoEm VALUES();
--INSERT INTO exerceCargoEm VALUES();
--INSERT INTO exerceCargoEm VALUES();
--INSERT INTO exerceCargoEm VALUES();
--INSERT INTO exerceCargoEm VALUES();

-- processo
INSERT INTO processo VALUES(1, "2020-01-01", "João", "INOCENTADO", "58999956024");
INSERT INTO processo VALUES(2, "2021-02-01", "João", "CULPADO", "63630773036");
INSERT INTO processo VALUES(3, "2021-03-03", "Maria", "INOCENTADO", "54572974039");
INSERT INTO processo VALUES(4, "2021-04-29", "Marcos", "CULPADO", "77976787071");
INSERT INTO processo VALUES(5, "2021-05-15", "Estácio", "CULPADO", "08569069057");
