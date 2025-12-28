import numpy as np

#Désordonne les éléments d'une matrice selon la clé
def encode(data,key):
    shape= data.shape
    raveled=data.ravel()

    indice=np.arange(len(raveled))

    np.random.seed(key)
    np.random.shuffle(indice)

    return raveled[indice].reshape(shape)

#Réordonne les éléments d'une matrice selon la clé
def decode(data,key):
    shape=data.shape

    flat_data=data.ravel()
    indices=np.arange(len(flat_data))

    np.random.seed(key)
    np.random.shuffle(indices)

    return flat_data[indices].reshape(shape)

#Somme la ligne de façon alternée et renvoie le résultat
def alt_sum(data):
    length=len(data)
    treat=np.array(data)

    if length%2:
        treat=np.insert(treat,length//2+1,0)
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


def Gen_key(*args:iter):
    #On récupère chaque lettre de chaque mot mis en clé puis on retire les doublons et on compte les occurences
    #Après la boucle de sommation de Love
    data=[]
    for element in args:
        for i in element:
            data.append((i))
    data_set=list(dict.fromkeys(data))
    occur=[data.count(i) for i in data_set]

    key=alt_sum(occur)
    while len(key)!=2:
        key=alt_sum(key)
        print(key)
    return key

