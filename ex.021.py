import playsound, datetime

cor = {'red':'\033[1;31m', 'limp':'\033[m'}

print('\n{1}Este som foi Processado em {0}{2}'.format(datetime.date.today().today(), cor['red'], cor['limp']))

playsound.playsound('ex.021_storm.mp3')



#import pygame
#variações abaixo não davam erro na maioria das vezes, mas não tocava música nenhuma!
#pygame.init()
#pygame.mixer.music.load('ex021_storm.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()

#variação do código acima (trocando a linha 11 pela linha 14)
#while(pygame.mixer.music.get_busy()):pass




