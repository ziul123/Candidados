class PoliticoPartido:
    def __init__(self, politicoCPF, partidoNumPart, dataFiliacao, cargo):
        self.politicoCPF = politicoCPF
        self.partidoNumPart = partidoNumPart
        self.dataFiliacao = dataFiliacao
        self.cargo = cargo

class PoliticoPartidoDAO:
    def create(self, cursor, politicoPartido):
        sql = "INSERT INTO politicoPartido VALUES(%(politicoCPF)s, %(partidoNumPart)s, %(dataFiliacao)s, %(cargo)s);"
        try:
            cursor.execute(sql, vars(politicoPartido))
        except Exception as ex:
            print(ex)
    
    def update(self, cursor, politicoPartido):
        sql = "UPDATE politicoPartido SET cargos = %(cargos)s WHERE politicoCPF = %(politicoCPF)s AND \
            partidoNumPart = %(partidoNumPart)s AND dataFiliacao = %(dataFiliacao)s);"
        try:
            cursor.execute(sql, vars(politicoPartido))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, politicoCPF, partidoNumPart, dataFiliacao):
        sql = "DELETE FROM politicoPartido WHERE (politicoCPF = %(politicoCPF)s AND partidoNumPart = %(partidoNumPart)s \
            AND dataFiliacao = %(dataFiliacao)s);"
        try:
            cursor.execute(sql, (politicoCPF, partidoNumPart, dataFiliacao))
        except Exception as ex:
            print(ex)

    def get(self, cursor, politicoCPF, partidoNumPart, dataFiliacao):
        sql = "SELECT * FROM politicoPartido WHERE (politicoCPF = %(politicoCPF)s AND partidoNumPart = %(partidoNumPart)s \
            AND dataFiliacao = %(dataFiliacao)s);"
        try:
            cursor.execute(sql, (politicoCPF, partidoNumPart, dataFiliacao))
            result = cursor.fetchone()
            politicoPartido = PoliticoPartido(*result)
            return politicoPartido
        except Exception as ex:
            print(ex)
    
    def getAll(self, cursor):
        sql = "SELECT * FROM politicoPartido;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            politicoPartido = [PoliticoPartido(*x) for x in result]
            return politicoPartido
        except Exception as ex:
            print(ex)
