class Beneficio():
    def __init__(self, codBen, nome, valor):
        self.codBen = codBen
        self.nome = nome
        self.valor = valor

class PoliticoDao():
    def __init__():
        pass

    def create(self, cursor, beneficio):
        try:
            data = {'codBen': beneficio.codBen, 'nome': beneficio.nome, 'valor': beneficio.valor}
            sql = "INSERT INTO beneficio VALUES(%(codBen)s, %(nome)s, %(valor)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, beneficio, codBen):
        try:
            data = {'codBen': beneficio.codBen, 'nome': beneficio.nome, 'valor': beneficio.valor}
            sql = "UPDATE beneficio SET nome = %(nome)s, valor = %(valor)s \
                WHERE codBen = %(codBen)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codBen):
        try:
            sql = f"DELETE FROM beneficio WHERE codBen = '{codBen}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def findByCPF(self, cursor, codBen):
        try:
            sql = f"SELECT * FROM beneficio WHERE codBen = '{codBen}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            codBen, nome, valor = result
            beneficio = Beneficio(codBen, nome, valor)
            return beneficio
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):
        try:
            sql = "SELECT * FROM beneficio"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None
