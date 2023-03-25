import requests


class Cliente:
    def __init__(self, url):
        self.url = url


    def EnviarRespuesta(self, mensaje:str):
        requests.post(self.url, mensaje)


