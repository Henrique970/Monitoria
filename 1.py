a = int(input('informe  um número: '))
c = input('Informe a operaçao(+,-,*,/): ')
b = -1

while b < 10:
    b += 1
    if c == '+':
        print(a,'+',b,'=',a+b)
    elif c == '-':
        print(a,'-',b,'=',a-b)
    elif c == 'x':
        print(a,'x',b,'=',a*b)
    elif c == '/':
        if a > 0:
            print(a, '/', b, '=', a/b)
        else:
            print('Nenhum número pode ser dividido por 0')
            break
    else:
        print('Informe uma opção válida!')
        break