numero = int(input('Informe um número pra ver se é primo: '))
n = numero
quatodade_divisores = 0
while n >= 1:
    if numero % n == 0:
        quatodade_divisores += 1
    n -= 1
if quatodade_divisores > 2:
    print(f'{numero}: Não é primo!')
else:
    print(f'{numero}: É primo')
    