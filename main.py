from fastapi import FastAPI

app = FastAPI()

#Definimos una ruta para manejar solicitudes HTTP GET en la raiz ("/")
@app.get("/")
def read_root():
    return {"message": "Hola comunidad de HUMAI, soy Javi"}