cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

tot_mais18 = tot_homem = tot_mulher_menos20 = 0
parada = False

while parada == False:
    print('\n', '-='*5, 'teste_lista de Pessoas', '-='*5)
    idade = int(input('Diga a idade: '))

    sexo = input('Diga o sexo: [M/F] ').strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = input('Dado inválido. Diga o sexo: [M/F] ').strip().upper()[0]

    fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    while fim != 'S' and fim != 'N':
        fim = input('Dado inválido. Quer continuar? [S/N]  ').strip().upper()[0]

    if idade > 18:
        tot_mais18 += 1
    if sexo == 'M':
        tot_homem += 1
    elif sexo == 'F' and idade < 20:
        tot_mulher_menos20 += 1

    if fim == 'N':
        break

print('\n*** Relatório das Pessoas Cadastradas ***')
print(cor['amarelo'], f'Pessoas com mais de 18 anos = {tot_mais18}')
print(f' Homens cadastrados = {tot_homem}')
print(f' Mulheres com menos 20 anos = {tot_mulher_menos20}', cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')

