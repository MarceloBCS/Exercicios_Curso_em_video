import datetime

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

#maximo = 0
#minimo = 1000  #gambiarra de programação. Deve ser evitada. Melhor criar um laço com "IF" em c=1

for c in range(1,6):
    peso = float(input('{}º - Diga o seu peso: '.format(c)))
    if c == 1:
        maximo = peso
        minimo = peso
    else:
        if peso > maximo:
            maximo = peso
        if peso < minimo:
            minimo = peso

print('-='*10)
print(cor['amarelo'], 'peso máximo = ', maximo, cor['limp'])
print(cor['amarelo'], 'peso mínimo = ', minimo, cor['limp'])

print('\nProcessado em {}'.format(datetime.date.today()))
