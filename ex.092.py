from datetime import date

cad = {}
cad['nome'] = input('Nome: ').strip().title()

nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
cad['idade'] = idade

cad['CTPS'] = input('CTPS ou [0] se não tiver: ').strip().upper()
if cad['CTPS'] != '0':
    ano_contr = int(input('Ano da Contratação: '))
    cad['ano_contratacao'] = ano_contr
    cad['salario'] = float(input('Salário = R$ '))
    aposent = 35 - (date.today().year - ano_contr)
    ano = 35 + ano_contr
    cad['aposentadoria'] = aposent

print('-='*60)
print('teste_lista = ', cad)

print('-='*60)

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

print(cor['amarelo'])
print(f'Nome = {cad["nome"]}')
print(f'Idade = {cad["idade"]}')
print(f'CTPS = {cad["CTPS"]}')
if cad['CTPS'] != '0':
    print(f'Contratação = {cad["ano_contratacao"]}')
    print(f'Salário = R$ {cad["salario"]:.2f}')
    print(f'Aposentadoria será em {cad["aposentadoria"]} anos ({ano})')

print(f'\nProcessado em {date.today()}')