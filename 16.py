#FAça um programa que receba um numero inteiro e positivo.
#TODO: Se for primo imprima a serie de fibonacci
#se o numero foi impar, impra seu antecessores em ordem decrescente até zero.
#se for par, imprima a soma de todos os numeros primos entre este numero e zero

numero = int(input("Digite um número: "))

#Para numeros PARES
if numero % 2 == 0 or numero == 2:
    print(f"{numero} é um número PAR e a soma dos numeros PRIMOS entre 0 e {numero} é de: ", end="")
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
    print(soma)
else:
    #numero impar PRIMO
    antecessor = numero
    quant_divisores = 0
    while antecessor > 0:
        if numero % antecessor == 0:
            quant_divisores +=1
        antecessor -= 1
    if quant_divisores == 2:

    # sequencia fibonacci:
        termo1 = 1
        termo2 = 1
        termo3 = 0
        print(termo1,",", termo2, end=", ")
        while True:
            #print(termo3, end=", ")
            termo3 = termo1 + termo2
            termo1 = termo2
            termo2 = termo3

            if termo3 > numero:
                break
            print(termo3, end=", ")


    #Numeros impares NAO PRIMO
    else:
        print(f"{numero} é um número IMPAR e seus antecessores são: ")
        while numero >= 0:
            print(numero, end=", ")
            numero -= 1