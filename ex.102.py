cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'highlight':'\033[1;30;42m', 'enfase':'\033[7;35;40m'}


def fatorial(num, show=False):
    """
    → Calcula o fatorial de um número:
    :parametro num: o número que será calculado o Fatorial
    :parametro show: (opcional). Mostra, ou não, o cálculo do fatorial
    :param return: retorna o fatorial
    Elaborado por Marcelo Bhering
    """
    f = 1
    for m in range(num, 0, -1):
        f *= m
        if show:
            print(cor['amarelo'], m, cor['limp'], 'x ' if m > 1 else '= ', end='')
    print(cor['highlight'], end=' ')
    return f


num = int(input('Número: '))
print(fatorial(num, show=True), cor['limp'])

print()

print(cor['enfase'])
help(fatorial)
print(cor['limp'])

from datetime import date
print(f'Processado em {date.today()}')
