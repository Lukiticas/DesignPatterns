from abc import ABCMeta, abstractclassmethod
class EDUO(metaclass = ABCMeta):
    @abstractclassmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractclassmethod
    def aprova(self, orcamento):
        pass

    @abstractclassmethod
    def reprova(self, orcamento):
        pass
    
    @abstractclassmethod
    def finaliza(self, orcamento):
        pass
    
class Em_aprovacao(EDUO):
    def aplica_desconto_extra(self, orc):
        desconto = orc.valor * 0.02
        orc.adiciona_desconto_extra(desconto)
    
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()
    
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
    
    def finaliza(self, orcamento):
        raise Exception("Orçamento em aprovação não podem ir para finalizado")
 
class Aprovado(EDUO):
    def aplica_desconto_extra(self, orc):
        desconto = orc.valor*0.05
        orc.adiciona_desconto_extra(desconto)

    def aprova(self, orcamento):
        raise Exception("Orçamento já está aprovado")
    
    def reprova(self, orcamento):
        raise Exception("Orçamentos aprovados não podem ser reprovados")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(EDUO):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos reprovados não recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orçamentos reprovados não podem ser aprovados")

    def reprova(self, orcamento):
        raise Exception("Orçamento reprovado não pode ser reprovado novamente")
    
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(EDUO):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orçamentos finalizados não recebem desconto extra")
    
    def aprova(self, orcamento):
        raise Exception("Orçamentos finalizados não podem ser aprovados novamente")
    
    def reprova(self, orcamento):
        raise Exception("Orçamentos finalizados não podem ser reprovados")
    
    def finaliza(self, orcamento):
        raise Exception("Orçamentos finalizados já estão finalizados")