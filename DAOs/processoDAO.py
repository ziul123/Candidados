class Processo:
    def __init__(self, numProc, andamento, dataInicio, autor, resultado):
        self.numProc = numProc
        self.andamento = andamento
        self.dataInicio = dataInicio
        self.autor = autor
        self.resultado = resultado


class ProcessoDAO:

    def create(self, cursor, processo):
        try:
            sql = "INSERT INTO processo VALUES(%(numProc)s, %(andamento)s, %(dataInicio)s, %(autor)s, %(resultado)s);"
            cursor.execute(sql, vars(processo))
        except Exception as ex:
            print(ex)


    def update(self, cursor, processo):
        try:
            sql = ("UPDATE processo SET andamento=%(andamento)s, dataInicio=%(dataInicio)s, "
                    "autor=%(autor)s, resultado=%(resultado)s WHERE numProc=%(numProc)s;")
            cursor.execute(sql, vars(processo))
        except Exception as ex:
            print(ex)

    def delete(cursor, numProc):
        pass

    def get(self, cursor, numProc):
        try:
            sql = "SELECT * FROM processo WHERE numProc=%(numProc)s"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)
            return None

    def getAll(cursor):
        try:
            sql = "SELECT * FROM processo;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as ex:
            print(ex)
            return None
