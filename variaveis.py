# Criando uma variável
''' Tipos de variaveis
1. int: numeros inteiros, sem decimais
ex: 0, 4, -1, 1000
2. float: números reais, com parte decimal
ex: 1.0, -2.7, 4.14
3. str: cadeias de caracteres, dados textuais
ex: ver linha 13
4. bool (Boolean): valores logicos - True or False
'''

idade = 25 
altura = 1.64
nome = 'carol'
cansada = True

# leia-se idade recebe 25

print(idade,nome)
print(type(idade))
print(type(cansada))
print(type(nome))
print(type(altura))

#input() - retorna um dado informado pelo usuário (entrada padrão) e pode receber uma str

linguagem = input('Qual a melhor linguagem de programação do mundo?')

print('você tem toda razão é', linguagem)