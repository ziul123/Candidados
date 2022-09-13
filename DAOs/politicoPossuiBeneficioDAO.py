class PoliticoPossuiBeneficio:

    def __init__(self, politicoCPF, beneficioCodBen):
        self.politicoCPF = politicoCPF
        self.beneficioCodBen = beneficioCodBen
    
class PoliticoPossuiBeneficioDAO:

    def __init__(self):
        pass

    def create(self, cursor, politicoPossuiBeneficio):

        sql = "INSERT INTO politicoPossuiBeneficio VALUES(%(politicoCPF)s, %(beneficioCodBen)s);"
        try:
            cursor.execute(sql, vars(politicoPossuiBeneficio))
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, politicoCPF, beneficioCodBen):

        sql = f"DELETE * FROM politicoPossuiBeneficio WHERE(politicoCPF = '{politicoCPF}' AND beneficioCodBen = \
            '{beneficioCodBen}');"
        try:
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def get(self, cursor, politicoCPF, beneficioCodBen):

        sql = f"SELECT * FROM politicoPossuiBeneficio WHERE(politicoCPF = '{politicoCPF}' AND beneficioCodBen = \
            '{beneficioCodBen}');"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            politicoPossuiBeneficio = PoliticoPossuiBeneficio(*result)
            return politicoPossuiBeneficio
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        
        sql = "SELECT * FROM politicoPossuiBeneficio;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            politicoPossuiBeneficio = [PoliticoPossuiBeneficio(*x) for x in result]
            return politicoPossuiBeneficio
        except Exception as ex:
            print(ex)
