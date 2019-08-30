import random
from time import sleep
ven = []
while True:
    print('Esse jogo é serio então você tem que se comprometer com uma coisa')
    sleep(3)
    a = input('Você se compromete em colocar só numeros de 1 a 10 sem que coloque um acima ou outro abaixo?[s/n]')
    if a == 'n':
        print('Então passar bem!')
        break
    elif a == 's':
        tudov = 0
        tudoc = 0
        nome = input('Informe seu nome: ')
        quanto = int(input('Informe quantas rodada deseja jogar: '))
        for i in range(0, quanto):
            i += 1
            print('-=' * 20)
            print('Rodada',i)
            escolha = input('Informe se quer par(p) ou impar(i) se colocar uma opção inválida vai ponto pro computador: ')
            if escolha == 'i' or escolha == 'p':
                numero = int(input('Informe o número que você escolhe: '))
                print(nome,'você escolheu',numero)
                computador = random.randint(1,10)
                print('O Computador escolheu',computador)
                soma = numero + computador

                if escolha == 'i':
                    if soma % 2 == 1:
                        print('Processando as informações...')
                        sleep(2)
                        print('então...')
                        sleep(1)
                        print('O vencedor é...')
                        sleep(1)
                        print('##########')
                        print(nome)
                        print('##########')
                        print('pois',numero, '+', computador, '=', soma, 'É um número impar!')
                        sleep(3)
                        tudov += 1
                    else:
                        print('processando as informações...')
                        sleep(2)
                        print('então...')
                        sleep(1)
                        print('O vencedor é...')
                        sleep(1)
                        print('##############')
                        print('O Computador')
                        print('##############')
                        print('pois',numero, '+', computador, '=', soma, 'É um número par!')
                        sleep(3)
                        tudoc += 1
                elif escolha == 'p':
                    if soma % 2 == 0:
                        print('processando as informações...')
                        sleep(2)
                        print('então...')
                        sleep(1)
                        print('o vencedor é...')
                        sleep(1)
                        print('##########')
                        print(nome)
                        print('##########')
                        print('pois',numero, '+', computador, '=', soma, 'É um número par!')
                        sleep(3)
                        tudov += 1
                    else:
                        print('processando as informações...')
                        sleep(2)
                        print('então...')
                        sleep(1)
                        print('O vencedor é')
                        sleep(1)
                        print('##############')
                        print('O Computador')
                        print('##############')
                        print('pois',numero, '+', computador, '=', soma, 'É um número impar!')
                        sleep(3)
                        tudoc += 1
            else:
                print('Opção Inválida!')
                sleep(1)
                print('O computador ganhou um ponto!')
                sleep(3)
                tudoc += 1
                print('-=' * 100)

    while True:
        print('#######################################')
        print('# 1 - Ver resultado desse jogo!       #')
        print('# 2 - Ver lista de ganhadores do dia! #')
        print('# 3 - Jogar Novamente!                #')
        print('# 4 - SAIR                            #')
        print('#######################################')
        op = int(input('Informe uma opção do quadro: '))
        if op == 1:
            print(nome,'ganhou',tudov,'vezes!')
            print('O Computador ganhou',tudoc,'vezes!')
            if tudoc > tudov:
                print('O computador venceu!')
                ven.append('computador')
            elif tudov > tudoc:
                print(nome,'venceu!')
                ven.append(nome)
            else:
                print('Impataram!!!')
            print('Obrigado por usar esse programa,',nome)
            print('-=' * 20)
        elif op == 2:
            print(ven)
            print('-=' * 20)
        elif op == 3:
            print('Vamos começar do início!')
            print('Aguarde um pouquinho...')
            sleep(5)
            print('Agora sim!')
            sleep(1)
        elif op == 4:
            print('Obrigado por usar esse programa,', nome)
            break
        else:
            print('Opção Inválida!')
            print('Digite "s" para sim ou "n" para não!')
    break
