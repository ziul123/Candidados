class ExerceCargoEm:
    def __init__(self, orgaoCodOrg, politicoCPF, dataEleito, nomeCargo, ambito, tempoMandato, salario):
        self.orgaoCodOrg = orgaoCodOrg
        self.politicoCPF = politicoCPF
        self.dataEleito = dataEleito
        self.nomeCargo = nomeCargo
        self.ambito = ambito
        self.tempoMandato = tempoMandato
        self.salario = salario


class ExerceCargoEmDAO:
    def create(self, cursor, exerceCargoEm):
        sql = "INSERT INTO exerceCargoEm VALUES(%(orgaoCodOrg)s, %(politicoCPF)s, %(dataEleito)s, %(nomeCargo)s, \
            %(tempoMandato)s, %(salario)s);"
        try:
            cursor.execute(sql, vars(exerceCargoEm))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def update(self, cursor, exerceCargoEm):
        sql = "UPDATE exerceCargoEm SET nomeCargo = %(nomeCargo)s, ambito = %(ambito)s, tempoMandato = %(tempoMandato)s, \
            salario = %(salario)s WHERE (orgaoCodOrg = %(orgaoCodOrg)s AND politicoCPF = %(politicoCPF)s AND \
            dataEleito = %(dataEleito)s);"
        try:
            cursor.execute(sql, vars(exerceCargoEm))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def delete(self, cursor, orgaoCodOrg, politicoCPF, dataEleito):
        sql = "DELETE FROM exerceCargoEm WHERE (orgaoCodOrg = %s AND politicoCPF = %s \
            AND dataEleito = %s);"
        try:
            cursor.execute(sql, (orgaoCodOrg, politicoCPF, dataEleito))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def get(self, cursor, orgaoCodOrg, politicoCPF, dataEleito):
        sql = "SELECT * FROM exerceCargoEm WHERE (orgaoCodOrg = %s AND politicoCPF = %s \
            AND dataEleito = %s);"
        try:
            cursor.execute(sql, (orgaoCodOrg, politicoCPF, dataEleito))
            result = cursor.fetchone()

            exerceCargoEm = ExerceCargoEm(*result)
            return exerceCargoEm
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM exerceCargoEm;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            exerceCargoEm = [ExerceCargoEm(*x) for x in result]
            return exerceCargoEm
        except Exception as ex:
            print(ex)
