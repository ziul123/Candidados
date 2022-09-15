class PoliticoVotaProjetoLei:
    def __init__(self, politicoCPF, projetoLeiNumProj, voto):
        self.politicoCPF = politicoCPF
        self.projetoLeiNumProj = projetoLeiNumProj
        self.voto = voto
    

class PoliticoVotaProjetoLeiDAO:
    def create(self, cursor, politicoVotaProjetoLei):
        sql = "INSERT INTO politicoVotaProjetoLei VALUES(%(politicoCPF)s, %(projetoLeiNumProj)s, %(voto)s);"
        try:
            cursor.execute(sql, vars(politicoVotaProjetoLei))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def update(self, cursor, politicoVotaProjetoLei):
        sql = ("UPDATE politicoVotaProjetoLei SET voto = %(voto)s WHERE(politicoCPF = %(politicoCPF)s AND projetoLeiNumProj = \
            %(projetoLeiNumProj})s;")
        try:
            cursor.execute(sql, vars(politicoVotaProjetoLei))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, politicoCPF, projetoLeiNumProj):
        sql = "DELETE * FROM politicoVotaProjetoLei WHERE(politicoCPF = %s AND projetoLeiNumProj = %s);"
        try:
            cursor.execute(sql, (politicoCPF, projetoLeiNumProj))
            DAOs.cnx.commit()
        except Exception as ex:
            print(ex)

    def get(self, cursor, politicoCPF, projetoLeiNumProj):
        sql = "SELECT * FROM politicoVotaProjetoLei WHERE (politicoCPF = %s AND projetoLeiNumProj = %s);"
        try:
            cursor.execute(sql, (politicoCPF, projetoLeiNumProj))
            result = cursor.fetchone()
            politicoVotaProjetoLei = PoliticoVotaProjetoLei(*result)
            return politicoVotaProjetoLei
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        
        sql = "SELECT * FROM politicoVotaProjetoLei;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            politicoVotaProjetoLei = [PoliticoVotaProjetoLei(*x) for x in result]
            return politicoVotaProjetoLei
        except Exception as ex:
            print(ex)
