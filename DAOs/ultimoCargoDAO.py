class UltimoCargo:
    def __init__(self, politicoCPF, nomeCargo, dataEleito, orgaoNome, ambito, salario, localEstado, localCidade):
        self.politicoCPF = politicoCPF
        self.nomeCargo = nomeCargo
        self.dataEleito = dataEleito
        self.orgaoNome = orgaoNome
        self.ambito = ambito
        self.salario = salario
        self.localEstado = localEstado
        self.localCidade = localCidade


class UltimoCargoDAO:
    def get(self, cursor, politicoCPF):
        sql = "SELECT * FROM ultimoCargo WHERE politicoCPF=%s;"
        try:
            cursor.execute(sql, (politicoCPF,))
            result = cursor.fetchone()
            ultimoCargo = UltimoCargo(*result)
            return ultimoCargo
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM ultimoCargo;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            ultimoCargo = [UltimoCargo(*x) for x in result]
            return ultimoCargo
        except Exception as ex:
            print(ex)
