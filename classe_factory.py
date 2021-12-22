#def Fabrica_chocolate_branco():
  
#padrão de projeto factory
class Fabrica_de_Chocolate:
  def __init__(self, porcentagem_cacau, peso):
    self.porcentagem_cacau = porcentagem_cacau
    self.peso = peso
    

#instância de um objeto
mil_folhas = Fabrica_de_Chocolate("45%", "100g")
lingua_de_gato = Fabrica_de_Chocolate("65%", "80g")
#o self é o que torna cada chocolate diferente


print(mil_folhas.peso)
print(lingua_de_gato.peso)