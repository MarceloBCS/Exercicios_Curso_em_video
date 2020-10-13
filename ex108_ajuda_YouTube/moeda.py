def diminuir (preço, taxa):
    r = preço - (preço * taxa/100)
    return r

def aumentar (preço, taxa=0):
    r = preço + (preço * taxa/100)
    return r

def dobrar (preço):
    r = preço * 2
    return r

def dividir (preço):
    r = preço / 2
    return r