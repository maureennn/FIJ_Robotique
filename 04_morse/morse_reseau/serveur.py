import network
import comMorse
import ledArduino

ADDRESS = "10.0.0.116"
PORT = 1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

while True :
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    thread.start()

    #notre communication

    message = thread.clientsocket.recv(4096)
    morse = message.decode("utf-8")

    print("message reçu :", morse)
    lettre = comMorse.decode(morse)

    print("message traduit :", lettre)
    ledArduino.envoiCaractere(lettre)
    
    thread.clientsocket.send("j'ai bien reçu le message".encode())