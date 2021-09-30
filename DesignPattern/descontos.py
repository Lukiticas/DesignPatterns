class semNada:
    def calcula(self, orcamento):
        return 0

class descontoCinco:
    def __init__(self, prox):
        self._proximo = prox 

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self._proximo.calcula(orcamento)

class descontoQinhentos:
    def __init__(self, prox):
        self._proximo = prox 

    def calcula(self, orcamento):
        if orcamento.valor >= 500:
            return orcamento.valor * 0.07
        else:
            return self._proximo.calcula(orcamento)
