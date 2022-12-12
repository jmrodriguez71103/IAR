import socket
import json


def read_json_file(): 
    with open('data.json') as file:
        data = json.load(file)
    return data 
    
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind ( ('localhost', 15001) )
mi_socket.listen(5)

serialize= json.dumps(read_json_file())

while True:
    conexion, addr = mi_socket.accept()
    print ("Nueva conexion")
    serialize= json.dumps(read_json_file())
    print (f'Serializacion: {serialize}')   
    conexion.send(serialize.encode())
    client_Rx = conexion.recv(1024)
    print (f'CLiente_rx: {client_Rx}')   
    conexion.close()
    