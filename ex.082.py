cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

c = 0
li_geral = []
extra_par = []
extra_impar = []

while True:
    c += 1
    print('-='*20)
    n = int(input(f'digite o {c}º número: '))
    li_geral.append(n)
    print(f'lista geral = {li_geral}')
    fim = input('Quer Continuar? [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        fim = input('Dados inválidos. Quer Continuar? [S/N] ').strip().upper()[0]
    if fim == 'N':
        break

for pos, valor in enumerate(li_geral):
    if valor % 2 == 0:
        extra_par.append(valor)
    else:
        extra_impar.append(valor)
print('-='*20)
print(f'A lista geral é {cor["amarelo"]}{li_geral}{cor["limp"]} e tem {cor["amarelo"]}{c} elementos {cor["limp"]}')
print(f'A lista com {cor["amarelo"]}pares{cor["limp"]} é {cor["amarelo"]}{extra_par}{cor["limp"]}')
print(f'A lista com {cor["amarelo"]}ímpares{cor["limp"]} é {cor["amarelo"]}{extra_impar}{cor["limp"]}')

from datetime import date
print(f'\nProcessado em {date.today()}')



