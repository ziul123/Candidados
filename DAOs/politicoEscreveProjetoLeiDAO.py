class PoliticoEscreveProjetoLei:

    def __init__(self, politicoCPF, projetoLeiNumProj):
        self.politicoCPF = politicoCPF
        self.projetoLeiNumProj = projetoLeiNumProj
    
class PoliticoEscreveProjetoLeiDAO:

    def __init__(self):
        pass

    def create(self, cursor, politicoEscreveProjetoLei):

        sql = "INSERT INTO politicoEscreveProjetoLei VALUES(%(politicoCPF)s, %(projetoLeiNumProj)s);"
        try:
            cursor.execute(sql, vars(politicoEscreveProjetoLei))
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, politicoCPF, projetoLeiNumProj):

        sql = f"DELETE * FROM politicoEscreveProjetoLei WHERE(politicoCPF = '{politicoCPF}' AND projetoLeiNumProj = \
            '{projetoLeiNumProj}');"
        try:
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def get(self, cursor, politicoCPF, projetoLeiNumProj):

        sql = f"SELECT * FROM politicoEscreveProjetoLei WHERE(politicoCPF = '{politicoCPF}' AND projetoLeiNumProj = \
            '{projetoLeiNumProj}');"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            politicoEscreveProjetoLei = PoliticoEscreveProjetoLei(*result)
            return politicoEscreveProjetoLei
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        
        sql = "SELECT * FROM politicoEscreveProjetoLei;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            politicoEscreveProjetoLei = [PoliticoEscreveProjetoLei(*x) for x in result]
            return politicoEscreveProjetoLei
        except Exception as ex:
            print(ex)
