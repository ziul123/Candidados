class ProcessoPoliticoDAO:
    def create(self, cursor, processoNumProc, politicoCPF):
        sql = "INSERT INTO processoPolitico VALUES(%s, %s);"
        try:
            cursor.execute(sql, (processoNumProc, politicoCPF))
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, processoNumProc, politicoCPF):
        sql = "DELETE * FROM processoPolitico WHERE(processoNumProc = %s AND \
            politicoCPF = %s;"
        try:
            cursor.execute(sql, (processoNumProc, politicoCPF))
        except Exception as ex:
            print(ex)
