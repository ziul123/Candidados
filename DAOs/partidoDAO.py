class Partido():
    def __init__(self, numPart, nome, dataCriacao, logo):
        self.numPart = numPart
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.logo = logo        


class PartidoDAO():
    def create(self, cursor, partido):
        sql = "INSERT INTO partido VALUES(%(numPart)s, %(nome)s, %(dataCriacao)s, %(logo)s);"
        try:
            cursor.execute(sql, vars(partido))
        except Exception as ex:
            print(ex)

    def update(self, cursor, partido):
        sql = ("UPDATE partido SET nome=%(nome)s, dataCriacao=%(dataCriacao)s, logo=%(logo)s "
                "WHERE numPart=%(numPart)s;")
        try:
            cursor.execute(sql, vars(partido))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, numPart):
        sql = ("DELETE FROM politicoPartido WHERE partidoNumPart=%(numPart)s; "
                "DELETE FROM partido WHERE numPart=%(numPart)s;")
        try:
            cursor.execute(sql, {'numPart':numPart})
        except Exception as ex:
            print(ex)

    def get(self, cursor, numPart):
        sql = "SELECT * FROM partido WHERE numpart=%s;"
        try:
            cursor.execute(sql, (numPart,))
            result = cursor.fetchone()
            partido = Partido(*result)
            return partido
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM partido;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            partidos = [Partido(*x) for x in result]
            return partidos
        except Exception as ex:
            print(ex)
