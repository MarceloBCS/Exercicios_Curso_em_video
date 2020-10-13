n1 = float(input('\ndiga a nota da Prova1: '))
n2 = float(input('diga a nota da Prova2: '))

media = (n1 + n2)/2

cor = {'red':"\033[1;31m", 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'limp':'\033[m'}

if media < 5:
    print('\nSua média foi {1}{0}{2} e por isso, vc foi {1}REPROVADO{2} !'.format(media, cor['red'], cor['limp']))
elif 5 <= media <= 6.9:
    print('\nSua média foi {1}{0}{2} e por isso, vc está em {1}RECUPERAÇÂO{2}'.format(media, cor['amarelo'], cor['limp']))
elif 10 >= media > 6.9:
    print('\n{1}Parabéns{2}!!! Sua média foi {1}{0}{2} e vc está {1}APROVADO{2} !!!'.format(media, cor['az'], cor['limp']))
else:
    print('Vc digitou uma nota equivocada. Tente novamente')

import datetime
print('\nProcessado em {}'.format(datetime.date.today()))