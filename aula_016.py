lanche = ('hambuguer', 'suco', 'pizza', 'pudim', 'batata frita', 'sorvete', 'pipoca')
print(sorted(lanche))   #Apenas mostra ordenado, mas a tupla não muda de posição
print(lanche)           #Como a Tupla é imutável, a ordem permanece original
print('-'*50)
print('Tupla inversa de 1 em 1 = ', lanche[::-1])
print('Tupla inversa de 2 em 2 = ', lanche[::-2])
print('-'*50)
#A Tupla pode ser deletada:
# del(lanche)   #Neste caso, se colocar o comando Print, ele vai dar erro, pq a Tupla não existe mais.
                #Não é possível deletar apenas 1 item da tupla (ex: del(lanche[0]). Isso não pode ser feito
#maneira 1:
print('maneira #1)')
for comida in lanche:
    print(comida, end=' | ')
print('\n', lanche)
print('-'*50)
#maneira 2:
print('maneira #2)')
for comida in range(0, len(lanche)):
    print(f'Comerei {lanche[comida]}', end=' | ')
    print(comida)  #só informa a posição dentro da Tupla, pq é a variável do FOR
print('-'*50)
#maneira 3:
print('maneira #3)')
for posicao, comida in enumerate(lanche):
    print(f'{comida} na posição = {posicao}')
print('-'*50)

a = (2,5,4, 'Marcelo')      #Tupla aceita colocar tipos diferentes como números, strings, etc...
b = (5,8,1,2,1)
c = a + b
print('tupla c: ', c)    #A ordem das parcelas muda a tupla
print('"5" apareceu {} vez(es) e o número "4" {} vez(es)'.format(c.count(5), c.count(4)))
d = b + a

print('\ntupla d: ', d)    #A ordem das parcelas muda a tupla
if 1 in d:
    print('"d.index(1)" foi achado na posição #', d.index(1))    #index significa dizer: Em que posição está a 1º ocorrência do elemento "2" ?
    print('"d.index(1)" foi achado na posição #', d.index(1, 4)) #Depois da vírgula do index, significar que se quer a posição do elemento "2" a partir da posição4
else:
    print('não achei #9')


