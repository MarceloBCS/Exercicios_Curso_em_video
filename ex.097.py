cor = {'red':'\033[1;31m', 'az':'\033[1;34m', 'limp':'\033[m'}

def escreva(msg):
    c = len(msg)
    print(cor['az'], '~'*(c+2), cor['limp'])
    print(cor['red'], '', msg, cor['limp'])
    print(cor['az'], '~'*(c+2), cor['limp'])


escreva('olá, Mundo!')
print()
escreva('Python is too hard to execute!!!')
print()
escreva('Cev')

from datetime import date
print(f'\nProcessado em {date.today()}')