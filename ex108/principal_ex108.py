from ex108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.monetario(p)} é {moeda.monetario(moeda.metade(p))}')  #moeda.monetario é uma função
                                                                                 #moeda.metade é OUTRA função
print(f'O dobro de {moeda.monetario(p)} é {moeda.monetario(moeda.dobro(p))}')

print(f'Aumentando 10%, temos {moeda.monetario(moeda.aumentar(p, 10))}')

print(f'Reduzindo 13%, temos {moeda.monetario(moeda.reduzir(p, 13))}')