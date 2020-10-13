import datetime

n = int(input('diga o número para gerar a tabuada: '))

cor = {'red':'\033[1;31m', 'limp':'\033[m'}
print(cor['red'], '-='*6, cor['limp'])

for c in range(1,11):
    print(' {0} x {1:^3} = {2:^3}'.format(n, c, n*c))

print(cor['red'], '-='*6, cor['limp'])

print('\nProcessado em {}'.format(datetime.date.today()))