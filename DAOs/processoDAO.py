class Processo:
    def __init__(self, numProc, andamento, dataInicio, autor, resultado):
        self.numProc = numProc
        self.andamento = andamento
        self.dataInicio = dataInicio
        self.autor = autor
        self.resultado = resultado


class ProcessoDAO:

    def create(self, cursor, processo):
        sql = "INSERT INTO processo VALUES(%(numProc)s, %(andamento)s, %(dataInicio)s, %(autor)s, %(resultado)s);"
        try:
            cursor.execute(sql, vars(processo))
        except Exception as ex:
            print(ex)

    def update(self, cursor, processo):
        sql = ("UPDATE processo SET andamento=%(andamento)s, dataInicio=%(dataInicio)s, "
                "autor=%(autor)s, resultado=%(resultado)s WHERE numProc=%(numProc)s;")
        try:
            cursor.execute(sql, vars(processo))
        except Exception as ex:
            print(ex)

    def delete(self, cursor, numProc):
        sql = ("DELETE FROM processoPolitico WHERE processoNumProc=%(numProc)s; "
                "DELETE FROM processo WHERE numProc=%(numProc)s;")
        try:
            cursor.execute(sql, {"numProc":numProc})
        except:
            print(ex)

    def get(self, cursor, numProc):
        sql = "SELECT * FROM processo WHERE numProc=%s;"
        try:
            cursor.execute(sql, (numProc,))
            result = cursor.fetchone()
            processo = Processo(*result)
            return processo
        except Exception as ex:
            print(ex)

    def getAll(self, cursor):
        sql = "SELECT * FROM processo;"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            processos = [Processo(*x) for x in result]
            return processos
        except Exception as ex:
            print(ex)
