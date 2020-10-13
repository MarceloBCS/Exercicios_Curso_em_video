n = int(input('diga o número: '))
from math import sqrt as raiz_2, floor as apbaixo, ceil as apcima
r1 = raiz_2(n)
r1_baixo = apbaixo(r1)
r1_cima = apcima(r1)
print('{0:<20.3f}'.format(r1), r1_baixo, '{:^10}'.format(''), r1_cima)

n2 = int(input('Qual é o nº´??? '))
import math
r2 = math.sqrt(n2)
print(math.floor(r2) , '{:^20.3f}'.format(r2) , math.ceil(r2))

import emoji
print(emoji.emojize('Oi, testei um emoji :house_with_garden:', use_aliases=False))












