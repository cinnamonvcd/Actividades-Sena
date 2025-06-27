
from app import app
from bson import ObjectId
from flask import request
from models.pelicula import Pelicula
from models.genero import Genero

@app.route("/pelicula/", methods=['GET'])
def listarPelicula():
    try:
        mensaje = None
        peliculas = Pelicula.objects()
        
    except Exception as error:
        mensaje = str(error)

    return {"mensaje": mensaje, "peliculas": peliculas}

@app.route("/pelicula/", methods=['POST'])
def addPelicula():
    try:
        mensaje = None
        estado = False
        if request.method == "POST":
            datos = request.get_json(force=True)
            
            genero = Genero.objects (id=ObjectId(datos['genero']) ).first
            if genero is not None :
                pelicula = Pelicula(**datos)
                pelicula.save()
                estado = True
                mensaje = "Pelicula agregada correctamente"
            else: 
                mensaje= "No se puede agregar, el genero no existe"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)
        if "duplicate key" in mensaje:
            mensaje = "No se puede agregar, el codigo de la pelicula ya existe"

    return {"estado": estado, "mensaje": mensaje}

@app.route("/pelicula/",methods=['PUT'])
def updatePelicula():
    try:
        mensaje= None
        estado = False
        if request.method == 'PUT':
            datos = request.get_json(force=True)
            pelicula = Pelicula.objects(id=ObjectId(datos['id'])).first()
            if pelicula is not None:
                pelicula.codigo=datos['codigo']
                pelicula.titulo=datos['titulo']
                pelicula.protagonista=datos['protagonista']
                pelicula.duracion=datos['duracion']
                pelicula.resumen=datos['resumen']
                pelicula.foto=datos['foto']
                pelicula.genero=ObjectId(datos['genero'])
                pelicula.save()
                estado= True
                mensaje= "Pelicula actualizada"
            else:
                mensaje= "No existe pelicula con el ID para actualizar"
                
        
    except Exception as error:
        mensaje = str(error)


    return {"estado": estado, "mensaje": mensaje}

@app.route("/pelicula/", methods=['DELETE'])
def deletePelicula():
    try:
        estado = False
        mensaje = None
        datos =request.get_json(force=True)
        if request.method == 'DELETE':
            pelicula = Pelicula.objects(id=ObjectId(datos['id'])).first()
            

            if pelicula is not None:
                pelicula.delete()
                estado = True
                mensaje = "Película eliminada correctamente"
            else:
                mensaje = "No existe película con ese ID"


    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}

@app.route("/pelicula/<string:id>", methods=['GET'])
def deletePeliculaId(id):
    try:
        estado = False
        mensaje = None
        if request.method == 'GET':
            pelicula = Pelicula.objects(id=id).first()
            if pelicula is not None:
                pelicula.delete()
                estado = True
                mensaje = "Película eliminada correctamente"
            else:
                mensaje = "No existe película con ese ID"


    except Exception as error:
        mensaje = str(error)

    return {"estado": estado, "mensaje": mensaje}