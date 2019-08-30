import random
nome = input('Informe seu nome: ')
escolha = input('Informe i para impar e p para par: ')
numero = int(input('Informe seu número: '))
computador = random.randint(1,10)
soma = numero + computador
print('Você escolheu,',numero,'e o computador,',computador)
print('A soma dos dois é',soma)
if escolha == 'i':
    if soma % 2 == 1:
        print('Você Ganhou!',nome)
    else:
        print('O computador Ganhou!')
elif escolha == 'p':
    if soma % 2 == 0:
        print('Você Ganhou!',nome)
    else:
        print('O computador Ganhou!')


