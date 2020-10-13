import datetime

n = int(input('qual o número? '))

cor = {'az':'\033[1;34m', 'red':'\033[1;31m', 'limp':'\033[m'}

t = 0

for c in range(1,n+1):
    if n % c == 0:
        t = t + 1
        print('divisor: ', c)

print('-='*6)
if t == 2:
    print('{}É primo{}'.format(cor['az'], cor['limp']))
else:
    print('{}NÃO É primo{}'.format(cor['red'], cor['limp']))

print('\nProcessado em {}'.format(datetime.date.today()))