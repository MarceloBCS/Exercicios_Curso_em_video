coisa = input('digite qualquer coisa: ')

cor = {'verm':'\033[1;31m', 'limp':'\033[m'}

print ('\nO tipo primitivo é: ', type(coisa))
print ('\nIsso seria Alfanumérico ???.......', coisa.isalnum())
print ('Isso seria uma letra ??? .........', coisa.isalpha())
print ('Isso seria um caracter Asc2 ???...', coisa.isascii())
print ('Isso seria um número ??? .........', coisa.isnumeric())
print ('Isso seria um nº decimal ???......', coisa.isdecimal())
print ('Isso seria um dígito ???..........', coisa.isdigit())
print ('Isso seria um identificador ("login"_only Alfanúmeros ou underscore_ e JAMAIS iniciando por nº ou com espaço)?', coisa.isidentifier())
print ('Isso seria caracter de letras minúsculas ??? .......................', coisa.islower())
print ('Isso seria um caracter de letras maiúsculas ???.....................', coisa.isupper())
print ('Isso seria uma palavra capitalizada (MAIÚCULO + minúsculo) ??? .....', coisa.istitle())
print ('Isso seria um caracter "printável" ??? .............................', coisa.isprintable())
print ('Isso seria um caracter de espaço ??? ...............................', coisa.isspace())

import datetime
print('\nPrograma executado {}{}{} !'.format(cor['verm'], datetime.date.today().today(), cor['limp']))







