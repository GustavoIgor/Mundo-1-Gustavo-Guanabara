#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init() #Agora esta linha é necessária
pygame.init()
pygame.mixer.music.load('Aerosmith Dream On.mp3')
pygame.mixer_music.play()
pygame.event.wait()

# Esta musica foi utilizada apenas para fins educacionais e pode ser acessada livremente no youtube
# https://www.youtube.com/watch?v=89dGC8de0CA