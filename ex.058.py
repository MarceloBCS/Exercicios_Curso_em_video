import random, datetime
random.seed()
pc = random.randint(0,10)
print(pc)       # apenas para fins de testes

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

tot = 0
c = False

while c != True:
    n = int(input('\nDe [0 a 10], Tente advinhar o número que estou pensando... >>> '))
    tot += 1
    if n != pc and n > pc:
        print('Pensei num nº menor')
    elif n != pc and n < pc:
        print('Pensei num nº maior')
    if n == pc:
        c = True

print('\nParabéns!!! Vc {2}advinhou o nº {0}{3} que estava pensando em {2}{1} tentativas{3}.'
      .format(n, tot, cor['red'], cor['limp']))

print('\nProcessado em {}'.format(datetime.date.today()))

