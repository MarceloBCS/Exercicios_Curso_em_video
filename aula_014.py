#Estrutura de repetição com teste lógico (while)
import datetime
c = 1
par = impar = 0
tot_par = 0
tot_impar = 0

while c != 0:
    n = int(input('diga um número: '))
    if n % 2 == 0:
        tot_par += + 1
        print('Este nº {} é par. Total de par é {}: '.format(n, tot_par))
    else:
        tot_impar += 1
        print('Este nº {} é impar. Total de ímpar é {}'.format(n, tot_impar))
    if n == 0:
        c = 0

print('\nProcessado em {}'.format(datetime.date.today().today()))
