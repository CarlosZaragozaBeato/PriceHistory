import requests

url = 'http://127.0.0.1:8085'  # URL del servidor
data = {'nombre': 'Juan', 'edad': 30}  # Datos a enviar en la solicitud POST


def EnviarRespuesta(mensaje:str, url:str):
    requests.post(url, mensaje)

