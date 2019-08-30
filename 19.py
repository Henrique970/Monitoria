# TODO: Faça um programa que imprima os números de 1 a 10
# TODO: e mostre a soma dos impares e a média dos pares usando for
soma = 0
media = 0
for i in range(1,11):
    print(i)
for impar in range(1,11,2):
    soma += impar
print('A soma dos impares é:',soma)
for par in range(2,11,2):
    soma += par
    media = soma / par
print('A média dos pares é:',media)
    