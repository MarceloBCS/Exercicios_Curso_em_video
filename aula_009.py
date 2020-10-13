'''frase = 'Eu tenho que aprender esta linguagem de forma urgente!!!!'

print(frase[-2], frase[-7], frase[-8], frase[-9], frase[-10])
print(len(frase))

import math
print(math.pi, " "*5, int(math.pi))

preco = 'R$ 20,56'
n = float(preco.strip('R$ ').replace(',', '.'))
print(float(preco.strip('R$ ').replace(',', '.')))
print(type(preco), type(n))
print(preco, " "*5, len(preco))'''

frase1 = 'Tenho que terminar o curso de Python, até sábado'
frase2 = 'o curso Sigmoidal custa 12x R$ 58,16 (por mês)'

print(len(frase1), len(frase2), frase2.find('R$'), frase2.find('('), frase1.count('o'))
print('-='*10)

n1 = frase2.split(' ')
print(n1[6].replace(',', '.'))

n2 = frase2[28:37] [3:8]
print(n2)
print(float(n2.replace(',', '.'))*12)

print(n1)
print('_'.join(n1))

print('\nfrase 1 --->', frase1.lower().count('e',5,-1))
print('\nfrase 1 =======>', frase1[::2])










