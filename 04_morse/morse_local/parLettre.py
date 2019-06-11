import dicoMatrice2D
import comMorse
import ledArduino

print("tape une lettre")
lettre = input()
reponseMorse = comMorse.encode(lettre)
print("le code morse est :",reponseMorse)


reponse = comMorse.decode(reponseMorse)
ledArduino.envoiCaractere(reponse)