import socket 

# Crea el socket del servidor



class Servidor:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Asigna una dirección IP y un puerto al socket del servidor
        self.server_address = ('127.0.0.1', 8085)
        self.server_socket.bind(self.server_address)

        # Escucha conexiones entrantes
        self.server_socket.listen(1)



    def StartServer(self):
        while True:
            #Espera a que llegue una solictud
            connection, client_address = self.server_socket.accept()

            try:
                request_data = connection.recv(1024).decode()

                #Envia una respuesta al cliente
                response_data = "Respuesta del servidor"
                response_headers = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n'.format(len(response_data))
                connection.send(response_headers.encode() + response_data.encode())
            finally:
                # Cierra la conexion 
                connection.close()


