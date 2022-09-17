print('1. Idoso')
print('2. Cadeirante')
print('3. Gestante')
print('4. Deficiente')
print('5. NDA')

resposta = int(input('Qual sua condição? Digite apenas números: '))

if (resposta==1) or (resposta==2) or (resposta==3) or (resposta==4):
    print('Você tem preferência, Pode passar a frente!')

elif (resposta==5):
    print('Você não tem preferência, aguarde!')

else:
    print('Opção Invalida!') 