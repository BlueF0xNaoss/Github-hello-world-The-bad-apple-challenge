import numpy as np
from rich import print
from Constantes import SIZE

def print_code(onje):
    print(f"[green]{onje}[/green]")

def print_decode(onje):
    print(f"[blue]{onje}[/blue]")

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
    while len(key)!=2:
        key=alt_sum(key)
        if not len(key):
            print(f"[red]{key}... \nAlors, tu vas rire mais...\nCeci est une exception statistiquement impossible, genre une chance sur un million, j'arrive même pas à calculer\n Bref dis-moi comment t'as fait ce sera marrant[/red]")
            break
    return int("".join([str(i) for i in key]))


def rule(num) -> bool:
        return (num%4==1)



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
    np.save("Test.npy",flat_data)
    print_code("File already fine")


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

#Done
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
        print_code("Converted successfully?")


def convert_to_file(data):
    The_file=data.tobytes().decode()
    print(The_file)
    with open("Spy.txt",'w') as Spy:
        Spy.write(The_file)

def CODE(file,forest,args:str):
    key= Gen_key(args)
    bit_file=convert_from_file(file,forest)
    bit_file=shuffle(bit_file,key)
    hide(forest,bit_file,key)


def DECODE(forest,args:str):
    key=Gen_key(args)
    matrix=find(forest,key,9)
    bit_file=deshuffle(matrix,key)
    print_decode(bit_file)
    convert_to_file(bit_file)


a=np.load("(80,60).npy")
print_code("Loaded")
CODE("Secret.txt",a,'_BlueF0xNaoss')

a=np.load("Test.npy")
DECODE(a,'_BlueF0xNaoss')

