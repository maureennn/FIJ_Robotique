import i2cComm
import time
import dicoMatrice2D

def envoiCaractere(lettre="a") :

    matrice = dicoMatrice2D.dico2D[lettre]
    for ligne in matrice :
        for led in ligne :
            i2cComm.writeNumber(led)

#print("On va afficher la lettre a")
#lettre = input()
#dicoMatrice2D.testMatrice2D(lettre)

#envoiCaractere("c")
