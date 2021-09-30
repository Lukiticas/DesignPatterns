class obs: 
    def imprime(self, nota):
        print(f"imprimindo nota fiscal {nota.cnpj}")

    def envia_por_email(self, nota):
        print(f"enviando por email nota fiscal {nota.cnpj}")
    
    def salva_no_banco(self, nota):
        print(f"salvando no banco nota fiscal {nota.cnpj}")