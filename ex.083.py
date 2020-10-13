cor = {'red':'\033[1;31m', 'az':'\033[1;34m', 'limp':'\033[m'}

pa = pf = erro = 0
expressao = input('Diga a expressão matemática para avaliação: ').strip()

for valor in expressao:
    if valor == '(':
        pa += 1
    elif valor == ')':
        pf += 1
    if pf > pa:
        erro += 1

if pa != pf or erro > 0:
    print(cor['red'], '\nA expressão matemática está errada.', cor['limp'], 'Verifique os parênteses')
elif pa == pf and erro == 0:
    print(cor['az'], f'\nExpressão matemática está correta!', cor['limp'])

from datetime import date
print(f'\nProcessado em {date.today()}')


