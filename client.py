import socket

PORT = 9999  # The Port number which isn't reserved by some internal system
HOST = "localhost"  # either localhost or IP Address of the system depending on connection router  will be the HOST


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: This specifies the address family for IPv4. AF_INET
# socket.SOCK_STREAM: This specifies the socket type as TCP (Transmission Control Protocol)

client.connect((HOST, PORT))
# server.bind((HOST, PORT)) is used to connect the server socket to a specific address and port.


done = False

while not done:
    client.send(input().encode('utf-8'))
    # client.send() to send the encoded data to server
    msg = client.recv(1024).decode('utf-8')
    # client.recv(1024) is used to receive the byte data within the limit of 1024 bytes
    if msg == "quit":
        done = True
    else:
        print("Message from server: ", msg)
# close the connection
client.close()
