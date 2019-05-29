# il existe deux types de bloucles

# While > tant que...
# Avec un compteur qui diminue à chaque tour
compteur = 10

while compteur >= 0:
    print("le cours est fini dans :", compteur)
    compteur = compteur - 1

# Avec un boolean
flag = True

while flag:
    print("bonjour")
    flag = False

# For > pour chaque
phrase = "Bonjour a tous !"

for lettre in phrase:
    if lettre in "aeiouy":
        print(lettre)
