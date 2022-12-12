import socket
import json
from random import uniform

def rand_number():
    return uniform(0, 90)


with open('data.json') as file:
    data = json.load(file)

while True:
    mi_socket = socket.socket()
    mi_socket.connect( ('localhost', 15000) )
    data["x"] = rand_number() ;
    data["y"] = rand_number() ;
    print(data)
    serialize = json.dumps(data)
    mi_socket.send(serialize.encode())
    respuesta = mi_socket.recv(1024)
    print (respuesta.decode())
    mi_socket.close()
