cor = {'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'limp':'\033[m'}

cad = []
pessoa = dict()
cont = tot_idade = 0
while True:
    pessoa['nome'] = input('Nome: ').strip().title()
    sexo = input('Sexo: [M/F] ').strip().title()
    while sexo[0] not in 'MF':
        print(cor['red'], 'Resposta inválida. ', cor['limp'], end='')
        sexo = input('Sexo [M/F] ').strip().upper()[0]
    pessoa['sexo'] = sexo
    idade = int(input('Idade: '))
    tot_idade += idade
    pessoa['idade'] = idade
    cont += 1
    cad.append(pessoa.copy())
    fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    while fim not in 'SN':
        print(cor['red'], 'Resposta inválida. ', cor['limp'], end='')
        fim = input('Quer continuar? [S/N] ').strip().upper()[0]
    if fim == 'N':
            break
    print('-=' * 20)

print('-=' * 20)
print(cad)

print('-=' * 20)
print(f'\nA) Cadastradas {cor["amarelo"]}{cont} pessoas{cor["limp"]}')

print(f'B) {cor["amarelo"]}Média de idade = {tot_idade / cont:.1f} anos{cor["limp"]}')

print('C) As mulheres cadastradas foram: ', end='')
for c in range(0, len(cad)):
    if cad[c]['sexo'] == 'F':
        print(cor['amarelo'], f'{cad[c]["nome"]}', cor['limp'], end=' | ')

print('\nD) lista das pessoas que estão acima da média: ')
for c in range(0, len(cad)):
   if cad[c]['idade'] > (tot_idade / cont):
        print(cor['amarelo'], f'  → nome = {cad[c]["nome"]}; sexo = {cad[c]["sexo"]}; idade = {cad[c]["idade"]}', cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')