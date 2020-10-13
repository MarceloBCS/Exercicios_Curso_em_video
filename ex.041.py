import datetime

nascimento = int(input('\ndiga o ano do seu nacimento: '))

cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'roxo':'\033[1;35m', 'verde':'\033[1;32m', 'limp':'\033[m'}

hoje = datetime.date.today().year
cat = hoje - nascimento

if cat <= 9:
    print('\nSua idade é {1}{0} anos{2} =-> categoria {1}Mirim{2}'.format(cat, cor['amarelo'], cor['limp']))
elif 9 < cat <=14:
    print('\nSua idade é {1}{0} anos{2} =-> categoria {1}Infantil{2}'.format(cat, cor['verde'], cor['limp']))
elif 14 < cat <= 19:
    print('\nSua idade é {1}{0} anos{2} =-> categoria {1}Junior{2}'.format(cat, cor['az'], cor['limp']))
elif 19 < cat <= 20:
    print('\nSua idade é {1}{0} anos{2} =-> categoria {1}Sênior{2}'.format(cat, cor['roxo'], cor['limp']))
else:
    print('\nSua idade é {1}{0} anos{2} =-> categoria {1}Master{2}'.format(cat, cor['red'], cor['limp']))

print('\nProcessador em {}'.format(datetime.date.today()))