def mensagem(txt):
    print('-='*10)
    print(txt)
    print('-='*10)


def soma(a, b):
    print(a+b)


def som_pac(*tam):
    s = 0
    for c in tam:
        s += c
    print(f'somando os {tam} é {s}')


def contador(*num):
    for c in num:
        print(num, end='')
        print(c, end=' | ')
    print()


def dobravalor(*lis):
    alista = []
    for k, v in enumerate(lis):
        #print(f'lis{k} = {2*v}', end=' | ')
        alista.append(2*lis[k])
    #print()
    print(alista)


mensagem('Python is not too easy to learn, but I will')
soma(4, 5)
soma(b=3, a=9)
contador(4, 4, 10, 1, 0)
contador(1, 3)
print()
valores = [7, 2, 5, 0, 4]
dobravalor(valores)
dobravalor(7, 2, 5, 0, 4)
print()
som_pac(4, 7, 1, 1, 9, 2, 6)
som_pac(1, 2, 5)
