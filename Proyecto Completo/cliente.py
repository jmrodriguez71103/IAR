import socket
import json
import time 
from random import uniform 

def rand_number(): 
    return uniform(0, 90)



def read_json_file(): 
    with open('data.json') as file:
        data = json.load(file)
    return data 
    

while True:
    mi_socket = socket.socket()
    mi_socket.connect( ('192.168.1.102', 15000) )
    serialize = json.dumps(read_json_file())
    print(serialize.encode()) 
    #print(type(serialize.encode())) 
    mi_socket.send(serialize.encode()) 
    respuesta = mi_socket.recv(30)
    #print(f'respuesta{respuesta}') 
    #print (respuesta.decode('ascii'))
    mi_socket.close()
    time.sleep(10); 
