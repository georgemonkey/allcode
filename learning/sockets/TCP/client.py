import socket
import threading

name = input("Choose your name: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.45', 9999))

def receive():
    while True:
        try:
          
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
          
            print("ERROR!")
            client.close()
            break


def write():

    while True:
        message = '{}: {}'.format(name, input(''))
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

