import requests
import json

POST_URL = "https://script.google.com/macros/s/AKfycbyKy9YsgiJ30RvukIgXC0TVGzvuRWLSQIm7JcTP3DcMwZMmFZl7LJvptB3ikW_7Jnsw/exec"
GET_URL = "https://script.google.com/macros/s/AKfycby7XInLIDjMgH__JjDHwXp4lGrSjL8pN6MisWAYZl2yTC-tK-BWNoRoE6FmXuw-jpDz/exec"

def guardar_usuario(nombre, email, password):
    data = {
        "nombre": nombre,
        "email": email, 
        "password": password
    }
    requests.post(POST_URL, data=json.dumps(data))

def obtener_usuarios():
    response = requests.get(GET_URL)
    return json.loads(response.text)