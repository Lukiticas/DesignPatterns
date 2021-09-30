# -*- coding: UTF-8 -*-
# orcamento.py
from EDUO import *

class Orcamento(object):

    def __init__(self):

        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0
    
    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)
    
    def finaliza(self):
        self.estado_atual.finaliza(self)
    
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra
    
    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):

        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome
