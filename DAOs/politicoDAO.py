class Politico():
    def __init__(self, cpf, nome, candidatura, DataNasc, foto):
        self.cpf = cpf
        self.nome = nome
        self.candidatura = candidatura
        self.DataNasc = DataNasc
        self.foto = foto

class PoliticoDao():
    def __init__():
        pass

    def create(self, cursor, politico):
        try:
            data = {'CPF': politico.cpf, 'nome': politico.nome,
            'candidatura': politico.candidatura, 'DataNasc': politico.DataNasc, 'foto': politico.foto}
            sql = "INSERT INTO Politico VALUES(%(CPF)s, %(nome)s, %(candidatura)s, %(DataNasc)s, %(foto)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, politico, codigo):
        try:
            data = {'CPF': politico.cpf, 'nome': politico.nome,
            'candidatura': politico.candidatura, 'DataNasc': politico.DataNasc, 'foto': politico.foto}
            sql = "UPDATE Politico SET Nome = %(nome)s, Candidatura = %(candidatura)s, DataNasc = %(DataNasc)s, Foto =' %(foto)s \
                WHERE codigo = %(codigo)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codigo):
        try:
            sql = f"DELETE FROM endereco WHERE codigo = '{codigo}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def find_by_id(self, cursor, codigo):
        try:
            sql = f"SELECT * FROM endereco WHERE codigo = '{codigo}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codigo, CEP, rua, bairro, cidade, estado, numero, complemento = result
            endereco = Endereco(codigo, CEP, rua, bairro, cidade, estado, numero, complemento)
            return endereco
        except Exception as ex:
            print(ex)
            return None

    def find_all(self, cursor):
        try:
            sql = "SELECT * FROM endereco"
            cursor.execute(sql)
            result = cursor.fetchall()

            # depois ver como retornar
            return result
        except Exception as ex:
            print(ex)
            return None