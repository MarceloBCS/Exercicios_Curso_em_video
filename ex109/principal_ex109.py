from ex109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p:.2f} é {moeda.metade(p, True)}')  #moeda.monetario é uma função
                                                            #moeda.metade é OUTRA função
print(f'O dobro de R$ {p:.2f} é {moeda.dobro(p, True)}')

print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')

print(f'Reduzindo 13%, temos {moeda.reduzir(p, 13, formatar=True)}')    #Não precisa marcar o nome do parâmetro, mas se pular algum
                                                                        #parâmetro opcional, terá que colocar o nome no último. Neste
                                                                        #exemplo, "formatar" precisou ser exposto pq se pula parametro