class Local():
    def __init__(self, codLoc, estado, municipio):
        self.codLoc = codLoc
        self.estado = estado
        self.municipio = municipio


class LocalDAO:
    def create(self, cursor, local):
        sql = "INSERT INTO local VALUES(%(codLoc)s, %(estado)s, %(municipio)s);"
        try:
            cursor.execute(sql, vars(local))
        except Exception as ex:
            print(ex)

    def update(self, cursor, local):
        sql = "UPDATE local SET estado = %(estado)s, municipio = %(municipio)s \
            WHERE codLoc = %(codLoc)s;"
        try:
            cursor.execute(sql, vars(local))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codLoc):
        sql = ("DELETE FROM orgao WHERE localCodLoc=%(codLoc)s;"
                "DELETE FROM local WHERE codLoc = %(codLoc)s;")
        try:
            cursor.execute(sql, {"codLoc":codLoc})
        except Exception as ex:
            print(ex)

    def get(self, cursor, codLoc):
        sql = "SELECT * FROM local WHERE codLoc=%s;"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            local = Local(*result)
            return local
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM local;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            locais = [Local(*x) for x in result]
            return locais
        except Exception as ex:
            print(ex)
