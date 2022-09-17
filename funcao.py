def saudações(nome, curso):
    print(f'Seja bem-vinde, {nome}!')
    print(f'Olá! é muito bom ver voce fazendo parte do melhor curso de {nome} do mundo!')

#parametros:(nome, curso)

saudações('Carol', 'Python')

# funções com retorno, não imprimir a soma dentro

def soma(num1,num2):
    return num1 + num2

    #depois de usar o return nada mais vai retornar, usar so no final
resultado = soma(5,7)
print('o resultado da soma é', resultado)

def calculadora(num1,num2,operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado2 = calculadora(10, 10) 
print(resultado2)