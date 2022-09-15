class Partido:
    def __init__(self, numPart, nome, dataCriacao, logo):
        self.numPart = numPart
        self.nome = nome
        self.dataCriacao = dataCriacao
        self.logo = logo        


class PoliticosNoPartido:
    def __init__(self, politicoNome, dataFiliacao, cargo):
        self.politicoNome = politicoNome
        self.dataFiliacao = dataFiliacao
        self.cargo = cargo


class PartidoDAO:
    def create(self, cursor, partido):
        sql = "INSERT INTO partido VALUES(%(numPart)s, %(nome)s, %(dataCriacao)s, %(logo)s);"
        try:
            cursor.execute(sql, vars(partido))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def update(self, cursor, partido):
        sql = ("UPDATE partido SET nome=%(nome)s, dataCriacao=%(dataCriacao)s, logo=%(logo)s "
                "WHERE numPart=%(numPart)s;")
        try:
            cursor.execute(sql, vars(partido))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def delete(self, cursor, numPart):
        sql = ("DELETE FROM politicoPartido WHERE partidoNumPart=%(numPart)s; "
                "DELETE FROM partido WHERE numPart=%(numPart)s;")
        try:
            cursor.execute(sql, {'numPart':numPart})
            DAOs.cnx.commit()
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

    def getPoliticos(self, cursor, partidoNumPart):
        try:
            cursor.callproc("politicosNoPartido", (partidoNumPart,))
            result = [r.fetchall() for r in cursor.stored_results()]
            politicosNoPartido = [PoliticosNoPartido(*x) for x in result]
            return politicosNoPartido
        except Exception as ex:
           print(ex) 
