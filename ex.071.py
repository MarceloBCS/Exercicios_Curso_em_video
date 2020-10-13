cor = {'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'limp':'\033[m'}

print(cor['red'], '='*22)
print(f'      Bhering Bank')
print('='*24, cor['limp'])
n = int(input('Valor do Saque: R$ '))

nota50 = n // 50
resto50 = n % 50

nota20 = (resto50) // 20
resto20 = resto50 % 20

nota10 = (resto20) // 10
resto10 = resto20 % 10

nota1 = resto10

print('{1}{0:>3} nota(s){2} R$50'.format(nota50, cor['amarelo'], cor['limp']))
print('{1}{0:>3} nota(s){2} R$20'.format(nota20, cor['amarelo'], cor['limp']))
print('{1}{0:>3} nota(s){2} R$10'.format(nota10, cor['amarelo'], cor['limp']))
print('{1}{0:>3} nota(s){2} R$ 1'.format(nota1, cor['amarelo'], cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')





