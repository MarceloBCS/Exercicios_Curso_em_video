cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}
fator = 0

while True:
    print(cor['amarelo'], '-*' * 28, cor['limp'])
    n = int(input(' Tabuada de qual valor ou digite nº negativo para sair: '))
    print(cor['amarelo'], '-*' * 28, cor['limp'])
    if n < 0:
        break
    while fator < 10:
        fator += 1
        print(' {0} x {1:>2} = {2:>2}'.format(n, fator, n*fator))
    fator = 0

from datetime import date
print(f'\nProcessado em {date.today()}')