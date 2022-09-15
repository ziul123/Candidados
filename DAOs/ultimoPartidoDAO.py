class UltimoPartido:
    def __init__(self, politicoCPF, partidoNumPart, partidoNome, dataFiliacao, cargo):
        self.politicoCPF = politicoCPF
        self.partidoNumPart = partidoNumPart
        self.partidoNome = partidoNome
        self.dataFiliacao = dataFiliacao
        self.cargo = cargo


class UltimoPartidoDAO:
    def get(self, cursor, politicoCPF):
        sql = "SELECT * FROM ultimoPartido WHERE politicoCPF=%s;"
        try:
            cursor.execute(sql, (politicoCPF,))
            result = cursor.fetchone()
            ultimoPartido = UltimoPartido(*result)
            return ultimoPartido
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM ultimoPartido;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            ultimoPartido = [UltimoPartido(*x) for x in result]
            return ultimoPartido
        except Exception as ex:
            print(ex)
