class PoliticoPartido:

    def __init__(self, politicoCPF, partidoNumPart, dataFiliacao, cargo):
        self.politicoCPF = politicoCPF
        self.partidoNumPart = partidoNumPart
        self.dataFiliacao = dataFiliacao
        self.cargo = cargo

    def create(self, cursor, politicoPartido):

        try:
            data = {'politicoCPF': politicoPartido.politicoCPF, 'partidoNumPart': politicoPartido.partidoNumPart,
            'dataFiliacao': politicoPartido.dataFiliacao, 'cargo': politicoPartido.cargo}
            sql = "INSERT INTO politicoPartido VALUES( %(politicoCPF)s, %(partidoNumPart)s, %(dataFiliacao)s, %(cargo)s"
            cursor.execute(sql, data)