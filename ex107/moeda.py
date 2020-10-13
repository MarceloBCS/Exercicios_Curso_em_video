def metade(valor):
    valor = valor/2
    return valor


def dobro(valor):
    valor *= 2
    return valor


def aumentar(valor, fator=1):
    valor *= (1+fator/100)
    return valor


def reduzir(valor, fator=1):
    valor *= (1-fator/100)
    return valor
