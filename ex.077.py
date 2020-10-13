cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'az':'\033[1;34m'}

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in range(0,len(tupla)):
    print('\n', '{0:>2}º) vogais da palavra {2}{1:.<20}{3} = '
          .format(palavra+1, tupla[palavra].upper(), cor['az'], cor['limp']), end=' ')

    for letra in range(0, len(tupla[palavra])):
        if tupla[palavra][letra] in 'aeiou':
            print(cor['amarelo'], tupla[palavra][letra], cor['limp'], '→ ' if letra < (len(tupla[palavra])-2) else '', end='')

from datetime import date
print(f'\n\nProcessado em {date.today()}')



