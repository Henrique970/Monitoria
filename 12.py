a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
soma = 0
while a < b:
    a += 1
    if a < b:
        if a % 2 == 0:
            soma += a
            print(f'{a} ',end="")
    else:
        pass
while a > b:
    b += 1
    if b < a:
        if b % 2 == 0:
            soma += b
            print(f'{b} ',end="")
    else:
        pass
print('   A soma dos pares é: ',soma)