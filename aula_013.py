#Estrutura de repetição com variável de controle (for)

i = int(input('início: '))
f = int(input('fim: '))
p = int(input('passo: '))
print('-='*10)
s = 0
for c in range(i,f+1):
    print('contando para frente: ', c)
    s = s + c
print(s)
print('-='*10)
for c in range(f,i-1, -1):
    print('contando ao contrário: ', c)
    s = s + c
print(s)
print('-='*10)
for c in range(i,f+1,p):
    print('contando com passo 2: ',c)
    s = s + c
print(s)
print('-='*10)
for c in range(f,i-1, -p):
    print('Contando ao contrário de 2 em 2: ', c)
    s = s + c
print(s)