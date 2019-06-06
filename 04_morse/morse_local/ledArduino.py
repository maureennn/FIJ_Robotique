import i2cComm
import time

dico = {"a": [  [1,1,1,1,1,] ,
                [1,0,0,0,1] ,
                [1,1,1,1,1] ,
                [1,0,0,0,1] ,
                [1,0,0,0,1]] ,

        "b":[   [1,1,1,1,0] ,
                [1,0,0,0,1] ,
                [1,1,1,1,0] ,
                [1,0,0,0,1] ,
                [1,1,1,1,0]] ,
}

def envoiCaractere() :

    matrice = dico["a"]
    for ligne in matrice :
        for led in ligne :
            i2cComm.writeNumber(led)

print("On va afficher la lettre a")
envoiCaractere()
