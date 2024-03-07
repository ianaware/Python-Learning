import socket

def run_server():
    #create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #set host and port for listening
    HOST = '127.0.0.1'
    PORT = 65432
    
     # Set the SO_REUSEADDR option to reuse the socket
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    #bind socket to host and port
    server_socket.bind((HOST, PORT))

    
    #start listening for connections
    server_socket.listen()
    print(f'Listening for connections on {HOST}:{PORT}', flush=True)
    
    
    #wait for a connection
    connection, address = server_socket.accept()
    print(f'Connection from {address} has been established')
    
    #close the connection
    connection.close()

run_server()