'''Jogo do Pedra - Papel - Tesoura'''
from random import randint
from time import sleep
print("Computador: Olá! Vamos jogar JóKenPô 3 vezes e veremos quem é o supremo campeão!\n"
      "")
pontos_jogador, pontos_pc = 0, 0 #Só porque eu lembrei daquele dia.
for i in range(1, 4):
    pc = randint(1, 3)
    escolha_jogador = 0
    print(f"{i}º Partida\n"
          f"===]]gerhet==============\n"
          "||JÓ - KEN - PÔ||\n"
          "=================\n"
          "||Pedra    - 1 ||\n"
          "||Papel    - 2 ||\n"
          "||Tesoura  - 3 ||\n"
          "=================\n")

    while escolha_jogador not in (1, 2, 3):
        escolha_jogador = int(input("Sua escolha: "))
    if pc == 1:
        pc = "Pedra"
    if pc == 2:
        pc = "Papel"
    if pc == 3:
        pc = "Tesoura"
    if escolha_jogador == 1:
        escolha_jogador = "Pedra"
    if escolha_jogador == 2:
        escolha_jogador = "Papel"
    if escolha_jogador == 3:
        escolha_jogador = "Tesoura"

    print("")
    sleep(0.5)
    print("JÓ!", end="")
    sleep(0.5)
    print(" KEN!", end="")
    sleep(1)
    print(" PÔ!")
    print("")
    print(f"Jogador escolheu [ {escolha_jogador} ] e o Computador escolheu [ {pc} ]. ", end="")
    if escolha_jogador == "Pedra" and pc == "Papel":
        print("Computador Ganha")
        pontos_pc += 1
    elif escolha_jogador == "Pedra" and pc == "Tesoura":
        print("Jogador Ganha")
        pontos_jogador += 1
    elif escolha_jogador == "Papel" and pc == "Tesoura":
        print("Computador Ganha")
        pontos_pc += 1
    elif escolha_jogador == "Papel" and pc == "Pedra":
        print("Jogador Ganha")
        pontos_jogador += 1
    elif escolha_jogador == "Tesoura" and pc == "Pedra":
        print("Computador Ganha")
        pontos_pc += 1
    elif escolha_jogador == "Tesoura" and pc == "Papel":
        print("Jogador Ganha")
        pontos_jogador += 1
    else:
        print("Deu empate")
    print("-=" * 30)
    print("")
print("-=-=-=-=-=-=-=-=FIM=-=-=-=-=-=-=-=-")
print(f"Pontuação:\n"
      f"Jogador: {pontos_jogador}\n"
      f"Computador: {pontos_pc}")
if pontos_pc > pontos_jogador:
    print("O Computador é o vencedor")
elif pontos_jogador > pontos_pc:
    print("O Jogador é o vencedor")
else:
    print("Deu uma puta cagada de empate")