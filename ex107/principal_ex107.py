from ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, 13)}')
print()

#import moeda   #Funciona igual, mas não é recomendado pq posso ter mais de 1 pasta com o mesmo nome.
                #Está sublinhado vermelho, pq não houve referenciamento correto para ex107
import ex107.moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {ex107.moeda.metade(p)}')
print(f'O dobro de {p} é {ex107.moeda.dobro(p)}')
print(f'Aumentando 10%, temos {ex107.moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {ex107.moeda.reduzir(p, 13)}')

#from moeda import metade, dobro, aumentar, reduzir #Funciona igual, mas não é recomendado pq posso ter
                                                    #mais de 1 pasta com o mesmo nome. Sublinhou em vermelho pq não
                                                    #houve referenciamento correto para ex107
from ex107.moeda import metade, dobro, aumentar, reduzir
p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {reduzir(p, 13)}')
