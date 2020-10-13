import requests, os


def baixar_aquivos(url, endereco):
    #faz uma requisição ao servidor
    resposta = requests.get(url)  #para ler o conteúdo na forma de stream (fluxo), adicionamos um 2º parametro opcional:
                                  # resposta = request.get(url, stream=True)

    if resposta.status_code == requests.codes.ok:     #Parametro "ok" equivale ao código 200 que significa que deu certo
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)               #recebe o arquivo inteiro. Se ele for grande, use abaixo

#            for parte in resposta.iter_content(chunk_size=256):#Este código irá baixar o programa em etapas e salvar SSD
#                novo_arquivo.write(parte)                      #Esta parte copia o trecho "parte" (256 bytes) baixado
        print(f'Download finalizado. Arquivo salvo em: {endereco}')

    else:
        resposta.raise_for_status()         #método para tratar erros da própria biblioteca requests


if __name__ == '__main__':
    base_url = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    output_dir = 'output'

    for i in range(1, 26):
        nome_arquivo = os.path.join(output_dir, 'nota_de_aula_{}.pdf'.format(i))
        baixar_aquivos(base_url.format(i), 'test.pdf')