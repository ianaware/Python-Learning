import socket
import ssl

# Create a regular socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL for secure communication
mysock = ssl.create_default_context().wrap_socket(mysock, server_hostname='data.pr4e.org')

# Connect to the server (Note: HTTPS default port is 443)
mysock.connect(('data.pr4e.org', 443))

# Prepare the HTTP GET command. Remember, the Host header is required for HTTP/1.1
cmd = 'GET /intro-short.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()

# Send the prepared command through the secure socket
mysock.send(cmd)

# Continuously receive data from the server and print it
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket connection once done
mysock.close()
