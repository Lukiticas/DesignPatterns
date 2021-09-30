import impostos
from impostos import ICMS, ISS, IKCV, ICPP
class CalculadorImposto(object):
    def realiza_calculo(self, orc, imposto):
        imposto_calculado = imposto.calcula(orc)
        print(imposto_calculado)

if __name__ == "__main__":
    from orcamento_novo import Orcamento, Item

    calculador = CalculadorImposto()
    orc = Orcamento()

    orc.adiciona_item(Item('Item A', 50))
    orc.adiciona_item(Item('Item B', 200))
    orc.adiciona_item(Item('Item C', 250))
        
    calculador.realiza_calculo(orc, ICPP())
    calculador.realiza_calculo(orc, IKCV())
    calculador.realiza_calculo(orc, IKCV(ICPP()))