# Liste des mots du pendu
liste_mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]

#dico des stades du pendu
chances = {  7:["____ ",
                "|/",
                "|",
                "|",
                "|",
                "|____"],
             6:["____ ",
                "|/ |",
                "|",
                "|",
                "|",
                "|____"],
             5:["____ ",
                "|/ |",
                "|  0",
                "|",
                "|",
                "|____"],
             4:["____ ",
                "|/ |",
                "| \\0",
                "|",
                "|",
                "|____"],
             3:["____ ",
                "|/ |",
                "| \\0/",
                "|", 
                "|",
                "|____"],
             2:["____ ",
                "|/ |",
                "| \\0/",
                "|  |",
                "|",
                "|____"],
             1:["____ ",
                "|/ |",
                "| \\0/",
                "|  |",
                "| /",
                "|____"],
             0:["____ ",
                "|/ |",
                "| \\0/",
                "|  |",
                "| / \\",
                "|____"],

}

# fonction qui affiche le pendu en fonction du nombre de chance restante
def pendu (chance=0):
   for ligne in chances[chance]:
      print(ligne)

# fonction qui masque les lettre sauf celles deja trouvee passee en parametre
def masque (mot_a_trouver,les_lettres_trouvees):
   mot_masque=""
  
   for lettre in mot_a_trouver:
      if lettre in les_lettres_trouvees :
         mot_masque += lettre
      else :
         mot_masque += "*"

   return mot_masque