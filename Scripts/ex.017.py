c_oposto = float(input('cateto oposto: '))
c_adjacente = float(input('cateto adjacente: '))

from math import hypot
hipotenusa = hypot(c_oposto, c_adjacente)

print('usando o cateto oposto {0:.3f} e o cateto adjacente {1:.3f}, vc terá como Hipotenusa {2:<10.3f}'.format(c_oposto, c_adjacente, hipotenusa))
