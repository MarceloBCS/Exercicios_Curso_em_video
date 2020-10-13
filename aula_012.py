n = input('\nQual é o seu nome? ').strip()

if  'MARCELO' in n.upper():
    print('\nShow de bola, {}'.format(n.capitalize()))
elif n.lower() in 'ana maria luciana isabella isabela isabele mônica':
    print('\nseu nome é feminino e lindo, {} '.format(n.title()))
elif 'vitor hugo' in n.lower():
    print('\neu não gosto de ignorância não, viu {} ?'.format(n.title()[:10]))
elif n.lower() == 'reneide':
    print('\nseu nome é incomum, mas eu gosto, {} '.format(n.capitalize()))
else:
    print('nada a acrescentar...')

print('\nHave nice day !!!')

