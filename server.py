#Chat room connection - client to client
import threading
import socket
host = '127.0.0.1'
port = 59000

#Creates a sever to listen for any incoming connections from clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

#manage the connections of each client
def manage_client(client):
    while True:
        try: #recieve the message from this client and broadcast it to all other clients
            msg = client.recv(1024)
            broadcast(msg)
        except: #if there is a problem with the connection remove the client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room'.encode('utf-8')) #encode for sending, decode for recieving
            aliases.remove(alias)
            break

#Recieve clients connections
def recieve():
    while True: 
        print("Server is listening...")
        client, address = server.accept() #accept all incoming connections (always running)
        print(f'connection is being established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has joined the chat room'.encode('utf-8'))
        client.send('you are now connected'.encode('utf-8'))

        thread = threading.Thread(target = manage_client, args=(client,))
        thread.start()

recieve()































