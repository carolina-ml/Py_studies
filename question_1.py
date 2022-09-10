import math

# Faça um programa que peça ao usuário um número e imprima todos os números de um até o número que o usuário informar.

qualquer_numero = int
def printar_numero(qualquer_numero):
    print(qualquer_numero)

#Imprime resultado na tela
print("Todos os números até o número escolhido")
print ("")

#ou
contador=0
numero=(int(input('digite um número')))
while numero > contador:
    contador = contador + 1
    print(contador)

# Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”

intervalos=[(0,24,9),
(25, 49.9),
(50, 74.9),
(75, 100)
]
valor=(float(input('digite um número')))
for i in intervalos:
    start,end=i
    if strt <= valor < end:
        print(start,end)
    elif valor < 0:
        print('Nada para mostrar. Fora do intervalo.')
        break
    elif valor > 100:
        print('Nada para mostrar. Fora do intervalo.')
        break
