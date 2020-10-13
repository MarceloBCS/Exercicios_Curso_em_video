cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Diga um número entre 0 e 20: '))
while n < 0 or n >20:
    print(cor['red'], 'Número inválido', cor['limp'], end='')
    n = int(input('Tente novamente com nº entre 0 e 20: '))

print('\nVc digitou o número {0}{1}{2}'.format(cor['amarelo'], extenso[n], cor['limp']))

from datetime import date
print(f'\nProcessado em {date.today()}')

#Para obter a posição e o nome ocupado nesta posição:
#for posicao, nome in enumerate(extenso):
#    print(f'posição {posicao} = {nome}')

#para obter a posição
#for c in range(0, len(extenso)):
#    print(c)







