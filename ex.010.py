n = float(input('\nDiga o $$$ em reais da sua carteira: '))
cambio = float(input('diga do câmbio do dia: '))
dolar = n / cambio

cor = {'amarelo':'\033[1;33m', 'azul':'\033[1;34m', 'limp':'\033[m'}

print('\no valor {2}R$ {0:<10.2f}{4}\n  será  {3}U$ {1:<10.2f}{4}'.format(n, dolar, cor['amarelo'], cor['azul'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))


