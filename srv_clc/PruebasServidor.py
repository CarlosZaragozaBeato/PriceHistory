# Configurar el servidor
import http.server
import socketserver

from PruebasCliente import MyHandler

PORT = 8000
Handler = MyHandler

# Crear el servidor
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print("Servidor iniciado en el puerto", PORT)
    
    httpd.serve_forever()
    
    
    
    
    
    
    
    
    
    
    
    
"""
import socket

# Crea el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asigna una dirección IP y un puerto al socket del servidor
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Escucha conexiones entrantes
server_socket.listen(1)
print('El servidor está listo para recibir solicitudes')

while True:
    # Espera a que llegue una solicitud
    connection, client_address = server_socket.accept()

    try:
        print('Conexión desde', client_address)

        # Recibe los datos de la solicitud
        request_data = connection.recv(1024).decode()

        # Imprime los datos de la solicitud
        print('Solicitud recibida:')
        print(request_data)

        # Envía una respuesta al cliente
        response_data = 'Respuesta del servidor'
        response_headers = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n'.format(len(response_data))
        connection.send(response_headers.encode() + response_data.encode())

    finally:
        # Cierra la conexión
        connection.close()
"""