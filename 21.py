import random
nome = input('Informe o seu nome: ')
qt = int(input('Informe a quantidade de partidas que você que jogar: '))
quantidade_jogador = 0
quantidade_computador = 0
for n in range(1, qt + 1):
    escolha = input('Escolha se quer par ou impa[p/i]: ')
    numero = int(input('Informe o número: '))
    computador = random.randint(1,10)

    print('O computador escolheu,',computador)

    soma = numero + computador

    if escolha == 'p':
        if soma % 2 == 0:
            print('Você Ganhou',nome)
            quantidade_jogador = quantidade_jogador + 1
        else:
            print('Você perdeu',nome)
            quantidade_computador += 1
    elif escolha == 'i':
        if soma % 2 == 1:
            print('Você Ganhou',nome)
            quantidade_jogador += 1
        else:
            print('Você perdeu',nome)
            quantidade_computador += 1

print('Você ganhou',quantidade_jogador,'vezes')
print('O computador ganhou',quantidade_computador,'vezes')
