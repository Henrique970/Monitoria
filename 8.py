a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))

resu = 1
while b > 0:
    resu *= a
    b -= 1
print(resu)
