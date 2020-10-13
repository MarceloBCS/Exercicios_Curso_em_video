cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m', 'az':'\033[1;34m'}

tot_cad = 0
nome_peso = []
pessoa = []
peso = []

while True:
    print('-='*12)
    nome_peso.append(input('Nome: ').strip().title())
    nome_peso.append((float(input('Peso: '))))
    tot_cad += 1
    fim = input('deseja continuar [S/N] ').strip().upper()
    while fim not in 'SN':
        print(cor['red'], 'Dados incorretos. ', cor['limp'], end='')
        fim = input('Deseja Continuar [S/N] ').strip().upper()
    if fim == 'N':
        print('-=' * 12)
        break

for c in range(0, len(nome_peso)):      #Aqui só percorre pela chave na lista "nome_peso" que foi criada
    if c % 2 == 1:
        peso.append(nome_peso[c])       #Aqui é criada uma lista auxiliar chamada peso para pegar apenas os índice pares
                                        #da lista "nome_peso", ou seja, efetivamente os valores referentes a peso e não nomes
menor = min(peso)
maior = max(peso)

print(f'\nA) Foram cadastradas {cor["amarelo"]}{tot_cad} pessoas{cor["limp"]}')

print(f'B) O(s) {cor["amarelo"]}mais pesado(s){cor["limp"]} tem {cor["amarelo"]}{maior} kg{cor["limp"]}: ', end='')
for pos, valor in enumerate(nome_peso):
    if valor == maior:
        print(cor['az'], f'{nome_peso[pos-1]}', cor['limp'], end=' | ')     #Como onde está o nome tem chave anterior ao peso,
                                                                            # tira-se 1 unidade da chave para pegar o nome na lista

print(f'\nC) O(s) {cor["amarelo"]}mais leve(s){cor["limp"]} tem {cor["amarelo"]}{menor} kg{cor["limp"]}: ', end='')
for pos, valor in enumerate(nome_peso):
    if valor == menor:
        print(cor['az'], f'{nome_peso[pos-1]}', cor['limp'], end=' | ')     #Como onde está o nome tem chave anterior ao peso,
                                                                            #tira-se 1 unidade da chave para pegar o nome na lista

from datetime import date
print(f'\n\nProcessado em {date.today()}')