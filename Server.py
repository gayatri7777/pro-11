import socket
from  threading import Thread
import time
import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer



IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

is_dir_exists = os.path.isdir('shared_files')
print(is_dir_exists)
if(not is_dir_exists):
    os.makedirs('shared_files')
    



def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.secket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    SERVER.listen(100)
    
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")
    
    
    
    
def handleClient(client, client_name):
    global clients
    global BUFFER_SIZE
    global SERVER

    # Sending welcome message
    banner1 = "Welcome, You are now connected to Server!\nClick on Refresh to see all available users.\nSelect the user and click on Connect to start chatting."
    client.send(banner1.encode())
    
def acceptConnections():
    global SERVER
    global client
    
    
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client"    : client,
            "address"   : addr,
            "connected_with" : "",
            "file_name"      : "",
            "file_size"      : 4096
        }
            
        print(f"Connection established with {client_name} : {addr}")
        
        thread = Thread(target =  handleClient, args = (client,client_name,))
        thread.start()
        
        
        
        
def setup():
    print("\n\t\t\t\t\t\tIP_MESSENGER\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    SERVER.listen(100)
    
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")
    
    acceptConnections()
    
    
    
def ftp():
    global IP_ADDRESS
    
    authorizer = DummyAuthorizer()
    authorizer.add_user("lftpd","lftpd",".",perm="elradfmw")
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    ftp_server = FTPServer((IP_ADDRESS,21),handler)
    ftp_server.serve_forever()
    
setup_thread = Thread(target=setup)
setup_thread.start()

ftp_thread = Thread(target=setup)
ftp_thread.start()
 