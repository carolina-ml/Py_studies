dicionario={'nome': 'carol', 'idade':25, 'altura': 1.64}
print(dicionario)
print(dicionario['nome'])

# adicionar elementos a um dict

dicionario['programador'] = True

# Sobre escreve automatico

dicionario['altura'] = 2

# iterate a dict: as chaves sao acessadas
for variavel in dicionario:
    print(variavel)