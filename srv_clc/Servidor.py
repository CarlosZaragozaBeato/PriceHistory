import socket


def Servidor(ip:str, puerto:int, conexionesMax:int):
    infoConexion = (ip, puerto)
    
    socketSrv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketSrv.bind(infoConexion)
    socketSrv.listen(conexionesMax)
    
    print("Esperando conexiones en %s:%s" %(ip, puerto))
    cliente, direccion = socketSrv.accept()
    print("Conexion establecida con %s:%s" %(direccion[0], direccion[1]))
    
    
    while True:
        datos = cliente.recv(1024)
        
        if datos == "exit":
            cliente.send("exit")
            break
        
        print("Recibido %s" %datos)
        cliente.sendall("--RECIBIDO--".encode())
    
    print("---------CONEXION CERRADA-----------------")
    socketSrv.close()
    


Servidor('127.0.0.1', 8080,5)