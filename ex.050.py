import datetime

cor = {'az':'\033[1;34m', 'limp':'\033[m'}

s = 0
contador = 0

for c in range(1,7):
    a = int(input('{}º número: '.format(c)))
    if a % 2 == 0:
        s += a          # é igual a S = s + a
        contador += 1   # é igual a contador = contador + 1

print('-='*15)
print('Houve {0}{3} pares{2} e eles {0}somam = {1}{2}'.format(cor['az'], s, cor['limp'], contador))

print('\nProcessado em {}'.format(datetime.date.today()))