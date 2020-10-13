n1 = float(input('\nnota da P1 (máx é 10): '))
n2 = float(input('nota da P2 (máx é 10): '))
s = n1 + n2
media = (n1+n2)/2

cor = {'amarelo':'\033[7;33m', 'verde':'\033[7;32m', 'limp':'\033[m', 'verm':'\033[7;31m', 'azul':'\033[1;34m'}

print ('\nA soma das notas {0:.3f} e {1:.3f} será {2:^5.2f} \n e a media das notas será {4}{3:.2f}{5}'
       .format(n1, n2, s, media, cor['azul'], cor['limp']))

#avaliação
if media == 7:
    print('\nescapou RASPANDO da Prova Final')
elif media < 5:
    print ('\n', cor['verm'], 'reprovado, Young Grasshopper !!!', cor['limp'])
elif media > 5 and media < 7:
    print('\n',cor['amarelo'], 'vc vai fazer prova final', cor['limp'])
else: print('\n{0}Parabéns!!!!{1}\n{0}Passou direto com nota {2:-^20}{1}'.format(cor['verde'], cor['limp'], media))

import datetime
print('\nProcessado em {}'.format(datetime.date.today().today()))









