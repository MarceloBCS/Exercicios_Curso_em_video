valor = float(input('diga o valor em metros: '))

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

km = valor / 10**3
hm = valor / 10**2
da = valor / 10
dm = valor * 10
cm = valor * 10**2
mm = valor * 10**3

print('\no valor {0:^10.2f} m convertido será: \n \n {1:>10.3f} km \n {2:>10.2f} hm \n {3:>10.1f} da'.format(valor, km, hm, da))
print(cor['amarelo'], '=-'*8, cor['limp'])
print('{0:>10.0f} dm \n {1:>10.1f} cm \n {2:>10.2f} mm'.format(dm, cm, mm))

import datetime
print('\nProcessado em {0}{1}{2}'.format(cor['amarelo'], datetime.date.today().today(), cor['limp']))





