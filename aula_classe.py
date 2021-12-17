class Chocolate:
    #atributo da classe
    porcentagem_de_cacau = '75%'

    #Método da classe
    def derreter(temperatura):
            print(f'Derreteu ao chegar em: {temperatura}')

#instância da classe chocolate
mil_folhas = Chocolate()

#atributo da classe
print(Chocolate.porcentagem_de_cacau)
#atributo do objeto
print(mil_folhas.porcentagem_de_cacau)

#invocando um método
Chocolate.derreter(19)