n = int(input('digite o número: '))

cor = {'verm':'\033[1;31m', 'limp':'\033[m'}

#tabuada será
t0 = n*0
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9

print(cor['verm'], '=-' * 5, cor['limp'])
print(' {0} x 0 = {1}\n {0} x 1 = {2}\n {0} x 2 = {3}\n {0} x 3 = {4}\n {0} x 4 = {5}'.format(n, t0, t1, t2, t3, t4))
print(' {0} x 5 = {1}\n {0} x 6 = {2}\n {0} x 7 = {3}\n {0} x 8 = {4}\n {0} x 9 = {5}'.format(n, t5, t6, t7, t8, t9))
print(cor['verm'], '=-' * 5, cor['limp'])

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))




