import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("192.168.1.45",9999))
server.listen()

client,addr=server.accept()

quit=False

while not quit:
    msg=client.recv(1024).decode('utf-8')
    if msg== 'quit':
        quit=True
    else:
        print(msg)    


    client.send(input("Message: ").encode('utf-8'))
    
