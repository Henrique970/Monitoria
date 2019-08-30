#TODO: FAça um programa que receba um numero inteiro e positivo.
#TODO: Se for primo imprima a serie de fibonacci
#TODO: se o numero foi impar, impra seu antecessores em ordem decrescente até zero.
#TODO: se for par, imprima a soma de todos os numeros primos entre este numero e zero

numero = int(input('Informe um número: '))

"""if numero % 2 == 1:
    contador = 0
    while numero >= contador:
        print(f'{numero}', end=" ")
        numero -= 1
    print('fim')"""

"""if numero % 2 == 0:
    primos = numero
    soma = 0
    while primos != 0:
        antecessor = primos
        quant_divisores = 0
        while antecessor > 0:
            if primos % antecessor == 0:
                quant_divisores += 1
            antecessor -= 1
        if quant_divisores == 2:
            soma += primos
        primos -= 1
    print(soma)"""

antecessor = numero
quant_divisores = 0
while antecessor > 0:
    if numero % antecessor == 0:
        quant_divisores +=1
    antecessor -= 1
if quant_divisores == 2:

    termo1 = 1
    termo2 = 1
    termo3 = 0
    print(termo1,",", termo2, end=" ")
    while True:
        termo3 = termo1 + termo2
        termo1 = termo2
        termo2 = termo3

        if termo3 > numero:
            break
        print(termo3, end=" ")


