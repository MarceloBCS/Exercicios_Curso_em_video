from datetime import date

cor = {'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'az':'\033[1;34m', 'limp':'\033[m'}


def voto(nasc):
    idade = date.today().year - nasc
    if idade >= 70 or 16 <= idade < 18:
        return f'Com {idade} anos: {cor["amarelo"]}Voto opcional{cor["limp"]}'
    elif idade < 16:
        return f'Com {idade} anos: {cor["red"]}Vc ainda não tem idade para votar{cor["limp"]}'
    else:
        return f'Com {idade} anos: {cor["az"]}Voto obrigatório{cor["limp"]}'


nasc = int(input('Ano do seu nascimento: '))
print(voto(nasc))

print(f'\nProcessado em {date.today()}')