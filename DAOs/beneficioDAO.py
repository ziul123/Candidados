class Beneficio():
    def __init__(self, codBen, nome, valor):
        self.codBen = codBen
        self.nome = nome
        self.valor = valor


class BeneficioDAO:
    def create(self, cursor, beneficio):
        sql = "INSERT INTO beneficio VALUES(%(codBen)s, %(nome)s, %(valor)s);"
        try:
            cursor.execute(sql, vars(beneficio))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def update(self, cursor, beneficio):
        sql = "UPDATE beneficio SET nome = %(nome)s, valor = %(valor)s \
                WHERE codBen = %(codBen)s;"
        try:
            cursor.execute(sql, vars(beneficio))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def delete(self, cursor, codBen):
        sql = "DELETE FROM beneficio WHERE codBen = %(codBen)s;"
        try:
            cursor.execute(sql, {'codBen': codBen})
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def get(self, cursor, codBen):
        sql = "SELECT * FROM beneficio WHERE codBen=%s;"
        try:
            cursor.execute(sql, (codBen,))
            result = cursor.fetchone()
            beneficio = Beneficio(*result)
            return beneficio
        except Exception as ex:
            print(ex)
        

    def getAll(self, cursor):
        sql = "SELECT * FROM beneficio;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            beneficios = [Beneficio(*x) for x in result]
            return beneficios
        except Exception as ex:
            print(ex)
