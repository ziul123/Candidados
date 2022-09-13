class ProjetoLei:

    def __init__(self, numProj, descricao, dataCriacao, aprovacao):
        self.numProj = numProj
        self.descricao = descricao
        self.dataCriacao = dataCriacao
        self.aprovacao = aprovacao

class ProjetoLeiDAO:

    def create(self, cursor, projetoLei):
        sql = "INSERT INTO projetoLei VALUES(%(numProj)s, %(descricao)s, %(dataCriacao)s, %(aprovacao)s)"
        try:
            cursor.execute(sql, vars(projetoLei))
        except Exception as ex:
            print(ex)

    def update(self, cursor, projetoLei):
        sql = ("UPDATE projetoLei SET descricao=%(descricao)s, dataCriacao=%(dataCriacao)s, " 
                "aprovacao=%(aprovacao)s WHERE numProj=%(numProj)s")
        try:
            cursor.execute(sql, vars(projetoLei))
        except Exception as ex:
            print(ex)
        
    def delete(self, cursor, numProj):
        sql = ("DELETE FROM politicoEscreveProjetoLei WHERE projetoLeiNumProj=%(numProj)s; "
                "DELETE FROM politicoVotaProjetoLei WHERE projetoLeiNumProj=%(numProj)s; "
                "DELETE FROM projetoLei WHERE numProj=%(numProj)s;")
        try:
            cursor.execute(sql, {"numProj":numProj})
        except Exception as ex:
            print(ex)
        
    def get(self, cursor, numProj):
            sql = "SELECT * FROM projetoLei WHERE numProj=%s;"
        try:
            cursor.execute(sql, (numProj,))
            result = cursor.fetchone()
            projetoLei = ProjetoLei(*result)
            return projetoLei
        except Exception as ex:
            print(ex)
            return None

    def getAll(self, cursor):
        try:
            sql = "SELECT * FROM projetoLei;"
            cursor.execute(sql)
            result = cursor.fetchall()
            projetos = [ProjetoLei(*x) for x in result]
            return projetos
        except Exception as ex:
            print(ex)
            return None
