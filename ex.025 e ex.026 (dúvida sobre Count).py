frase = input('Diga o nome completo: ').strip().lower()

n = frase.split(' ')

print('\nQuantas vezes aparece Silva: ', n.count('silva')) #Count pode ser usado em lista ou string completa e não pega erro "SILVANA"

print('\n','#'*20)

letra = input('\ndiga qual letra que vc quer checar: ').strip()

n2 = n.count(letra) #count não está aceitando lista (nem variável nem com str específica
print(n2)
print('\nA letra "{0}" aparece {1} vezes'.format(letra, n2))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))
