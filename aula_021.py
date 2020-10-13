help(input)  #auxílio na documentação

print(input.__doc__) #auxílio na documentação


def contador(i, f, p):      #Os 2 conjuntos de aspas 3x são chamadas de DocStrings para o "help(função)"
    """
    →Faz uma contagem e mostra na tela.
    :sobre o parâmetro i: início da contagem
    :sobre o parâmetro f: fim da contagem
    :sobre o parâmetro p: passo da contagem
    :return: sem retorno
    Função criada pelo Gustavo Guanabara do Canal Curso_em_Vídeo
    """
    c = i
    while c <= f:
        print(f'{c}', end=' | ')
        c += p
    print('FIM!')


contador(1, 100, 7)
help(contador)


def somar(a=0, b=0, c=5, d=0):  #Isso é chamado de parâmetro opcional. Assim, eu posso ter menos parâmetros na função
    s = a + b + c + d
    print(f'A soma = {s}')
    return s


s1 = somar(2, 4)
s2 = somar(d=8, b= 1)
s3 = somar(6)
print(f'Personalizando os resultados, as somas são {s1}, {s2}, {s3}')

def teste(b):
    #global a    #Comando global tranforma a variável local "a" em variável global, substituindo o valor global anterior
    a = 8
    b += 4
    c = 2
    print(f'\nO "a" local vale {a}')
    print(f'O "b" local vale {b}')
    print(f'O "c" local vale {c}')


a = 5
teste(a)
print('='*10)
print(f'O "a" global vale {a}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print()
print(fatorial(5))
print(fatorial())

n = int(input('Digite um número: '))
fn = fatorial(n)

print(f'Fatorial de {n}! = {fn}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Diga o número para saber se é par: '))
print(f'{par(n)}')
if par(n):
    print('É par')
else:
    print('É ímpar')