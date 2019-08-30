a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))

if a == b:
    print('Não tem números entre números iguais')
while a < b:
    a += 1
    if a < b:
        print(f'{a} ',end="")
    else:
        pass
while b < a:
    b += 1
    if b < a:
        print(f'{b} ',end="")
    else:
        pass
