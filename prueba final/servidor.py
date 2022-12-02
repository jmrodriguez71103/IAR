import socket
import json

with open('data.json') as file:
    data = json.load(file)

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mi_socket.bind ( ('localhost', 10000) )
mi_socket.listen(5)

serialize= json.dumps(data)

while True:
    conexion, addr = mi_socket.accept()
    print ("Nueva conexion")

    print (data)
    #conexion.send(data)
    conexion.send(serialize.encode())
    conexion.close()
