nome = "claudia"

def primeira_caps(nome):
    for letra in nome:
    # se a letra for igual a primeira letra do nome
        if letra == nome[0]:
            print(nome[0].upper())
        else:
            print(letra)
            
primeira_caps(nome)