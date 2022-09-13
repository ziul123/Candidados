class ProjetoLei:

    def __init__(self, numProj, descricao, dataCriacao, aprovacao):
        self.numProj = numProj
        self.descricao = descricao
        self.dataCriacao = dataCriacao
        self.aprovacao = aprovacao

class ProjetoLeiDAO:

    def __init__(self):
        pass

    def create(self, cursor, projetoLei):

        try:
            data = {'numProj': projetoLei.numProj, 'descricao': projetoLei.descricao,
            'dataCriacao': projetoLei.dataCriacao, 'aprovacao': projetoLei.aprovacao}
            sql = "INSERT INTO projetoLei VALUES(%(numProj)s, %(descricao)s, %(dataCriacao)s, %(aprovacao)s)"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)

    def update(self, cursor, projetoLei, numProj):

        try:
            data = {'numProj': numProj, 'descricao': projetoLei.descricao,
            'dataCriacao': projetoLei.dataCriacao, 'aprovacao': projetoLei.aprovacao}
            sql = "UPDATE projetoLei SET descricao = %(descricao)s, dataCriacao = %(dataCriacao)s \
                aprovacao = %(aprovacao)s WHERE numProj = %(numProj)s"
            cursor.execute(sql, data)
        except Exception as ex:
            print(ex)
        
    def delete(self, cursor, numProj):

        try:
            sql = f"DELETE * FROM projetoLei WHERE numProj = '{numProj}'"
            cursor.execute(sql)
        except Exception as ex:
            print(ex)
        
    def findById(self, cursor, numProj):

        try:
            sql = f"SELECT * FROM projetoLei WHERE numProj = '{numProj}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            numProj, descricao, dataCriacao, aprovacao = result
            projetoLei = ProjetoLei(numProj, descricao, dataCriacao, aprovacao)
            return projetoLei
        except Exception as ex:
            print(ex)
            return None

    def findAll(self, cursor):
        try:
            sql = "SELECT * FROM projetoLei"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as ex:
            print(ex)
            return None