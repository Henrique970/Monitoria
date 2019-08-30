a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))

while a < b:
    a += 1
    if a < b:
        if a % 2 == 1:
            print(f'{a} ',end="")
    else:
        pass
while a > b:
    b += 1
    if b < a:
        if b % 2 == 1:
            print(f'{b} ',end="")
    else:
        pass