#codigo principal
from moeda import dividir, dobrar, aumentar, diminuir
preço = float(input('Preço: '))
taxa = int(input('% : '))

print(f'O preço dividido por 2 {dividir(preço)}')
print(f'O dobro {dobrar(preço)}')
print(f'O aumento com taxa de {taxa} é {aumentar(preço)} ')
print(f'E a diminuição com a taxa de {taxa} é de {diminuir(preço, taxa)}')

#linha 8 - Faltou a inclusão da variável preço dentro da função aumentar()
#linha 8 - faltou a inclusão do 2º parâmetro para a função aumentar(), pq são necessários
            # 2 parâmetros (vc não colocou nenhum deles como opcional)
#linha 6 até linha 9 - Faltou colocar o caminho correto para o módulo, uma vez que usou o comando import moeda. A outra
            #opção seria usar o comando from moeda import dividir, dobrar, aumentar, diminuir

