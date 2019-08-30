import random
print('#' * 15)
print('# 1 - Pedra   #')
print('# 2 - Papel   #')
print('# 3 - Tesoura #')
print('###############')

nome = input('Informe seu nome: ')
escolha = int(input('Informe sua escolha: '))
computador = random.randint(1,3)

if escolha == 1:
    print('Você escolheu Pedra!')
    if computador == 1:
        print('Computador escolheu Pedra')
        print('Impate!',nome)
    elif computador == 2:
        print('Computador escolheu Papel')
        print('Computador Ganhou!')
    elif computador == 3:
        print('O computador escolheu Tesoura!')
        print('Você ganhou!', nome)