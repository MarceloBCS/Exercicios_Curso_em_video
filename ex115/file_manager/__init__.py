from ex115 import painel


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')            #Código 'rt' = read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'w+')           #wt significa write text. O "+" significa que se não existir, é para criar.
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo |{nome}| criado com sucesso')


def leia_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO para ler o arquivo')
    else:
        painel.cabeçalho('Pessoas Cadastradas')
        for linha in a:                                 #Cada linha no laço For é uma lista
            dado = linha.split(';')                     #Cada elemento da lista será separado por ";"
            #dado[1] = dado[1].replace('\n', '')        #Substituir o elemento '\n' que pula linha por "nada"
            dado[1] = dado[1].rstrip()                  #comando rstrip() p/ eliminar os espaços à direita (até o final)
            print(f'{dado[0]:.<30}{dado[1]:.>5} anos')

        #print(a.read())    #Mostra cada linha do arquivo. Se colocar nº inteiro "X" no parênteses, ele ler X caracteres
    a.close()


def criar_cadastro(file, nome='', idade=0):
    painel.cabeçalho('Cadastro de novas Pessoas')
    while True:
        nome = input('Nome: ').strip().title()
        if nome == '':
            painel.errado('ERROR! O nome não pode ser desconhecido.')
            continue
        else:
            while True:
                idade = input('Idade: ').strip()
                try:
                    idade = int(idade)
                except:
                    painel.errado('ERROR. A idade deve ser um número inteiro.')
                    continue
                else:
                    a = open(file, 'at')
                    try:
                        a.write(f'{nome};{idade}\n')
                    except:
                        painel.errado('Houve um ERRO ao tentar registrar esta')
                    else:
                        print(f'Registro de {nome} foi gravado com sucesso')
                    a.close()
                    break
        break
