# On a pour depart, un chiffre aleatoire qui est choisi
# apres, le jeu nous demande de taper un nombre entre 0 et 100
# si la reponse est inerieur au nombre aleatoir
# il doit afficher "le nombre est plus grand"
# si la reponse est superieur au nombre aleatoire
# il doit afficher "le nombre est plus petit"
# et sinon, vous avez gane.
# Ici on importe une librairie qui contient des fonctions aleatoire.
import random 

# intialise nos variables nbaleatoire et trouver nbaleatoire sera genere par l'odrinateur.
# Trouver est un boonlean qui est egale a Faux.
nbAleatoire = random.randrange(0,100)
trouver = False

# Tant que trouver est egale a Faux on continue.
while trouver == False:
    print("tape un nombre entre 0 et 100")
# On converti le nombre tape au clavier en int
    reponse = int(input() )
# On compare notre reponse avec le nbaleatoire.
    if reponse < nbAleatoire:
        print("le nombre est plus grand")
    elif reponse > nbAleatoire:
        print("le nombre est plus petit")

    else:
        print("vous avez gagne")
# On passe trouver a Vrai pour arreter la boucle.
        trouver = True
