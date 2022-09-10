from math import pi 

raio=float(input('Digite o raio do círculo'))
print ("A area do círculo com raio " + str(raio) + " é: " + str(pi * raio**2))

"""" 
list_letras_removidas = []
entrada1 = input('Entrada 1: ').lower().strip()
entrada2 = input('Entrada 2: ').lower().strip()
list_entrada1 = list(entrada1)
list_entrada2 = list(entrada2)

for letra in list_entrada1:
    if letra in list_entrada2:
        letra_removida = list_entrada2.pop(list_entrada2.index(letra))
        list_letras_removidas.append(letra_removida)
    else:
        break

if list_letras_removidas == list_entrada1:
    print(f'{entrada1} é subsequência de {entrada2}.')
else:
    print(f'{entrada1} não é subsequência de {entrada2}.')
"""

"""
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. 
Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.
"""
