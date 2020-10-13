def metade(valor, formatar=False, currency='R$ '):
    valor = valor/2
    if formatar:
        return f'{currency}{valor:.2f}'.replace('.', ',')
    else:
        return valor


def dobro(valor, formatar=False, currency='R$ '):
    valor *= 2
#    if formatar:
#        return f'{currency}{valor}'.replace('.', ',')
#    else:
#        return valor
    #return valor if not formatar else f'{currency}{valor}'.replace('.', ',')        #comando opcional, ao invés das linhas acimas.
    #return valor if formatar is False else f'{currency}{valor}'.replace('.', ',')   #comando opcional, ao invés das linhas acimas.
    #return valor if formatar == False else f'{currency}{valor}'.replace('.', ',')   #comando opcional, ao invés das linhas acimas.
    #return valor if False else f'{currency}{valor}'.replace('.', ',')               #comando opcional, ao invés das linhas acimas.
    return valor if False else monetario(valor)                                     #comando opcional, ao invés das linhas acimas.


def aumentar(valor, fator=0, formatar=False, currency='R$ '):   #"formatar" Não precisou ser exposto no programa principal
    valor *= (1+fator/100)                                      #pq se pula parametro "currency" na declaração da função
    if formatar:
        return f'{currency}{valor:.2f}'.replace('.', ',')
    else:
        return valor
#    return valor if False else monetario(valor)                #comando opcional, ao invés das linhas acimas


def reduzir(valor, fator=0, formatar=False, currency='R$ '):    #"formatar" Não precisou ser exposto no programa principal
    valor *= (1-fator/100)                                      ##pq se pula parametro "currency" na declaração da função
    if formatar:
        return f'{currency}{valor:.2f}'.replace('.', ',')
    else:
        return valor


def monetario(valor, currency='R$ '):
    return f'{currency}{valor:.2f}'.replace('.', ',')


def resumo(valor, aum=0, red=0):
    e = 40
    print('-'*e)
    print('RESUMO DO VALOR'.center(e))
    print('-'*e)
    print('Preço Analisado', f'{monetario(valor):.>24}')
    print('Dobro do preço', f'{dobro(valor, True):.>25}')
    print('Metade do preço', f'{metade(valor, True):.>24}')
    print(f'{aum}%', 'de aumento', f'{aumentar(valor, aum, True):.>25}')
    print(f'{red}%', 'de redução', f'{reduzir(valor, red, True):.>25}')
    print('-'*e)


'''def resumo(valor, aum=0, red=0):
    e = 34
    print('-'*e)
    print('RESUMO DO VALOR'.center(e))
    print('-'*e)
    print(f'Preço Analisado \t\t{monetario(valor)}')
    print(f'Dobro do preço \t\t\t{dobro(valor, True)}')
    print(f'Metade do preço \t\t{metade(valor, True)}')
    print(f'{aum}% de aumento \t\t\t{aumentar(valor, aum, True)}')
    print(f'{red}% de redução \t\t\t{reduzir(valor, red, True)}')
    print('-'*e)'''