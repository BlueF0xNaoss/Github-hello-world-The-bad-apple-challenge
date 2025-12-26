#Version 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1 du projet, circulez, y a rien à voir
import pygame
import os
import time
import sys
pygame.init()

def main():
    espace=width,height=1200,600
    Fenetre=pygame.display.set_mode(espace)

    #a=[(f"Bad_apple/frames/output_{str(i+1):0>4}.jpg") for i in range(6572)]
    #images=[pygame.image.load(i) for i in a]
    Rectangle=pygame.Rect(0,0,1200,600)
    print("done")
    k=0
    lastshot= time.time_ns()
    while 1:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        #Fenetre.fill("black")
        current= time.time_ns()
        if current-lastshot>=50000000:
            Fenetre.blit(pygame.image.load(f"frames/output_{str(k+1):0>4}.jpg"),Rectangle)    
            k+=1
            k=k%6572
            lastshot=current
        pygame.display.flip()
        #time.sleep(0.1)
main()

