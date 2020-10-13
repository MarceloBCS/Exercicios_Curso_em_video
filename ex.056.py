import datetime

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

media = 0
soma_idade = 0
idade_anterior_h = 0
tot_genero_m = 0

for c in range(1,5):
    nome = input('Diga o seu nome: ').strip()
    idade = int(input('Diga a sua idade: '))
    sexo = input('Diga o seu gênero: [H] ou [M] ').strip()
    print('-='*15)

    if sexo.upper() == 'H' and idade > idade_anterior_h:
        idade_anterior_h = idade
        h_velho = nome

    if sexo.upper() == 'M' and idade < 20:
        tot_genero_m += 1     #tot_genero_m = tot_genero_m + 1

    soma_idade += idade     #soma_idade = soma_idade + idade

media = soma_idade / c      # Tire do laço para evitar trabalho desnecessário da CPU

print(cor['amarelo'], 'Homem mais velho é o {0}. Ele tem {1} anos'.format(h_velho, idade_anterior_h ))
print(' idade média do grupo = {:.1f}'.format(media))
print(' Nº de mulheres < 20 = ', tot_genero_m, cor['limp'])

print('\nProcessado em {}'.format(datetime.date.today()))