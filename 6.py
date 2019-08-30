numero = 2
soma = 0
while numero <= 100:
    anterior = numero
    divisores = 0

    while anterior > 0:
        if numero % anterior == 0:
            divisores += 1
        anterior -= 1
    if divisores == 2:
        soma += numero
    numero += 1
print(soma)
