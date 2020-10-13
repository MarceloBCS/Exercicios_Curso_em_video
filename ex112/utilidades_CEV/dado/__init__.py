cor = {'red':'\033[1;31m', 'lim':'\033[m'}


def leiadinheiro(valor=0):
    valor = valor.strip().replace(',', '.').split()
    valor = ''.join(valor)
    while valor.isalpha() == True or valor == '':
        print(cor['red'], f'ERROR !!! "{valor}" é um preço inválido', cor['lim'])
        print('-' * 10)
        valor = input('Digite novamente o preço: R$ ').strip().replace(',', '.').split()
        valor = ''.join(valor)

    valor = float(valor)
    print(valor, f'type= {type(valor)}')
    return valor

