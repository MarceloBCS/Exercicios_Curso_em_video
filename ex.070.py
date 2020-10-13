cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'red':'\033[1;31m'}

tot_gasto = mais_1000 = menor_preco = count = 0

while True:
    nome = input(('Qual é o produto: ')).strip().title()
    preco = float(input('Qual é o preço: R$ '))
    fim = input('Continuar? [S/N] ').strip().upper()[0]
    while fim != 'S' and fim != 'N':
        fim = input('Dados inválidos. Continuar? [S/N] ').strip().upper()[0]
    print('-=' * 10)
    count += 1
    tot_gasto += preco

    if preco > 1000:
        mais_1000 += 1

    if count == 1 or preco < menor_preco:
        nome_mais_barato = nome
        menor_preco = preco

    if fim == 'N':
        break

print('\n{} ***** Check out dos Produtos *****{}'.format(cor['red'], cor['limp']))
print(cor['amarelo'], f'Total gasto na compra = R$ {tot_gasto:.2f}')
print(f' Nº de produtos > R$1.000 = {mais_1000}')
print(f' Produto mais barato é: {nome_mais_barato} = R$ {menor_preco:.2f}', cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')
