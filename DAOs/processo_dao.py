class Processo:
    def __init__(self, NumProc, Vara, Andamento, DataInicio, Autor, Resultado):
        self.NumProc = NumProc
        self.Vara = Vara
        self.Andamento = Andamento
        self.DataInicio = DataInicio
        self.Autor = Autor
        self.Resultado = Resultado


class ProcessoDAO:
    def get_all(cursor):
        sql = "SELECT * FROM Processo;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def get(cursor, NumProc):
        sql = "SELECT * FROM Processo WHERE NumProc=%s"
        cursor.execute(sql, (NumProc,))
        result = cursor.fetchall()
        return result

    def insert(cursor, processo):
        sql = "INSERT INTO Processo VALUES(%(NumProc)s, %(Vara)s, %(Andamento)s, %(DataInicio)s, %(Autor)s, %(Resultado)s);"
        cursor.execute(sql, vars(processo))

    def update(cursor, processo):
        sql = ("UPDATE Processo SET Vara=%(Vara)s, Andamento=%(Andamento)s, DataInicio=%(DataInicio)s, "
                "Autor=%(Autor)s, Resultado=%(Resultado)s WHERE NumProc=%(NumProc)s;")
        cursor.execute(sql, vars(processo))

    def delete(cursor, NumProc):


