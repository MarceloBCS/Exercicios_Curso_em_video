import datetime

cor = {'az':'\033[1;34m', 'limp':'\033[m', 'red':'\033[1;31m', 'amarelo':'\033[1;33m', 'ver':'\033[1;32;40m', 'contraste':'\033[1;31;40m'}

print('''\nEscolha o seu gênero:
[H] Se vc for Homem
[M] Se vc for Mulher''')

genero = input('\nQual é o seu gênero? ').strip()

if genero.lower() == 'h':
    birth = int(input('diga o ano do seu nacimento: '))
    hoje = datetime.date.today().year
    idade = hoje - birth

    if idade == 18:
        print(cor['amarelo'], '\nVc tem {} anos e por isso, deve se alistar este ano !!!'.format(idade), cor['limp'])
    elif idade > 18:
        print(cor['red'], '\nVc tem hoje {} anos. Está atrasado {} ano(s) para se alistar'.format(idade, idade-18), cor['limp'])
    elif idade < 18:
        print('\nVc tem hoje {2}{0} anos{3} e seu {2}alistamento será no ano {1}{3}'.format(idade, 18-idade+hoje, cor['az'], cor['limp']))

elif genero.lower() == 'm':
    print('\n{}Vc é mulher e por isso, não precisará cumprir o Alistamento Obrigatório{}'.format(cor['ver'], cor['limp']))
else:
    print('\n{}Vc escolheu opção errada de gênero{}'.format(cor['contraste'], cor['limp']))

print('\nProcessador em {}'.format(datetime.date.today().today()))









