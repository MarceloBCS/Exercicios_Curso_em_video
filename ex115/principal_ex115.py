from ex115 import painel, file_manager
#from ex115.file_manager import *                    #opção para importar tudo, mas tem que tirar o "path" nas funções
from time import sleep
from datetime import date

nome = ''
idade = 0

arq = 'Curso_em_Video.txt'
if not file_manager.arquivo_existe(arq):             #Se não existir o arquivo 'Curso_em_Video.txt , criar o arquivo.
    file_manager.criar_arquivo(arq)

while True:
    painel.cabeçalho('*****  MENU PRINCIPAL  *****')    #chama a função cabeçalho para início do painel
    painel.menu(['Ver pessoas cadastradas',             #chama a função que mostra as opções coloridas p/ o usuário
                 'Cadastrar novas pessoas',
                 'Sair do Sistema'])
    while True:
        #opcao = painel.escolha('Sua opção: ')              #chama a função para o usuário escolher

        opcao = painel.leia_int('Erro! Digite um número inteiro') #usando função só para ler número inteiro
                                                              #É necessário inutilizar try, except, else e deslocar o if

        '''try:
            opcao = int(opcao)                              #testa a opção do usuário. Se for inteiro, Ok
        except:
            painel.errado('Erro! Só é aceito números')     #Chama a função para erros de escolha no menu pelo usuário
            continue
        else:'''

        if 1 != opcao != 2 and opcao != 3:
            painel.errado('Erro! Opção inexistente.')  #Chama a função para erros de escolha no menu pelo usuário
            continue
        elif opcao == 1:
            file_manager.leia_arquivo(arq)                  #Chama a função para ver o cadastro gravado num txt
            break
        elif opcao == 2:
            file_manager.criar_cadastro(arq, nome, idade)           #Chama a função para gravar novo cadastro no txt
            break
        elif opcao == 3:
            painel.linha('*')                          #Chama a função que cria linha com o simbolo escolhido
            print('Saindo do programa...'.center(40))
            break
    if opcao == 3:
        sleep(.5)
        painel.cabeçalho('Obrigado. Até breve!')           #chama a função cabeçalho do diretorio painel p/ despedida
        break

print(f'\nProcessado em {date.today()}')

