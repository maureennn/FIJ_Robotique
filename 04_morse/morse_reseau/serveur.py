import network
import comMorse
import ledArduino

ADDESS = ""
PORT = 1111

socket = network.newServerSocket()
socket.bind((ADDESS,PORT))

while True :
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    thread.start()

    #notre communication

    message = thread.clientsocket.recv(4096)
    morse = message.decode("etf-8")

    print("message reçu :", morse)
    lettre = comMorse.decode(morse)

    print("message traduit :", lettre)
    ledArduino.envoiCaractere(lettre)
    
    thread.clientsocket.send("j'ai bien reçu le message".encode())