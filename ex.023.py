n = str(input('diga 1 número entre 0 até 9999 : '))
soma = '000'+n

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

print(cor['amarelo'], soma, cor['limp'])
print('\nunidade é:', soma[-1])
print('dezena  é ', soma[-2])
print('centena é ', soma[-3])
print('milhar  é ', soma[-4])

l = int(len(n))

if l == 1:
    d0 = n[0]
    print('\n====> unidade : ', d0)
elif l == 2:
    d0 = n[0]
    d1 = n[1]
    print('====> unidade : {} \n====> dezena  : {}'.format(d0, d1))
elif l == 3:
    d0 = n[0]
    d1 = n[1]
    d2 = n[2]
    print('====> unidade : ', d0, '\n====> dezena :  ', d1, '\n====> centena : ', d2)
elif l == 4:
    d0 = n[0]
    d1 = n[1]
    d2 = n[2]
    d3 = n[3]
    print('====> unidade : ', d0, '\n====> dezena  : ', d1, '\n====> centena : ', d2, '\n====> milhar  : ', d3)
else: print('*'*10, 'Presta Atenção: era número com ATÉ 4 dígitos !!!')

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))



