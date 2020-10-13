n = int(input('\ndiga o 1º número: '))

cor = {'roxo':'\033[1;35m', 'limp':'\033[m'}

print('\n o seu dobro será {2}{0:>11}{4} \n e o seu triplo será {2}{1:>8}{4} \n e a raiz quadrada '
      'será {2}{3:>5.3f}{4}'.format(2*n, 3*n , cor['roxo'], n**(1/2), cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))

