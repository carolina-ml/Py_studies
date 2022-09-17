#Criando listas - lista = []


lista_de_listas = [10, [9,5,3]]

lista=[3.5,6.8,9.1, 60, 34, 27]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[:3])
print(lista[3:1:6])
print(lista[4:8])

# usando os elementos da lista, percorrer por cada elemento

for elemento in lista:
    print(elemento)

# usando os índices

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(i)
