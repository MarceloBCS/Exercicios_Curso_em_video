def metade(valor):
    valor = valor/2
    return valor


def dobro(valor):
    valor *= 2
    return valor


def aumentar(valor, fator=0):
    valor *= (1+fator/100)
    return valor


def reduzir(valor, fator=0):
    valor *= (1-fator/100)
    return valor


def monetario(valor, currency='R$ '):
    return f'{currency}{valor:.2f}'.replace('.', ',')