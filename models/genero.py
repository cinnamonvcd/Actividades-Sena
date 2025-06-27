from mongoengine import *

# Crear clase que representa la colección Genero en la base de datos
class Genero(Document):
    nombre = StringField(max_length=50, unique=True, required=True)
# crear una funcion para mostrar
    def __str__(self):
        return self.nombre
