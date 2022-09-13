class Beneficio():
    def __init__(self, codBen, nome, valor):
        self.codBen = codBen
        self.nome = nome
        self.valor = valor

class BeneficioDAO:
    def __init__():
        pass

    def create(self, cursor, beneficio):
        sql = "INSERT INTO beneficio VALUES(%(codBen)s, %(nome)s, %(valor)s)"
        try:
            cursor.execute(sql, vars(beneficio))
        except Exception as ex:
            print(ex)

    def update(self, cursor, beneficio):
        sql = "UPDATE beneficio SET nome = %(nome)s, valor = %(valor)s \
                WHERE codBen = %(codBen)s"
        try:
            cursor.execute(sql, vars(beneficio))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codBen):
        sql = "DELETE FROM politicoPossuiBeneficio WHERE beneficioCodBen = %(codBen)s; \
                DELETE FROM beneficio WHERE codBen = %(codBen)s;"
        try:
            cursor.execute(sql, {'codBen': codBen})
        except Exception as ex:
            print(ex)

    def get(self, cursor, codBen):
        sql = f"SELECT * FROM beneficio WHERE codBen = '{codBen}'"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as ex:
            print(ex)
            return None
        
        codBen, nome, valor = result
        beneficio = Beneficio(codBen, nome, valor)
        return beneficio

    def getAll(self, cursor):
        sql = "SELECT * FROM beneficio"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
            return None

        return result
