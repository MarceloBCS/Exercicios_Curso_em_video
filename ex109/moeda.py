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


def reduzir(valor, fator=0, currency='R$ ', formatar=False):    #"formatar" precisou ser exposto no programa principal
    valor *= (1-fator/100)                                      ##pq se pula parametro "currency" na declaração da função
    if formatar:
        return f'{currency}{valor:.2f}'.replace('.', ',')
    else:
        return valor


def monetario(valor, currency='R$ '):
    return f'{currency}{valor:.2f}'.replace('.', ',')