import network
import comMorse

ADDRESS =""
PORT = 1111

while True:

    socket = network.newClientSocket()
    socket.connect((ADDRESS,PORT))

    print("ecris une lettre")
    lettre = input()

    morse = comMorse.encode(lettre)
    socket.send(morse.encode())

    reponse = socket.recv(4096)
    print(reponse)