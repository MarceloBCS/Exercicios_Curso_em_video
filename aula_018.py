teste = list()
galera = list()
clone = list()
teste.append('Gustavo')
teste.append('40')

galera.append(teste[:])
clone.append(teste)
print('teste original = ', teste)
print('galera = ', galera)
print('clone = ', clone)
print('-'*20)

teste[0] = 'Maria'
teste[1] = '22'
print('teste modif1 = ', teste)
print('galera original = ', galera)
print('clone.append(teste)', clone)
print('='*40)
galera.append(teste[:])
clone.append(teste)
print('teste modif1 = ', teste)
print('galera.append(teste[:]) = ', galera)
print('modif2 = clone.append(teste)', clone)

galerao = []
dado = []

for c in range (0,4):
    dado.append(input('\nDiga o seu nome: '))
    dado.append(int(input('Diga a sua idade: ')))
    galerao.append(dado[:])
    dado.clear()

print(f'\nOs maiores de idade são: ', end='')
for p in galerao:
    if p[1] >= 18:
        print(f'{p[0]} → {p[1]} anos', end=' | ')

print(f'\nOs menores de idade são: ', end='')
for p in galerao:
    if p[1] < 18:
        print(f'{p[0]} → {p[1]} anos', end=' | ')

print('\ndado = ', dado)
print('galerao = ', galerao)

