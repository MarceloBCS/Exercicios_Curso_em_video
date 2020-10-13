nome = input('diga o nome da cidade que vc nasceu: ').lower().strip().replace('-', ' ').split()

cor = {'amarelo':'\033[1;33m', 'limp':'\033[m'}

frase = ' '.join(nome)

print(cor['amarelo'], nome, cor['limp'])
print(nome[-1]) #treinando o uso de letra de uma palavra na lista
print(nome[2][1:]) #treinando o uso de letra de uma palavra na lista

print('\nO nome da cidade começa por Santo? ', nome[0] == 'santo') #EX: Santorini ou Santos vão dar False pq é split

print('\n Comando in ----> cidade tem a palavra Santo em algum lugar? ', 'santo' in nome) #(Ex: Santorni, Santos) vai dar False se Split e s/ samto

print('\n Comando in ----> cidade começa por Santo? ', 'santo' in nome[0])  #(Ex: Santorini, Santos) na posição #0 vai dar erroneamente True

#Comando FIND e RFIND não podem ser usados em lista
print('\n Comando find --> tem a palavra Santo no nome? ', '\n', frase,
      '-'*5+'> posição str', frase.find('santo')) #santos ou santorini seria dado como TRUE


import datetime
print('\n{1}Processado em {0}{2}'.format(datetime.date.today().today(), cor['amarelo'], cor['limp']))






