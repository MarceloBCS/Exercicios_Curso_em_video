cor = {'red':'\033[1;31m', 'ver':'\033[1;32m', 'limp':'\033[m', 'amarelo':'\033[1;33m'}

cad = dict()
cad['nome'] = input('Nome: ').strip().title()
cad['media'] = float(input(f'media de {cad["nome"]}: '))

print('-='*15)
print(f'O nome é {cad["nome"]}')
print(f'A média = {cad["media"]}')

if cad['media'] < 5:
    cad['sit'] = 'Reprovado'
    print(f'A situação do {cad["nome"]} é {cor["red"]}{cad["sit"]}{cor["limp"]}')
elif 5 <= cad['media'] < 7:
    cad['sit'] = 'Recuperação'
    print(f'A situação do {cad["nome"]} é {cor["amarelo"]}{cad["sit"]}{cor["limp"]}')
else:
    cad['sit'] = 'Aprovado'
    print(f'A situação do {cad["nome"]} é {cor["ver"]}{cad["sit"]}{cor["limp"]}')
print('-='*15)
print(cad)
print('-='*15)

from datetime import date
print(f'\nProcessado em {date.today()}')