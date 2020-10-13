try:    #tente...
    num = float(input('digite o numerador: '))
    den = float(input('digite o denominador: '))
    r = num / den
#except:  #"Genérico". Se der errado, faça...
#   print(f'Infelizmente, houve um erro {ZeroDivisionError}. Vc não pode dividir por Zero')

except KeyboardInterrupt:
    print(f'  1) O usuário interrompeu o programa')
except (ValueError, TypeError):
    print(f'  2) Erro de valor = <{ValueError}>   ou   Erro de tipo <{TypeError}>')
except ZeroDivisionError:
    print(f'  3) Tentativa de dividir por Zero... Tente novamente.')
except Exception as erro:       #"Genérico". Se der errado os de cima, faça abaixo criando a "variável erro"...
    print(f' 4) O erro encontrado foi <{erro}>')
    print(f' 4) O problema encontrado teve causa = <{erro.__cause__}> e classe = <{erro.__class__}>')

else:   #Se der certo, faça...
    print(f'Deu certo! A razão = {r:.2}')
finally: #acontecerá dando certo ou dando errado...
    print('\nVolte sempre !')
    print('-'*20)



'''import shelve
shelve.open()'''
#import request