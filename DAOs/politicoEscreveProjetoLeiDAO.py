class PoliticoEscreveProjetoLeiDAO:
    def create(self, cursor, politicoCPF, projetoLeiNumProj):
        sql = "INSERT INTO politicoEscreveProjetoLei VALUES(%s, %s);"
        try:
            cursor.execute(sql, (politicoCPF, projetoLeiNumProj))
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, politicoCPF, projetoLeiNumProj):
        sql = "DELETE * FROM politicoEscreveProjetoLei WHERE (politicoCPF=%s AND projetoLeiNumProj=%s);"
        try:
            cursor.execute(sql, (politicoCPF, projetoLeiNumProj))
        except Exception as ex:
            print(ex)
