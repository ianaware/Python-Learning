import socket

# Set up the client
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a socket object using IPv4 and TCP protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Send data
    client_socket.sendall(b'Hello, world')

    # Receive and print the response
    data = client_socket.recv(1024)
    print(f"Received {data.decode()} from the server")

# The socket is closed when exiting the 'with' block
