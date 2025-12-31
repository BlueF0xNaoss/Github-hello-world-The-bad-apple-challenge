import numpy as np
from sys import stdout
from time import sleep,time_ns
from random import choice
from pygame import mixer
from Constantes import *
mixer.init()
music=mixer.music
Kuro=choice(["@","#","M"])
Shiro=choice(["_","-"," "])

matric=np.load(PACKED_ARRAY).
#matric=np.unpackbits(matric)
matric=matric.reshape(FRAME_NUMBER,SIZE[1],SIZE[0])
matric=np.where(matric!=0,Kuro," ")
matric=matric.repeat(2,2)
print('\n')


music.load("Audio.mp3")
stdout.write("\033[2J")
stdout.write("\033[34m")
k=0
while True:
    buffer=[]
    stdout.write("\033[H")
    for line in matric[k]:
        buffer.append(''.join(line))
    stdout.write("\n".join(buffer))
    stdout.flush()
    if k==0:
        music.play()
        start=time_ns()
    o=int(((mixer.music.get_pos())/1_000)*30)
    k+=1+(o-k)
    k=k%6572
    sleep(1/30)