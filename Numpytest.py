import numpy as np 
import PIL.Image as pl
import pygame
import sys
import time
from Constantes import *
pygame.init()

#On charge le dataset qu'on a mis en jeu et on le décompresse
#Ensuite on est obligé d'inverser l'axe des x et des y sinon l'image sera inversé, c'est une affaire de comptage
#Numpy compte de haut en bas comme c'est une matrice à deux dimensions et Pygame de gauche à droite comme cest une image
dataset=np.load(PACKED_ARRAY,mmap_mode='r')
dataset=np.unpackbits(dataset).reshape((FRAME_NUMBER,SIZE[1],SIZE[0]))
dataset=np.swapaxes(dataset,1,2)
print("Initialisation terminée")

#Les deux-trois éléments pour écrire un programme Pygame
espace=WINDOW
display=pygame.display.set_mode(espace)
Main_rectangle=display.get_rect()

#On réduit la profondeur et on mets une palette très légères pour aller plus vite
Fenetre=pygame.Surface(SIZE,depth=8)
palette=[(0,0,0),(255,255,255)]+[(0,0,0)]*254   
Fenetre.set_palette(palette)

print("Lancement de l'audio")
pygame.mixer_music.load("Audio.mp3")
pygame.mixer_music.play(loops=-1)

Frame_id=0
lastshot= time.time_ns()
print("Lancement de la vidéo")

while 1:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
            break

    current= time.time_ns()
    #C'est ma façon de ticker... Quoi il y a un moyen plus propre? Et alors, j'aime bien, c'est logique
    if current-lastshot>=NANOSECONDS_PER_FRAMES:
        display.fill("black")

        #On récupère les données d'une frame et on les affiche, c'est tout simple
        pygame.surfarray.blit_array(Fenetre,dataset[Frame_id])
        display.blit(pygame.transform.scale(Fenetre,espace),Main_rectangle)

        Frame_id+=1
        Frame_id=Frame_id%6520
        lastshot=current

        pygame.display.flip()
