p = float(input('\ndiga o seu peso [Kg]: '))
h = float(input('diga a sua altura [m]: '))

cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'ver':'\033[1;32m', 'roxo':'\033[1;35m', 'limp':'\033[m'}

IMC = p / (h**2)

if IMC <= 18.5:
    print('\nSeu {3}IMC é {0:.1f}{4}. Logo, seu {3}peso {1:.1f} kg está abaixo do ideal para sua altura {2:.2f} m{4}'
          .format(IMC, p, h, cor['az'], cor['limp']))
elif 18.5 < IMC <= 25:
    print('\nSeu IMC é {3}{0:.1f}{4}. Logo, seu {3}peso {1:.1f} Kg está ideal para sua altura de {2:.2f} m{4}'
          .format(IMC, p, h, cor['ver'], cor['limp']))
elif 25 < IMC <=30:
    print('\nSeu {3}IMC é {0:.1f}{4}. Logo, seu {3}peso {1:.1f} Kg em {2:.2f} m{4} significa que vc está com {3}Sobrepeso{4}'
          .format(IMC, p, h, cor['amarelo'], cor['limp']))
elif 30 < IMC <= 40:
    print('\nSeu {3}IMC é {0:.1f}{4}. Logo, seu {3}peso {1:.1f} Kg em {2:.2f} m{4} significa que vc apresenta {3}Obesidade{4}'
          .format(IMC, p, h, cor['roxo'], cor['limp']))
else:
    print('\nSeu {3}IMC é {0:.1f}{4}. Logo, seu {3}peso {1:.1f} kg em {2:.2f} m{4} significa que vc apresenta {3}Obesidade Mórbida{4}'
          .format(IMC, p, h, cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today()))

