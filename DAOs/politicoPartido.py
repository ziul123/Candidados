from requests import delete


class PoliticoPartido:

    def __init__(self, politicoCPF, partidoNumPart, dataFiliacao, cargo):
        self.politicoCPF = politicoCPF
        self.partidoNumPart = partidoNumPart
        self.dataFiliacao = dataFiliacao
        self.cargo = cargo

    def create(self, cursor, politicoPartido):

        sql = "INSERT INTO politicoPartido VALUES( %(politicoCPF)s, %(partidoNumPart)s, %(dataFiliacao)s, %(cargo)s"
        try:
            cursor.execute(sql, vars(politicoPartido))
        except Exception as ex:
            print(ex)
    
    def update(self, cursor, politicoPartido):

        sql = "UPDATE politicoPartido SET cargos = %(cargos) WHERE politicoCPF = %(politicoCPF AND \
            partidoNumPart = %(partidoNumPart) AND dataFiliacao = %(dataFiliacao))"
        try:
            cursor.execute(sql, vars(politicoPartido))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, politicoCPF, partidoNumPart, dataFiliacao):

        sql = f"DELETE * FROM politicoPartido WHERE (politicoCPF = '{politicoCPF}' AND partidoNumPart = '{partidoNumPart}' \
            AND dataFiliacao = '{dataFiliacao}')"
        
        try:
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def get(self, cursor, politicoCPF, partidoNumPart, dataFiliacao):

        sql = f"SELECT * FROM politicoPartido WHERE (politicoCPF = '{politicoCPF}' AND partidoNumPart = '{partidoNumPart}' \
            AND dataFiliacao = '{dataFiliacao}')"
        
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as ex:
            print(ex)
            return None
        
        politicoPartido = PoliticoPartido(*result)
        return politicoPartido
    
    def getAll(self, cursor):

        sql = "SELECT * FROM politicoPartido"

        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
            return None
        
        politicoPartido = [PoliticoPartido(*x) for x in result]
        return politicoPartido