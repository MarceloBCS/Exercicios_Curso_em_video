import datetime

cor = {'az':'\033[1;34m', 'roxo':'\033[1;35m', 'limp':'\033[m'}

letra = input('Diga [M] masculino ou [F] feminino: ').strip().upper()[0]

while letra not in 'MF':
    letra = input('Dados inválidos. Digite [M] masculino ou [F] feminino: ').strip().upper()[0]

if letra == 'M':
    print(cor['az'], '\nO sexo digitado foi Masculino', cor['limp'])
if letra == 'F':
    print(cor['roxo'], '\nO sexo digitado foi Feminino', cor['limp'])

print('\nProcessado em {}'.format(datetime.date.today()))

