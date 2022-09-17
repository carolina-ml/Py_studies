#Métodos de listas
lista = ['teardrops', 'avalanche', 'bring me the horizon']

#append: adicionar elementos no final da lista

print('eu gosto de:', lista)

#insert: escolhe a posição que quer inserir o elemento

lista.insert(3, 'throne')

print('Depois do insert:', lista)

# extend

lista_de_musicas = ['oh no', 'there is a hell...', 'mantra']
lista.extend(lista_de_musicas)
print('Depois de extend:', lista)

# pop elimina o ultimo, quando nao especifica o indice

lista.pop()
print('lista pós-pop:', lista)

lista.pop(0)
print('lista pós-pop -com indice', lista)

# remove: diz o valor que quer remover

lista.remove('throne')

print('lista pós-remove-o elemento escolhido', lista)

# count: conta quantos elementos tem 

print('quantia de mantra na lista:', lista('mantra'))

#index: usa o indice de determinado elemento

print('índice do elemento avalanche:', lista.index('avalanche'))

#Funções para listas

# len

print(len(lista))

# sum

print(sum(lista))

# max: retorna o maior elemento

print('maior elemento da lista':max(lista))
# min: retorna o menor elemento

print('menor elemento da lista':imin(lista))