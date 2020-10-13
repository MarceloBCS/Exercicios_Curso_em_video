cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

def area(l, c):
    print(f'A área do terreno {l}x{c} é {cor["amarelo"]}{l*c}m2{cor["limp"]}')


print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)

from datetime import date
print(f'\nProcessado em {date.today()}')
