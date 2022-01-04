class Chocolate:
  origem_cacau ='Bahia' 
  #atributo da classe
  #init é a factory dessa classe
  def __init__(self, porcentagem_cacau, peso):
    self.porcentagem_cacau = porcentagem_cacau
    self.peso = peso

    #Método da classe
  def derreter(temperatura):
    print(f'Derreteu ao chegar em: {temperatura}')
            
  def retorna_porcentagem_de_cacau(self):
    return self.porcentagem_cacau

  def printa_informacoes(self):
    print(self.peso, self.porcentagem_cacau)

#a factory retorna uma instância da classe chocolate == objeto
mil_folhas = Chocolate('75%', '50g')
trufa = Chocolate('55%', '20g')


mil_folhas.printa_informacoes()
trufa.printa_informacoes()
print(mil_folhas.origem_cacau)



#print(mil_folhas.peso, mil_folhas.porcentagem_cacau)
#atributo da classe
#print(Chocolate.porcentagem_de_cacau)
#atributo do objeto
#print(mil_folhas.porcentagem_de_cacau)

#invocando um método
#Chocolate.derreter(19)python

#mil_folhas.retorna_porcentagem_de_cacau()