#C'est un json mais façon python, parce que flemme de faire un vrai json

SIZE= (80,60) #Taille de l'image, conditionne sa qualité

FRAME_NUMBER=6572   #Nombre de Frame de la vidéo
OFFSET=52

FPS=30 #Les FPS de la vidéo, ma mmatrice à moi est reglée sur 30FPS
NANOSECONDS_PER_FRAMES=(1/FPS)*1000000000    

FRAME_PATH="Out/"

BINFRAME_PATH="out/"

PACKED_ARRAY=f"{SIZE}.npy".replace(' ','')   #Le fichier binaire

CODED_ARRAY=f"Truquage.npy".replace(' ','')   #Le fichier binaire avec un message

WINDOW= 480,360     #La taille de la fenêtre

AUDIO="Audio.mp3"

EXTENSION='.jpg'