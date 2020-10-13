cor = {'amarelo':'\033[1;33m', 'limp':'\033[m', 'roxo':'\033[7;35;40m'}


def notas(*num, sit=0):
    """
    → Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos (Aceita várias notas) serão guardadas como uma Tupla (num), armazenados num
                dicionário "resp"
    :param sit: valor opcional. Indica se deve ou não adicionar a situação da média dos alunos
    :return: dicionário com várias informações sobre a situação da turma (total de notas, maior, menor, média, situação)
    """
    media = sum(num) / len(num)
    resp = dict()
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['media'] = media

    if sit:
        if media >= 7:
            resp['situação'] = 'Boa → Aprovado'
        elif media < 5:
            resp['situação'] = 'Ruim → Reprovado'
        else:
            resp['situação'] = 'razoável → Recuperação'

    return resp


print('-='*10)
resp = notas(9.5, 1, 6.5, 1, 7, 4, sit=True)
print(cor['amarelo'], resp)

print()
print(cor['roxo'], end='')
help(notas)
print(cor['limp'])

from datetime import date
print(f'Processado em {date.today()}')
