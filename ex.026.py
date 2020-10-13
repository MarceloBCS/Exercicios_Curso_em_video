frase = input('Escreva uma frase: ').rstrip().lower()

letra = input('diga qual letra que vc quer checar: ').strip().lower()

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

n = frase.count(letra) #count não está aceitando lista (nem variável nem com str específica

print('\nA letra "{0}" aparece {1} vezes'.format(letra, n))

print('\nA letra "{0}" aparece pela 1º vez na posição: #{1}'.format(letra, frase.find(letra))) #FIND não funciona em lista

print('\nA letra "{0}" aparece pela última vez na posição #{1}'.format(letra, frase.rfind(letra))) #RFIND não funciona em lista

print('\n{1}comprimento da entrada: {0} elementos{2}'.format(len(frase), cor['red'], cor['limp']))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))











