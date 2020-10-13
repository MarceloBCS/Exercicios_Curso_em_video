import datetime

cor = {'yellow':'\033[1;33m', 'limp':'\033[m'}

contador_numeros = 0
s = 0
for c in range(3,500,3):
    if c % 2 == 1:
        s += + c                    # é igual s = s + c
        contador_numeros += + 1     #equivalente a contador_numeros = contador_numeros + 1

print('{1}Soma = {0}{2}'.format(s, cor['yellow'], cor['limp']))
print('Foram encontrados e usados {1}{0} números{2}'.format(contador_numeros, cor['yellow'], cor['limp']))

print('\nProcessador em {}'.format(datetime.date.today()))