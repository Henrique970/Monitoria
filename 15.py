n1 = int(input('N1:'))
n2 = int(input('N2:'))

menor = n1
maior = n2

if n1 > n2:
    maior = n1
    menor = n2

menor += 1
while menor < maior:
    print(menor)
    menor += 1