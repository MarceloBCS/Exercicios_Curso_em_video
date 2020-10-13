nome = input('Diga o nome completo: ').strip().lower()

cor = {'verm':'\033[1;31m', 'az':'\033[m', 'limp':'\033[m'}

n = nome.split(' ')

print(nome, cor['verm'], '*'*5, cor['limp'], n)

print('\nTem Silva em alguma parte do nome? ', 'silva' in nome) #Ex: Silvana vai dar erroneamente True

print('\nTem silva no 1º nome: ', 'silva' in n[0]) #Ex: Silvana vai dar erroneamente True na 1º posição

print('\nTem silva em alguma parte do nome: ', 'silva' in n) #Ex: Silvana vai dar False

print('\nA 1º posição do nome "Silva" é : ', nome.find('silva'))

#print('\nA 1º posição do nome "Silva" é :', n.find('silva')) #Comando FIND não pode ser usado em lista

print('\nQuantas vezes aparece Silva: ', n.count('silva')) #Count pode ser usado em lista ou string completa e não pega erro "SILVANA"

import datetime
print('\nProcessador em {}'.format(datetime.date.today().today()))





