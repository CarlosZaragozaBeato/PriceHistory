import socket


def Cliente(ipServidor:str, puertoServidor:int):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ipServidor, puertoServidor))
    
    print("Conectado con el servidor ----> %s:%s" %(ipServidor, puertoServidor))
    
    while True:
        msg = input("> ")
        cliente.send(msg.encode())
        respuesta = cliente.recv(4096)
        print(respuesta.decode())
        if respuesta == "exit":
            break
        
    print("-----------CONEXION CERRADA--------------")
    cliente.close()
    
    
Cliente('127.0.0.1',8080)