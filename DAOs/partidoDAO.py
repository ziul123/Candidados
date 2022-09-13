class Partido():
    def __init__(self, numPart, nome, dataCriacao, logo):
        self.numPart = numPart
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.logo = logo        

class PartidoDAO():
    def __init__():
        pass

    def create(self, cursor, partido):
        try:
            data = {'numPart': partido.numPart, 'nome': partido.nome, 'dataCriacao': partido.dataCriacao, 'logo': partido.logo}
            sql = "INSERT INTO partido VALUES(%(numPart)s, %(nome)s, %(dataCriacao)s, %(logo)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, partido, numPart):
        try:
            data = {'numPart': numPart, 'nome': partido.nome, 'dataCriacao': partido.dataCriacao, 'logo': partido.logo}
            sql = "UPDATE partido SET nome = %(nome)s, dataCriacao = %(dataCriacao)s, logo = %(logo)s \
                WHERE numPart = %(numPart)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, numPart):
        try:
            sql = f"DELETE FROM partido WHERE numPart = '{numPart}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def findById(self, cursor, numPart):
        try:
            sql = f"SELECT * FROM partido WHERE numpart = '{numPart}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            numPart, nome, dataCriacao, logo = result
            partido = Partido(numPart, nome, dataCriacao, logo)
            return partido
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):
        try:
            sql = "SELECT * FROM partido"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None
