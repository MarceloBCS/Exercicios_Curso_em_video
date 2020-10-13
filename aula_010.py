n = [1, 2, 3, 4, 5]
from random import random, uniform, randint, randrange, choice, shuffle, seed

#Na realidade são pseudo-aleatórios, uma vez que o computador não consegue gerar números verdadeiramente aleatórios
#utiliza um cálculo (por vezes complexo) cujo resultado parece aleatório. A função random.seed inicializa toda a maquinaria
#que depois é utilizada para calcular o próximo número. Como tal, todo este processo é completamente determinístico e
#dependente do valor com que inicializas o processo. Por esse motivo é que os valores são os mesmos se utilizar um valor
# inicial semelhante. Se utilizares a data actual em vez de 0 para a random.seed os valores serão diferentes de cada vez
# que invocares o teu programa, porque a seed será sempre diferente.
#Quando ainda não geraste nenhum valor pseudo-aleatório, precisa dar o valor inicial, sendo que em todas as chamadas
#subsequentes o valor será substituído pelo valor aleatório obtido na chamada anterior. Logicamente, com valores diferentes
#o valor aleatório inicial será diferente e, por esse motivo, também os subsequentes

seed()  # A método seed() define o valor de número inteiro de partida utilizado na geração de números aleatórios.
        # Deve-se chamar esta função antes de chamar qualquer outro módulo de função aleatória.
        # inicia a semente dos número pseudo randômicos

print(random())                             #random() retorna um float x tal que 0 <= x < 1.
print('uniform:  ', uniform(1.18, 200.89))  #uniform(10,20) retorna um float x tal que 10 <= x < 20 (não entra o 20)

print('randint:  ', randint(10, 99))     #randint(10,99) retorna um inteiro x tal que 10 <= x <= 99 (não entra o 99)
print('***randrange:', randrange(0, 16, 3)) #randrange(5, 11, 3) retorna um inteiro x tal que 5 <= x < 11 (não entra 11)
                                            # e x varia em step de 3 unidades

items = [1, 2, 3, 4, 5, 6, 7]
print('choice: ', choice(items)) # seleciona um dos elementos aleatoriamente

shuffle(items)
print('shuffle: ', items)        # embaralha os itens aleatoriamente


# Aula#10 - Condições parte 1