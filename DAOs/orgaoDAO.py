class Orgao():
    def __init__(self, codOrg, nome):
        self.codOrg = codOrg
        self.nome = nome

class OrgaoDAO():
    def __init__():
        pass

    def create(self, cursor, orgao):
        try:
            data = {'codOrg': orgao.codOrg, 'nome': orgao.nome}
            sql = "INSERT INTO partido VALUES(%(codOrg)s, %(nome)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, orgao, codOrg):
        try:
            data = {'codOrg': codOrg, 'nome':orgao.nome}
            sql = "UPDATE orgao SET nome = %(nome)s \
                WHERE codOrg = %(codOrg)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codOrg):
        try:
            sql = f"DELETE FROM orgao WHERE codOrg = '{codOrg}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def findById(self, cursor, codOrg):
        try:
            sql = f"SELECT * FROM orgao WHERE codOrg = '{codOrg}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codOrg, nome = result
            orgao = Orgao(codOrg, nome)
            return orgao
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):
        try:
            sql = "SELECT * FROM orgao"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None
