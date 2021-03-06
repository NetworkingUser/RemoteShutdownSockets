import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=1524

s.connect((host,port))
    
