a = float(input('1º número: '))
b = float(input('2º número: '))
c = float(input('3º número: '))

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

s = [a, b, c]

maior = max(s)
menor = min(s)

print('\nfunção MIN => menor número é {}'. format(menor))
print('função MAX => maior número é {}'.format(maior))
print('\n', cor['red'], '#'*20, cor['limp'], '\n')


# 2ºforma = aprendida nos comentários
a = float(input('1º número: '))
b = float(input('2º número: '))
c = float(input('3º número: '))

lista = [a, b, c]
lista_ordenada = sorted(lista)

print('\nLista ordenada ---> O menor é: {}'.format(lista_ordenada[0]))
print('lista ordenada ---> O maior é: {}'.format(lista_ordenada[-1]))
print('\n', cor['red'], '*'*20, cor['limp'], '\n')


# 3ºforma de fazer a mesma tarefa, mas coloquei tudo junto para enfeitar o ganso

if a > b and a > c and b > c:
    print('\n maior = {0} e o menor= {1}'.format(a, c))
elif a > b and a > c and b < c:
    print('\n maior = {0} e o menor= {1}'.format(a, b))
elif a > b and a < c:
    print('\n maior = {0} e o menor= {1}'.format(c, b))
elif a < b and a < c and b > c:
    print('\n maior = {0} e o menor= {1}'.format(b, a))
elif a < b and a > c and b > c:
    print('\n maior = {0} e o menor= {1}'.format(b, c))
elif a < b and b < c:
    print('\n maior = {0} e o menor= {1}'.format(c, a))
elif a == b < c:
    print('\n maior = {0} e o menor= {1}'.format(c, a))
elif a == b > c:
    print('\n maior = {0} e o menor= {1}'.format(a, c))
elif b == c < a:
    print('\n maior = {0} e o menor= {1}'.format(a, b))
elif b == c > a:
    print('\n maior = {0} e o menor= {1}'.format(b, a))
elif a == c < b:
    print('\n maior = {0} e o menor= {1}'.format(b, a))
elif a == c > b:
    print('\n maior = {0} e o menor= {1}'.format(a, b))
elif a == b == c:
    print('\n todos os números são iguais a {}'.format(a))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
