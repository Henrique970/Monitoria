a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
div = 0
if a == b:
    print('Não tem números entre números iguais')
while a < b:
    a += 1
    if a < b:
        div = 0

        print(f'{a} ',end="")
    else:
        pass

#while numero <= 100:
 #   anterior = numero
  #  divisores = 0
   # while anterior > 0:
    #    if numero % anterior == 0:
     #       divisores += 1
      #  anterior -= 1
    #if divisores == 2:
     #   soma += numero
    #numero += 1
#print(soma)



#while b < a:
 #   b += 1
  #  if b < a:
   #     print(f'{b} ',end="")
    #else:
     #   pass

#a = int(input('Informe o primeiro número: '))
#b = int(input('Informe o segundo número: '))

#resu = 1
#while b > 0:
 #   resu *= a
  #  b -= 1
#print(resu)
