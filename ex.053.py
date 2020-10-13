import datetime

cor = {'amarelo':'\033[1;33m', 'red':'\033[1;31m', 'limp':'\033[m'}

frase = input('Diga a frase: ').strip().lower().split(' ')

nova_frase = ''.join(frase)
print('comprimento da string = ', len(nova_frase))

limite = len(nova_frase)
teste = 0

# Ao invés de usar o laço abaixo, poderia-se ter invertido a String com o comando:
'''inverso = nova_frase[::-1]
if nova_frase == inverso:
    print('É um palindromo')
else:
    print('não é um palindromo')'''

for c in range(0, limite):
    if nova_frase[c] == nova_frase[limite-1-c]:
        teste = teste + 1
        #print(teste)

if teste == limite:
    print(cor['amarelo'], '\nÉ palindromo', cor['limp'])
else:
    print(cor['red'], '\nNÃO É palindromo', cor['limp'])

print('\nProcessado em {}'.format(datetime.date.today()))
