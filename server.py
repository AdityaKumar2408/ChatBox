import socket

PORT = 9999  # The Port number which isn't reserved by some internal system
HOST = "localhost"  # either localhost or IP Address of the system depending on connection router  will be the HOST

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: This specifies the address family for IPv4. AF_INET
# socket.SOCK_STREAM: This specifies the socket type as TCP (Transmission Control Protocol)

server.bind((HOST, PORT))
# server.bind((HOST, PORT)) is used to bind the server socket to a specific address and port.

server.listen()
# server.listen() listens for incoming connections from client

client, addr = server.accept()
# server.accept() accepts incoming connections from client

done = True

while done:
    msg = client.recv(1024).decode('utf-8')
    # client.recv(1024) is used to receive the byte data within the limit of 1024 bytes
    if msg == "quit":
        done = False
    else:
        print("Message from client: ", msg)
    client.send(input().encode('utf-8'))
    # client.send() to send the encoded data to client
# close the connection
client.close()
server.close()