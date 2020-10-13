cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

nome = []
nota = []
boletim = []
fim = ''
cont = aluno = 0
while fim != 'N':
    print('-=' * 15)
    n = input('Nome: ').strip().title()
    n1 = float(input('N1 = '))
    n2 = float(input('N2 = '))
    nome.append(n)
    nota.append(n1)
    nota.append(n2)
    nota.append((n1+n2)/2)
    nome.append(nota[:])
    boletim.append(nome[:])
    del nome[:]
    del nota[:]
    cont += 1
    fim = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        print(cor['red'], 'Dados incorretos. ', cor['limp'], end='')
        fim = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if fim == 'N':
        break

print('-='*15)
print('Nº', ' ', 'NOME', ' '*6, 'MÉDIA')
for c in range(0,len(boletim)):
    print(cor['amarelo'], f'{c:<2}   {boletim[c][0]:<10}   {boletim[c][1][2]:<10.1f}', cor['limp'])
print('-='*15)

print(f'boletim {len(boletim)} elementos ', boletim)
for c in range(0, len(boletim)):
    print('boletim ', boletim[c])

while aluno != 999:
    print('-=' * 15)
    aluno = int(input(f'Mostrar nota de qual dos {cont} alunos? [999 encerra] '))
    if aluno == 999:
        break
    for c in range(0, len(boletim)):
        if aluno == c:
            print(f'Notas de {cor["amarelo"]}{boletim[c][0]} = {boletim[c][1][0]} e {boletim[c][1][1]}{cor["limp"]} '
                  f'| {cor["amarelo"]}Média = {boletim[c][1][2]:.1f}{cor["limp"]}')

from datetime import date
print(f'\nProcessado em {date.today()}')

