Meh, petit manuel à l'usage du consultant

Rule 86: "If there is a screen, Bad Apple will be seen"
    C'est là loi. Du coup j'ai tenté le Bad Apple but... J'ai pas slay y a zéro originalité mais au moins ça existe

À la base, c'était un projet pour apprendre les matrices puis ça finis comme ça...

FAQ:

1. C'est quoi ce truc?
        R/C'est mon petit bébé un projet de stéganographie vidéo (pour la faire courte une façon de cacher un arbre dans une forêt) permettant de transporter presque incogniton un fichier dans une vidéo en noir et blanc (pas en nuance de gris... Ne pas confondre). Et effectivement la vidéo ne peut être lue que par script sinon ce serait pas drôle. Pour l'instant je ne peux pas encore extraire de moi-même les frames de la vidéo donc on va dire que c'est plus un diaporama d'agent secret...
        Ah et il y a aussi un afficheur de matrice 3d binaire en vidéo ascii, un nom cool pour dire que non seulement tu peut voir ta vidéo mais tu peux aussi l'afficher en texte dansant dans la console...

2.Comment ça marche?
        R/C'est plutôt simple en vrai, la partie la plus compliquée est de résoudre le problème de dépendance pour ça tu te connectes à Internet et tu ouvres l'invite de commande dans ton env et tu fais
                pip install requirements.txt
                (En soit tu peux skip l'étape si tu as des versions assez récentes de numpy,pillow,pygame,rich)
        Si tu veux enjoy la vidéo il te faudra son audio et toutes les frames de celle-ci, dépose l'audio dans le dossier racine (au même niveau que ce fichier) et renomme AUDIO dans constante et les frames dans le dossier /frames puis crée un dossier /Binframes ensuite lance Outils.py. Une fois le programme terminé, lance Numpytest.py et tu verras s'afficher la fenêtre
        Pour l'ascii, c'est pareil que pour la vidéo sauf qu'à la place d'ouvrir Numpytest, c'est Ascii-table qu'il faut lancer
        Par contre si tu veux cacher, je n'ai encore rien fait de user friendly désolé... À dans deux versions
        Mais la procédure est simple si tu connais un peu te débrouiller, il y a un sample à la fin du fichier codec, ça devrait servir...


3.Qu'est-ce que je peux custom en deux-deux sans vraiment tout casser?
        R/Dans Constantes.py
            Il y a là théoriquement les trucs les plus simples qu'une personne voudrait modifier:
            _SIZE choisis la qualité de l'image mais aussi la taille du fichier vidéo, il vaut 60x80. La qualité est faible parce qu'avec ma méthode de compression, une trop bonne qualité fait gonfler la taille du fichier, genre une vidéo de 3 minutes mais de 142 Mo, tu y crois toi? Mais aussi la taille des matrices, avec la RAMpocalypse pas sûr d'en avoir une bonne matrice qui tourne sans cataclysmer ton pc. Évidemment on pourrait pousser la compresssion plus loin mais ça rendrait inopérante toute tentative de stéganographie.
            _NUMBER_FRAMES définis la longueur de trame, en gros le nombre de frame au cas où tu as ton propre diaporama de photo, note que par défaut le nombres de frames pris en compte est 6572, mais les frames visibles sont à 6520, j'en ai coupé 52 vers la fin pour matcher avec la musque qui elle s'arrêtait net.
                Pour corriger ça, mets OFFSET à zéro
            _NANOSECONDS_PER_FRAMES, c'est l'inverse des FPS en gros c'est la vitesse de lecture de la vidéo là on est à 30FPS
            _FRAME_PATH, c'est le chemin d'accès au dossier de la diapo
            _BINFRAME_PATH, ça c'est un dossier qui sera créé de toute façon, mais évitons les risques autant le créer maintenant
            _PACKED_ARRAY, ça c'est le nom du fichier de la 'vidéo' qui sera créé 
            _WINDOW c'est la taille de la fenêtre Pygame
            _AUDIO c'est l'audio en question
            _CODED_ARRAY, c'est le nom du fichier avec la matrice qui contient un message
        
Note: Vu que c'est le bazar il peut arriver qu'il y ait un problème dans la lecture lors des reshape, bon, ce sera pas tout le temps mais vaut mieux prévenir que guérir, alors les erreurs du style "Cannot reshape (Un grand chiffre long sa mère) with shape {FRAME_NUMBER},{SIZE},{SIZE}" sont un problème de mathématique, alors on sort la calculette:
    Coupable numéro 1: Tu as peut-être oublié d'actualiser les valeurs de FRAME_NUMBER ou de SIZE vérifie simplement en divisant le gros
        chiffre par (frame x height x width) soit ça donne 1, alors c'est le pc qui déconne, soit ça donne 8 ou (0.625)alors c'est un problème de bit, soit ça donne autre chose que 1 ou 8 ou 0.625 et là c'est bel et bien un problème d'actualisation de la taille de ta vidéo. Vérifie que tu as bien actualisé la taille de la trame et la longueur de trame sinon tu devras faire repasser ta matrice à la case conversion-enregistrement.
    Coupable 2... C'est moi, oui MOA, il arrive que les matrices soient compressés en octet plutôt qu'en bit ou à l'inverse, en bit plutôt
        qu'en octet, alors ce type d'erreur ne survien que dans Numpytest.py ou dans Ascii-table.py lors du chargement de la matrice, alors si c'est 8 le reste, c'est que tu as dépaqueté une matrice déjà dépaquettée dans ce cas commente la ligne 13 du fichier en plaçant un # devant, si c'est 0.625 décommente la ligne 13, c'est tout je pense.
