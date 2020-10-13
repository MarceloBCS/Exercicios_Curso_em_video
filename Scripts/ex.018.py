a = float(input('diga o ângulo: '))
from math import sin , cos, tan, radians

r = radians(a)

seno = sin(r)
cosseno = cos(r)
tang = tan(r)

print('o ângulo {0}º é vale {1:.3f} radianos'.format(a, r))
print('___ o seno = {0:^10.3f} \n___ o cosseno = {1:^10.3f} \n___ a tangente = {2:^10.3f}'.format(seno, cosseno, tang))







