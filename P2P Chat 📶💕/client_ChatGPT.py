
import socket
import threading
from cryptography.fernet import Fernet

#generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

#function to encrypt message
def encrypt(message):
    return cipher.encrypt(message)

#function to decrypt message
def decrypt(cipher_text):
    return cipher.decrypt(cipher_text)

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                decrypted_message = decrypt(message)
                broadcast_message = f'{nickname}: {decrypted_message}'
                self.broadcast(encrypt(broadcast_message))
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(encrypt(f'{nickname} left the chat!'))
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            client.send(encrypt('NICK'.encode()))
            nickname = client.recv(1024).decode()
            self.nicknames.append(nickname)
            client.send(encrypt('Connected to the server!'.encode()))
            print(f'{nickname} connected!')
            client.send(encrypt(f'{nickname} connected!'.encode()))
            self.clients.append(client)
            client.send(encrypt(f'{nickname} connected!'.encode()))
            client.send(key)
            clientThread = threading.Thread(target=self.handle, args=(client,))
            clientThread.start()


peer = Peer('127.0.0.1', 55555)
receiveThread = threading.Thread(target=peer.receive)
receiveThread.start()
