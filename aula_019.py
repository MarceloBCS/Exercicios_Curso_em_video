cor = {'branco':'\033[1;30m', 'amarelo':'\033[1;33m', 'roxo':'\033[1;35m', 'red':'\033[1;31m',
       'az':'\033[1;34m', 'az_claro':'\033[1;36m', 'verde':'\033[1;32m', 'limp':'\033[m'}

for pos, valor in cor.items():
    print(f'{pos} | {valor}', end='')
print('\n','-='*30)
cor['red'] = '\033[1;31m'
cor['az'] = '\033[1;34m'
print(cor)

del cor['red']
print('-='*30)
print(cor.values()) #foi como lista: []
print(cor.keys())   #foi como lista: []
print(cor.items())  #foi como tupla: ()
print(cor)          #foi como dicionário: {}
print('-='*30)

pessoas = {'nome':'marcelo', 'sexo':'masculino', 'idade':'46', 'peso':'82'}
pessoas['nome'] = 'leandro'
pessoas['nome'] = 'Bhering'
pessoas['signo'] = 'aquarinano'
print(pessoas['idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*30)

brasil = [[], []]
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil[0].append(estado1)
brasil[1].append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0][0]['uf'])
print('-='*30)

brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa ').strip().upper()
    estado['sigla'] = input('Sigla ').strip().upper()
    brasil.append(estado.copy())

print(f'elemntos da lista = {len(brasil)}', brasil)
for k in brasil:
    for key, val in k.items():
        print(f'{key} = {val}', end=' | ')
    print(k)
print('-='*30)
for k in brasil:
    print(f'k = {k}', end='')
    for key in k.keys():
        print(f' | {key}', end=' | ')
    print()


