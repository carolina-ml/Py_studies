class Chocolate:
  #atributo da classe
  #init é a factory dessa classe
  def __init__(self, porcentagem_cacau, peso):
    self.porcentagem_cacau = porcentagem_cacau
    self.peso = peso

    #Método da classe0
  def derreter(temperatura):
    print(f'Derreteu ao chegar em: {temperatura}')
            
  def retorna_porcentagem_de_cacau(self):
    return self.porcentagem_cacau

#a factory retorna uma instância da classe chocolate == objeto
mil_folhas = Chocolate('75%', '50g')
trufa = Chocolate('55%', '20g')

#atributo da classe
#print(Chocolate.porcentagem_de_cacau)
#atributo do objeto
#print(mil_folhas.porcentagem_de_cacau)

#invocando um método
#Chocolate.derreter(19)python

mil_folhas.retorna_porcentagem_de_cacau()
