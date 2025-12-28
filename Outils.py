import numpy as np
import PIL.Image as pl
from threading import Thread
from rich import progress as pb #Ce truc m'a bouffé du temps alors qu'il est inutilement con
from Constantes import *

#J'ai vraiment besoin de commenter?
def convert_and_resize(path=FRAME_PATH,repath=BINFRAME_PATH,size=(80,60)):
    with pb.Progress() as Bar:
        Id=Bar.add_task("Open and convert",total=FRAME_NUMBER)
        for i in range(FRAME_NUMBER):
            a=i+1    
            pl.open(f"{path}output_{a:0>4}.jpg").convert("1").resize(size).save(f"{repath}output_{a:0>4}.jpg")
            Bar.advance(Id)

def save(size=SIZE,name=f"{SIZE}".replace(' ',''),path=BINFRAME_PATH):
    global State
    State=0
    dataset=np.zeros((FRAME_NUMBER,size[0],size[1]),dtype=np.uint8)

    #Spamme les Thread si tu veux mais avec ma petite config je peux pas aller bien loin
    #Assure-toi juste que Thread_count en tienne compte
    first=Thread(target=Thread_append,args=(path,dataset,0,FRAME_NUMBER/2))
    second=Thread(target=Thread_append,args=(path,dataset,FRAME_NUMBER/2,FRAME_NUMBER))
    first.start()
    second.start()
    Thread_count=2

    while True:
        if State>=Thread_count:
            print("File registering")
            dataset=np.packbits(dataset) #C'est ici qu'on empaquette les données de l'array ça compresse énomément, ça divise pratiquement par 6 la taille du paquet et pour un coût en calcul plutôt faible
            np.save(f"{path+name}",dataset)
            print("\nSaved")
            break
        else:
            continue

def Thread_append(path,array,x=0,y=FRAME_NUMBER):
    global State
    with pb.Progress() as Bar:
        Id=Bar.add_task("Open and append",total=y-x)
        for i in range(x,y):
            a=i+1
            img=pl.open(f"{path}output_{a:0>4}.jpg").convert("1")
            array[i]=np.array(img,dtype=np.uint8)
            Bar.advance(Id)
        else:
            State+=1
            print("C'est fait")


convert_and_resize(size=SIZE)
save(size=SIZE[::-1])