import numpy as np
from rich import print
from Constantes import *

def print_code(msg):
    print(f"[green]{msg}[/green]")

def print_decode(msg):
    print(f"[blue]{msg}[/blue]")



#Désordonne les éléments d'une matrice selon la clé
def shuffle(data,key):
    shape= data.shape
    raveled=data.ravel()

    indice=np.arange(len(raveled))

    np.random.seed(key)
    np.random.shuffle(indice)

    return raveled[indice].reshape(shape)

#Réordonne les éléments d'une matrice selon la clé
def deshuffle(data,key):
    shape=data.shape
    recipe=np.zeros(len(data),dtype=np.uint8)

    flat_data=data.ravel()
    indices=np.arange(len(flat_data))

    np.random.seed(key)
    np.random.shuffle(indices)
    recipe[indices]=flat_data
    

    return recipe.reshape(shape)

#Somme la ligne de façon alternée et renvoie le résultat
#C'est un peu notre façon de randomiser la clé
def alt_sum(data)->list[int]:
    length=len(data)
    treat=np.array(data)

    if length%2:
        treat=np.insert(treat,(length//2)+1,0)
        length+=1

    #En divisant l'array en deux, puis en sommant la première partie avec l'inverse de la seconde on a ce qu'on voulait
    treat=treat.reshape(2,length//2)
    final=treat[0]+treat[1][::-1]
    to_send=[]
    #Là on gère les résultats à deux chiffres
    for i in final:
        for j in str(i):
            to_send.append(int(j))
    return to_send


def Gen_key(args:str)->int:
    #On récupère chaque lettre de chaque mot mis en clé puis on retire les doublons et on compte les occurences
    #Après la boucle de sommation de Love
    data=[i for i in args]
    data_set=list(dict.fromkeys(data))
    occur=[data.count(i) for i in data_set]
    key=occur
    l_count=0
    while len(key)!=2:
        key=alt_sum(key)
        if not len(key):
            print(f"[red]{key}... \nAlors, tu vas rire mais...\nCeci est une exception statistiquement impossible, genre une chance sur un million, j'arrive même pas à calculer\n Bref dis-moi comment t'as fait ce sera marrant[/red]")
            break
        if l_count>20:
            print("Alors soit ton mot de passe est vraiment, vraiment long, soit il est vraiment vraiment petit")
        l_count+=1
    return int("".join([str(i) for i in key]))

#C'est la règle de dispersion des pixels, c'est pas encore totalement au point mais c'est un début
def rule(num) -> bool:
        return (num%4==1)


#Là on a la fonction qui vas disperser selon les règles le message dans la matrice
#On découpe le morceau en pièce, par défaut c'est en lettre et on mets les morceaux dans la matrices
def hide(Core,data,seed):
    data=data.flatten()
    ZERO=np.zeros(len(Core.flatten()),dtype=np.uint8)
    ZERO_length=ZERO.size
    np.random.seed(seed)
    
    flat_data=Core.ravel()
    pieces=len(data)
    p_count=0
    l_count=0

    for frame in flat_data:
        if pieces==p_count:
            break
        else:
            if rule(l_count):
                flat_data[l_count]=data[p_count]
                p_count+=1
        l_count+=1
    name="Test.npy"
    np.save(name,flat_data)
    print_code(f"Hé, on a finis de préparer {name} ton message caché est prêt...")


#Récupère les n pieces d'une matrice truquée...
def find(Mod_Core,seed,pieces):
    Found=[]
    p_count=0
    l_count=0
    for frame in Mod_Core:
        if pieces==p_count:
            break
        else:
            if rule(l_count):
                Found.append(Mod_Core[l_count])
                p_count+=1
        l_count+=1
    return np.array(Found)

#Récupère un fichier texte et en fait une matrice
def convert_from_file(file,forest):
    try:
        with open(file) as fl:
            txt=fl.read()
            print_code('File opened')
            print_code(f"{len(txt)} Is the length")
            matrix=np.frombuffer(txt.encode(),dtype=np.uint8)
            if len(matrix.ravel())>= len(forest):
                print("TO HEAVY")
                fl.close()
            else:
                return matrix
    except UnicodeError:
        print("[red]File format not supported, we are working on it to make it available[/red]")   
    finally:
        print_code(f"File {file} converted successfully")

#Écrit un fichier texte avec les données d'une matrice
def convert_to_file(data,name="Spy"):
    The_file=data.tobytes().decode()
    print(The_file)
    with open(f"{name}.txt",'w') as Spy:
        Spy.write(The_file)


#C'est genre la boucle de codage
def CODE(file,forest,args:str):
    key= Gen_key(args)
    bit_file=convert_from_file(file,forest)
    bit_file=shuffle(bit_file,key)
    hide(forest,bit_file,key)


#C'est genre la boucle de décodage
def DECODE(forest,args:str):
    key=Gen_key(args)
    matrix=find(forest,key,6)
    bit_file=deshuffle(matrix,key)
    convert_to_file(bit_file)

#Sample de code
a=np.load(PACKED_ARRAY)
print_code("Loaded")
CODE("Message ulta top secret.txt",a,'_BlueF0xNaoss')

a=np.load(CODED_ARRAY)
DECODE(a,'_BlueF0xNaoss')