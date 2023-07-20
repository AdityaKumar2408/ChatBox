# ChatBox

This is a simple implementation of a Socket Chat application that allows users to communicate with each other using their IP addresses. The application uses Python's socket library to establish a connection between clients and enable real-time chatting.


**Requirements**

To run this Socket Chat application, you need to have the following installed:

* Python 3.x


**Features**

* Real-time messaging: Users can send and receive messages in real-time.

* IP address-based connections: The chat application identifies clients based on their IP addresses.

![Screenshot (497)](https://github.com/AdityaKumar2408/ChatBox/assets/110921916/6f97369f-00e7-49dc-af40-c06d9dce9a45)


**How it Works**

The Socket Chat application uses a client-server architecture. The server listens on a specific port for incoming connections from clients. When a client tries to connect, the server establishes a socket connection with the client.

The clients enter the IP address of the server to initiate the connection. Once connected, clients can exchange messages through the server. The server acts as an intermediary, relaying messages between connected clients.

# License

This project is licensed under the MIT License.
