import http.server
import socketserver

# Crear un manejador de solicitudes
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Obtener los datos de la solicitud
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Procesar los datos
        response = "Los datos recibidos son: {}".format(post_data)
        
        # Responder a la solicitud
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(response.encode('utf-8')))
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
        

import requests

url = 'http://127.0.0.1:8000'  # URL del servidor
data = {'nombre': 'Juan', 'edad': 30}  # Datos a enviar en la solicitud POST

response = requests.post(url, data=data)

print(response.text)  # Imprime la respuesta del servidor







"""
import socket

# Crea el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket del cliente al servidor
server_address = ('localhost', 8080)
client_socket.connect(server_address)

# Envía una solicitud al servidor
request_data = 'POST / HTTP/1.1\nHost: localhost\nContent-Type: text/plain\nContent-Length: 5\n\nHola'
client_socket.sendall(request_data.encode())

# Recibe la respuesta del servidor
response_data = client_socket.recv(1024).decode()

# Imprime la respuesta del servidor
print('Respuesta recibida:')
print(response_data)

# Cierra la conexión del cliente
client_socket.close()
"""