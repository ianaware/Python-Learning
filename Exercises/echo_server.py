'''

Now, for a practical exercise. You'll write a basic echo server that receives a message from the client and then sends it right back.

Server:

Import the socket module.

Create a socket object using socket.socket().

Bind the socket to localhost and a port of your choice.

Set the server to listen for incoming connections.

Accept a connection when one comes in.

Receive data from the client and send it back using the same connection.

Close the connection.

Client:
Import the socket module.
Create a socket object.
Connect to the server using the same host and port as the server.
Send some data to the server.
Receive the echo from the server and print it.
Close the socket.


'''

import socket #import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 65432

server_socket.bind((HOST, PORT))

server_socket.listen(1)
print(f'Server is listening on {HOST} {PORT}')

conn, adr = server_socket.accept()
print(f'Connected by {adr}')

while True:
    data = conn.recv(1024)
    if not data:
        conn.sendall(data)
        break
    
conn.close()
