class Local():
    def __init__(self, codLoc, estado, municipio):
        self.codLoc = codLoc
        self.estado = estado
        self.municipio = municipio

class LocalDAO():
    def __init__():
        pass

    def create(self, cursor, local):
        try:
            data = {'codLoc': local.codLoc, 'estado': local.estado, 'municipio': local.municipio}
            sql = "INSERT INTO local VALUES(%(codLoc)s, %(estado)s, %(municipio)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, local, codLoc):
        try:
            data = {'codLoc': codLoc, 'estado': local.estado, 'municipio': local.municipio}
            sql = "UPDATE local SET estado = %(estado)s, municipio = %(municipio)s \
                WHERE codLoc = %(codLoc)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codLoc):
        try:
            sql = f"DELETE FROM local WHERE codLoc = '{codLoc}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def get(self, cursor, codLoc):
        try:
            sql = f"SELECT * FROM local WHERE codLoc = '{codLoc}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codLoc, estado, municipio = result
            local = Local(codLoc, estado, municipio)
            return local
        except Exception as ex:
            print(ex)
            return None

    def getAll(self, cursor):
        try:
            sql = "SELECT * FROM local"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None
