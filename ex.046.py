import time, emoji, datetime

cor = {'red':'\033[1;31m', 'amarelo':'\033[7;33m', 'limp':'\033[m'}

c = int(input('diga o tempo para detonação: '))

for c in range(c, -1, -1):
    time.sleep(1)
    print(c)
print('-='*10)
print(cor['red'], emoji.emojize(':fire:'*10), cor['limp'])
print(cor['amarelo'], '!!! Detonação !!!', cor['limp'])
print(cor['red'], emoji.emojize(':fire:'*10), cor['limp'])

print('\nDetonado em {}'.format(datetime.date.today()))