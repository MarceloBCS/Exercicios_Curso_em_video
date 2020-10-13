import datetime

cor = {'az':'\033[1;34m', 'amarelo':'\033[1;33m', 'limp':'\033[m'}

contador_maioridade = 0
contador_minoridade = 0

for c in range(1,8):
    ano = int(input('{}º - Diga o ano de nacimento: '.format(c)))
    idade = datetime.date.today().year - ano
    if idade >= 21:
        contador_maioridade = contador_maioridade + 1
    else:
        contador_minoridade = contador_minoridade + 1

print('-='*11)
print('{2}{0} maior(es){3} de 21 anos\n{4}{1} menor(es){3} de 21 anos'.
      format(contador_maioridade, contador_minoridade, cor['az'], cor['limp'], cor['amarelo']))

print('\nProcessado em {}'.format(datetime.date.today()))

