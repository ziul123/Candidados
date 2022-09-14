class ProcessoPolitico:

    def __init__(self, processoNumProc, politicoCPF):
        self.processoNumProc = processoNumProc
        self.politicoCPF = politicoCPF
    
class ProcessoPoliticoDAO:

    def __init__(self):
        pass

    def create(self, cursor, processoPolitico):

        sql = "INSERT INTO processoPolitico VALUES(%(processoNumProc)s, %(politicoCPF)s);"
        try:
            cursor.execute(sql, vars(processoPolitico))
        except Exception as ex:
            print(ex)
    
    def delete(self, cursor, processoNumProc, politicoCPF):

        sql = f"DELETE * FROM processoPolitico WHERE(processoNumProc = '{processoNumProc}' AND \
            politicoCPF = '{politicoCPF})';"
        try:
            cursor.execute(sql)
        except Exception as ex:
            print(ex)

    def get(self, cursor, processoNumProc, politicoCPF):

        sql = f"SELECT * FROM processoPolitico WHERE(processoNumProc = '{processoNumProc}' AND \
            politicoCPF = '{politicoCPF})';"
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            processoPolitico = ProcessoPolitico(*result)
            return processoPolitico
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM processoPolitico;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            processoPolitico = [ProcessoPolitico(*x) for x in result]
            return processoPolitico
        except Exception as ex:
            print(ex)
