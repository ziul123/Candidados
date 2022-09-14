class Orgao():
    def __init__(self, codOrg, nome, localCodLoc):
        self.codOrg = codOrg
        self.nome = nome
        self.localCodLoc = localCodLoc


class OrgaoDAO():
    def create(self, cursor, orgao):
        sql = "INSERT INTO partido VALUES(%(codOrg)s, %(nome)s, %(localCodLoc);"
        try:
            cursor.execute(sql, vars(orgao))
        except Exception as ex:
            print(ex)

    def update(self, cursor, orgao):
        sql = "UPDATE orgao SET nome = %(nome)s, localCodLoc=%(localCodLoc)s \
            WHERE codOrg = %(codOrg)s;"
        try:
            cursor.execute(sql, vars(orgao))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codOrg):
        sql = ("DELETE FROM exerceCargoEm WHERE codOrg=%(codOrg)s;"
                "DELETE FROM orgao WHERE codOrg=%(codOrg)s")
        try:
            cursor.execute(sql, {"codOrg":codOrg)
        except Exception as ex:
            print(ex)

    def get(self, cursor, codOrg):
        sql = "SELECT * FROM orgao WHERE codOrg=%s;"
        try:
            cursor.execute(sql, (codOrg,))
            result = cursor.fetchone()
            orgao = Orgao(*result)
            return orgao
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM orgao;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            orgaos = [Orgao(*x) for x in result]
            return orgaos
        except Exception as ex:
            print(ex)
