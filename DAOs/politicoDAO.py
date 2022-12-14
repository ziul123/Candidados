import DAOs


class Politico():
    def __init__(self, cpf, nome, candidatura, dataNasc, foto):
        self.cpf = cpf
        self.nome = nome
        self.candidatura = candidatura
        self.dataNasc = dataNasc
        self.foto = foto


class PoliticoDAO():
    def create(self, cursor, politico):
        sql = "INSERT INTO politico VALUES(%(CPF)s, %(nome)s, %(candidatura)s, %(dataNasc)s, %(foto)s);"
        try:
            cursor.execute(sql, vars(politico))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def update(self, cursor, politico):
        sql = ("UPDATE politico SET nome=%(nome)s, candidatura=%(candidatura)s, dataNasc=%(dataNasc)s, foto=%(foto)s "
                "WHERE CPF=%(CPF)s;")
        try:
            cursor.execute(sql, vars(politico))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def delete(self, cursor, CPF):
        sql = ("DELETE FROM politico WHERE CPF=%(CPF)s;")
        try:
            cursor.execute(sql, {"CPF":CPF})
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def get(self, cursor, CPF):
        sql = "SELECT * FROM politico WHERE CPF=%s;"
        try:
            cursor.execute(sql, (CPF,))
            result = cursor.fetchone()
            politico = Politico(*result)
            return politico
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM politico;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            politicos = [Politico(*x) for x in result]
            return politicos
        except Exception as ex:
            print(ex)

    def getCandidatos(self, cursor):
        sql = "SELECT * FROM politico WHERE candidatura IS NOT NULL;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            candidatos = [Politico(*x) for x in result]
            return candidatos
        except Exception as ex:
            print(ex)
