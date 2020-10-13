cor = {'red':'\033[1;31m', 'limp':'\033[m'}

menor = maior = contador = soma = 0
n = 1

while n != 0:
    contador += + 1
    n = int(input('digite um número inteiro qualquer ou digite [0] para sair: '))
    if contador == 1 and n != 0:
        menor = maior = n
    if n < menor and n != 0:
        menor = n
    elif n > maior and n != 0:
        maior = n
    soma += n

if contador == 1:
    media = 0
else:
    media = soma / (contador-1)

print('{3}nº digitados = {0} \nMenor = {1} \nMaior = {2}'.format(contador-1, menor, maior, cor['red']))
print('Média = {0:.2f}{1}'.format(media, cor['limp']))

from datetime import date
print('\nProcessado em {}'.format(date.today()))



