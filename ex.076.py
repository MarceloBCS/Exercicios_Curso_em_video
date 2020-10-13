print('-'*44)
print(' '*12, 'listagem de preço')
print('-'*44)

cad = ('lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'transferidor', '4.20',
            'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')

for c in range(0,len(cad),2):
    #print('{0:.<12}......................R$ {1:>6}'.format(cad[c], cad[c+1]))
    print(f'{cad[c]:.<12}......................R$ {cad[c+1]:>6}')               #print alternativo tbm funciona !!!!!

print('-'*44)

