a = (8, 6, 7, 1)
b = [9, 4, 5, 8, -3, 15]
c = ['Z', 'T', 'P', 'Y', 'A', 'D', 'E']
print(a)
print(sorted(a))
print('-='*10)

print(b, c)
b.sort()
c.sort()
print('\nsort()       ', b, ' →→→→→→→→→ ', c,)
b.sort(reverse=False)
c.sort(reverse=False)
print('reverse=False ', b, '→→→→→→→→→ ', c)
b.sort(reverse=True)
c.sort(reverse=True)
print('reverse=True ', b, ' →→→→→→→→→ ', c)
print('-='*10)

num = [2, 5, 9, 1]
print(num)
print(num[1])   #Mostra o elemento da posição #1
num.append(4)   #inclui o elemento "4" na última posição
print(num)
num.sort()              #ordena na ordem normal
print('Testando o num.sort() = ', num)
num.sort(reverse=True)  #ordena de forma inversa
print('usando num.sort(reverse=True) = ', num)

num.insert(3,15)     #insere na posição #3 o elemento "0"
print('\nusando o insert(3,15) = ', num)
del num[2:5]
print('\nusando o del num[2:5] = ', num)
num.pop()   #elimina o último elemento da lista
print('usando pop() ', num)
num.pop(1)  #elimina o elemento da posição #1
print('usando o num.pop(1) = ', num)

if 7 in num:
    num.remove(7) #remove(7) remove o elemento "7" sem dar erro pela ausência. Já pop(7), remove o elemento da posição #7
else:
    num.append(14)
    print('\nnão achei o número "7" na sua lista')
    print('usando num.append(14), insere-se no final o valor 14 = ', num)

valor1 = []
valor2 = list()
valor3 = list(range(50,4,-3))
print('\nvalor3 = ', valor3)

valor1.append(2)
valor1.append(4)
valor1.append(2)
valor1.append(4)

valor2.append(0)
valor2.append(6)
valor2.append(1)
print('\nvalor1 = {} e a valor2 = {}'.format(valor1, valor2))

print(valor1[-1])
for c_chaves in valor1:        #c_haves refere-se ao valor de cada elemento e não da sua posição
    print(f'{c_chaves:.^5}', ' → ' if c_chaves != valor1[-1] else '  ', end='')

print('\n', '-='*20)
for posicao, v in enumerate(valor2):
    print(f' Na {posicao+1}º posição - eu encontrei o valor {v}')

lista_a = [2, 3, 4, 5, 6, 7,]
lista_b = lista_a       #isso significa que a lista_b ficou ligada a lista_a. QQ modificação em uma, altera a outra
lista_c = lista_a[:]    #isso significa que a lista_c recebeu uma cópia (sem vinculação) dos valores da lista_a
lista_b[2] = 8
lista_a[1] = 10
print('lista_a = ', lista_a)
print('lista_b = ', lista_b)
print('lista_C = ', lista_c)
