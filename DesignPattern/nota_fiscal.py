from datetime import date
from observadores import obs

class Item:
    def __init__(self, descricao, valor):
        self._descricao =  descricao
        self._valor = valor 

    @property
    def descricao(self):
        return self._descricao
    
    @property
    def valor(self):
        return self._valor 
    
class Nota_fiscal:
    
    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=[]):
        self._razao_social = razao_social
        self._cnpj = cnpj
        self._data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception("Detalhes da nota não podem ter mais que 20 caracteres") 
        self._detalhes = detalhes
        self._itens = itens

        for observador in observadores:
            observador(self)


    
    @property
    def razao_social(self):
        return self._razao_social
    
    @property
    def cnpj(self):
        return self._cnpj
    
    @property
    def data_de_emissoa(self):
        return self._data_de_emissao
    
    @property
    def detalhes(self):
        return self._detalhes

if __name__ == "__main__":
    itens = [Item("item A", 100), Item("Item B", 200)]

    nota_fiscal = Nota_fiscal("FHA SDKS", "01234567890123", itens, date.today(),"", observadores=[obs().imprime,
        obs().envia_por_email,
        obs().salva_no_banco])
            
