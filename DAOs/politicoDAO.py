class Politico():
    def __init__(self, cpf, nome, candidatura, dataNasc, foto):
        self.cpf = cpf
        self.nome = nome
        self.candidatura = candidatura
        self.dataNasc = dataNasc
        self.foto = foto

class PoliticoDAO():
    def __init__():
        pass

    def create(self, cursor, politico):
        try:
            data = {'CPF': politico.cpf, 'nome': politico.nome,
            'candidatura': politico.candidatura, 'dataNasc': politico.dataNasc, 'foto': politico.foto}
            sql = "INSERT INTO politico VALUES(%(CPF)s, %(nome)s, %(candidatura)s, %(dataNasc)s, %(foto)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, politico, CPF):
        try:
            data = {'CPF': CPF, 'nome': politico.nome,
            'candidatura': politico.candidatura, 'dataNasc': politico.dataNasc, 'foto': politico.foto}
            sql = "UPDATE politico SET nome = %(nome)s, candidatura = %(candidatura)s, dataNasc = %(dataNasc)s, foto =' %(foto)s \
                WHERE CPF = %(CPF)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, CPF):
        try:
            sql = f"DELETE FROM politico WHERE CPF = '{CPF}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def findById(self, cursor, CPF):
        try:
            sql = f"SELECT * FROM politico WHERE CPF = '{CPF}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            CPF, nome, candidatura, dataNasc, foto = result
            politico = Politico(CPF, nome, candidatura, dataNasc, foto)
            return politico
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):
        try:
            sql = "SELECT * FROM politico"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None
