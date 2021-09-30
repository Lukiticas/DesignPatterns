from abc import ABCMeta, abstractmethod

class Imposto:
    def __init__(self, outro_imposto = None):
            self._outro_imposto = outro_imposto

    def calculo_outro_imposto(self, orcamento):
        if self._outro_imposto is None:
            return 0
        else: 
            return self._outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class template(Imposto, metaclass = ABCMeta):

    def calcula(self, orcamento):
        if self.deve_usar_max(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)
    
    @abstractmethod
    def deve_usar_max(self, orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass

def IPVX(alguma_funcao_ou_metodo):
    def wrapper(self, x):
        return alguma_funcao_ou_metodo(self, x) + 50
    return wrapper

class ISS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_outro_imposto(orcamento)

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_outro_imposto(orcamento)

class ICPP(template):

    def deve_usar_max(self, orcamento):
        return orcamento.valor > 500


    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(template):           
    
    def deve_usar_max(self,orcamento):
        return orcamento.valor > 500 and self._tem_item(orcamento)
    
    def maxima_taxacao(self, orcamento):
       return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def _tem_item(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False