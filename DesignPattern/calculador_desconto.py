from descontos import descontoCinco, descontoQinhentos, semNada

class calculadorDesconto:
    def calcula(self, orc):
        desconto = descontoCinco(descontoQinhentos(semNada())).calcula(orc)
        return desconto
    
if __name__ == "__main__":
    from orcamento_novo import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    print(orcamento.valor)

    orcamento.aprova()
    orcamento.reprova()

    print(orcamento.valor)

    
    
            
        
            