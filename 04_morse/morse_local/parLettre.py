import dicoMatrice2D
import comMorse
import ledArduino

print("tape un code morse")
code = input()
reponse = comMorse.decode(code)
ledArduino.envoiCaractere(reponse)