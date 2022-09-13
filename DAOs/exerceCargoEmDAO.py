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

    def __init__(self):
        pass

    def create(self, cursor, exerceCargoEm):

        try:
            data = {'orgaoCodOrg': exerceCargoEm.orgaoCodOrg, 'politicoCPF': exerceCargoEm.politicoCPF,
                    'dataEleito': exerceCargoEm.dataEleito, 'nomeCargo': exerceCargoEm.nomeCargo, 'ambito': exerceCargoEm.ambito,
                    'tempoMandato': exerceCargoEm.tempoMandato, 'salario': exerceCargoEm.salario}
            sql = "INTERT INTO exerceCargoEm VALUES(%(orgaoCodOrg)s, %(politicoCPF)s, %(dataEleito)s, %(nomeCargo)s, \
                %(tempoMandato)s, %(salario)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, exerceCargoEm, orgaoCodOrg, politicoCPF, dataEleito):

        try:
            data = {'orgaoCodOrg': orgaoCodOrg, 'politicoCPF': politicoCPF, 'dataEleito': dataEleito,
                    'nomeCargo': exerceCargoEm.nomeCargo, 'ambito': exerceCargoEm.ambito,
                    'tempoMandato': exerceCargoEm.tempoMandato, 'salario': exerceCargoEm.salario}
            sql = "UPDATE exerceCargoEm SET nomeCargo = %(nomeCargo)s, ambito = %(ambito)s, tempoMandato = %(tempoMandato)s, \
                salario = %(salario)s WHERE (orgaoCodOrg = %(orgaoCodOrg)s AND politicoCPF = %(politicoCPF)s AND \
                dataEleito = %(dataEleito)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, orgaoCodOrg, politicoCPF, dataEleito):

        try:
            sql = f"DELETE * FROM exerceCargoEm WHERE (orgaoCodOrg = '{orgaoCodOrg}' AND politicoCPF = '{politicoCPF}' \
                AND dataEleito = '{dataEleito}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def findById(self, cursor, orgaoCodOrg, politicoCPF, dataEleito):

        try:
            sql = f"SELECT * FROM findById WHERE (orgaoCodOrg = '{orgaoCodOrg}' AND politicoCPF = '{politicoCPF}' \
                AND dataEleito = '{dataEleito}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            exerceCargoEm = ExerceCargoEm(*result)
            return exerceCargoEm
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):

        try:
            sql = "SELECT * FROM exerceCargoEm"
            cursor.execute(sql)
            result = cursor.fetchall()

            exerceCargoEm = [ExerceCargoEm(*x) for x in result]
            return exerceCargoEm
        except Exception as ex:
            print(ex)
            return None