class PoliticoPossuiBeneficioDAO:
    def create(cursor, politicoCPF, beneficioCodBen):
        sql = "INSERT INTO politicoPossuiBeneficio VALUES (%s, %s);"
        try:
            cursor.execute(sql, (politicoCPF, beneficioCodBen))
        except Exception as ex:
            print(ex)

    def delete(cursor, politicoCPF, beneficioCodBen):
        sql = "DELETE FROM politicoPossuiBeneficio WHERE politicoCPF=%s AND beneficioCodBen=%s;"
        try:
            cursor.execute(sql, (politicoCPF, beneficioCodBen))
        except Exception as ex:
            print(ex)
