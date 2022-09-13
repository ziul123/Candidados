class ExerceCargoEm:

    def __init__(self, orgaoCodOrg, politicoCPF, dataEleito, nomeCargo, ambito, tempoMandato, salario):
        self.orgaoCodOrg = orgaoCodOrg
        self.politicoCPF = politicoCPF
        self.dataEleito = dataEleito
        self.nomeCargo = nomeCargo
        self.ambito = ambito
        self.tempoMandato = tempoMandato
        self.salario = salario


class ExerceCargoEmDAO:

    def __init__(self):
        pass

    def create(self, cursor, exerceCargoEm):

        try:
            data = {'orgaoCodOrg': exerceCargoEm.orgaoCodOrg, 'politicoCPF': exerceCargoEm.politicoCPF,
            'dataEleito': exerceCargoEm.dataEleito, 'nomeCargo': exerceCargoEm.nomeCargo, 'ambito': exerceCargoEm.ambito,
            'tempoMandato': exerceCargoEm.tempoMandato, 'salario': exerceCargoEm.salario}
