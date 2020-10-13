'''#Acessando a web com a API Request
import requests

#A função requests.get() obtém um recurso qualquer através de uma URL passada como argumento. Neste caso, não foi requerida
#autenticação para fazer a requisição. A chamada a essa função retorna um objeto do tipo Response, que dentre outras coisas
# contém o status da requisição, que é um código numérico indicando o que aconteceu com a requisição
response = requests.get('http://www.pudim.com.br/')

# Código 200 significa "requisição OK!"
print(response.status_code == 200)
print(response)

#O conteúdo da resposta enviada pelo servidor é armazenado no atributo content da resposta e pode ser acessado como qualquer
# outro atributo (response.content no código abaixo)
c = len(response.content)
print(c)'''

cor = ('\033[1;30;41m',     # 0 Red
       '\033[1;30;43m',     # 1 Yellow
       '\033[1;30;46m',     # 2 Green
       '\033[m'             # 3 limpeza
       )

#Biblioteca 2
import requests, webbrowser
try:
    site = requests.get('http://www.pudim.com.br/')
#except Exception as zebra:
#    print(cor[0], 'biblioteca request ---> O site Pudim não está acessível no momento', cor[3])
except:
    print(cor[0], 'biblioteca request ---> O site Pudim não está acessível no momento', cor[3])
else:
    print(cor[1], 'biblioteca request ---> consegui acessar o site Pudim com sucesso', cor[3])
    webbrowser.open('http://www.pudim.com.br/')

#Biblioteca 2
import urllib, webbrowser
try:
   site = urllib.request.urlopen('http://www.pudim.com.br/')
#except Exception as zebra:
#    print('\n', cor[0], 'urllib → O site Pudim não está acessível no momento', cor[3])
except:
    print('\n', cor[0], 'urllib → O site Pudim não está acessível no momento', cor[3])
else:
    print('\n', cor[2], 'urllib → consegui acessar o site Pudim com sucesso', cor[3])
    print(site.read)
    print('\nabrindo o site...')
    webbrowser.open('http://www.pudim.com.br/')