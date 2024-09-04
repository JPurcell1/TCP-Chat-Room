import threading
import socket
alias = input('Choose an alias: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_recieve():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8') #encode for sending, decode for recieving
            if msg == "alias?":
               client.send(alias.encode('utf-8'))
            else:
                print(msg)
        except: 
            print('Error')
            client.close
            break

#Sending messages on the sever
def client_send():
    while True:
        msg = f'{alias}: {input('')}' 
        client.send(msg.encode('utf-8'))

recieve_thread = threading.Thread(target = client_recieve)
recieve_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()