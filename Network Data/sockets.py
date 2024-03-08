# Import necessary libraries
import socket  # Library for network connections
import ssl     # Library for secure connections over SSL/TLS

# Create a new socket object, using IPv4 addressing and TCP (a stream-based protocol)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the original socket with SSL for secure communication and set the server's hostname for SSL handshake
my_ssl_socket = ssl.create_default_context().wrap_socket(my_socket, server_hostname='www.py4e.com')

# Establish a connection to the server ('www.py4e.com') on port 443 (the standard port for HTTPS)
my_ssl_socket.connect(('www.py4e.com', 443))

# Prepare the HTTP GET request to fetch the content of romeo.txt. 
# The request is encoded into bytes as required by the network protocol.
cmd = 'GET /code3/romeo.txt HTTP/1.1\r\nHost: www.py4e.com\r\n\r\n'.encode()

# Send the prepared command (HTTP GET request) through the secure socket
my_ssl_socket.send(cmd)

# Start an infinite loop to receive data from the server in chunks of 512 bytes
while True:
    # Receive a chunk of data from the server
    data = my_ssl_socket.recv(512)
    
    # If there is no more data (the server closed the connection), break out of the loop
    if len(data) < 1:
        break
    
    # Decode the received bytes into a string and print it out, 
    # without adding a new line after each chunk (hence 'end=''')
    print(data.decode(), end='')

# Close the secure socket connection once all data is received and printed
my_ssl_socket.close()