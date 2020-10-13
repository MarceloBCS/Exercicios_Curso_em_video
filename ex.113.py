cor = ('\033[m',        # 0 - limpeza
       '\033[1;31m',    # 1 - vermelho
       '\033[1;33m',    # 2 - amarelo
       '\033[1;30;44m', # 3 - azul
       '\033[1;30;45m'  # 4 - roxo
        )


def leiaint(txt):              #fiz de uma forma (com input dentro na função)
    while True:
        valor = input(txt).strip().replace(',', '.')
        try:
            valor = int(valor)
        except Exception as zebra:
            print(cor[1], end='')
            print(f'ERRO: "{valor}" Não foi um inteiro válido.', cor[0],
                  f'Causa do erro <{zebra.__cause__}, Classe = <{zebra.__class__}>')
            print('-' * 40)
            continue
        else:
            return valor


def leiafloat(valor):                   #fiz de OUTRA forma (com input no programa principal)
    while True:
        try:
            valor = float(valor)
        except Exception as zebra:
            print(cor[1], end='')
            print(f'ERRO: "{valor}" não é um real válido.', cor[0],
                  f'Causa do erro <{zebra.__cause__}, Classe = <{zebra.__class__}>')
            print('-' * 40)
        else:
            return valor
        valor = input(' Digite um real novamente: ').strip().replace(',', '.')


print(cor[2], '='*40, cor[0])
n_int = leiaint(' Digite um inteiro: ')                         #fiz de uma forma (com input dentro na função)
print(cor[2], '='*40, cor[0])

n2 = input(' Digite um real: ').strip().replace(',', '.')       #fiz de OUTRA forma  (com input no programa principal)
n_real = leiafloat(n2)
x = str(n_real).replace('.', ',')

print(cor[2], '='*40, cor[0])
print(f' O valor {cor[3]}inteiro = {n_int}{cor[0]} e o valor {cor[4]}real = {x}{cor[0]}')

from datetime import date
print(f'\nProcessado em {date.today()}')