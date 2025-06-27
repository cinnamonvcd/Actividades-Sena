from bson import ObjectId
from flask import request
from models.genero import Genero
from app import app,db


@app.route("/genero/", methods=['GET'])
def listarGeneros():
    """
    Función que retorna la lista de generos
    existentes en la colección generos
    Returns:
        _type_: lista de generos
    """
    try:
        mensaje = None
        #esto es como db genero.find() en mongo
        generos = Genero.objects()
    except Exception as error:
        mensaje = str(error)
    
    return {"mensaje": mensaje, "generos": generos}

@app.route("/genero/", methods=['POST'])
def addGenero():
    try:
        mensaje = None
        estado = False
        if request.method == 'POST':
            datos = request.get_json(force=True)
            # esta linea significa lo mismo q la de abajo genero = genero(nombre=datos['nombre])
            genero = Genero(**datos)
            genero.save()
            # los posibles errores pueden terminar en la linea 32 si no el estado se convierte en true
            estado = True
            mensaje = "Genero agregado correctamente"
        else:
            mensaje = "No permitido"
    except Exception as error:
        mensaje = str(error)
        
    #recibir los datos en formato json
    #el estado por si es true lo agrego y si llega false no lo pudo agregar
    return {"estado": estado, "mensaje": mensaje}

@app.route("/genero/",methods=['PUT'])
def updateGenero():
    try:
        mensaje= None
        estado = False
        if request.method == 'PUT':
            datos = request.get_json(force=True)
            genero = Genero.objects(id=ObjectId(datos['id'])).first()
            if genero is not None:
                genero.nombre=datos['nombre']
                genero.Genero=ObjectId(datos['genero'])
                genero.save()
                estado= True
                mensaje= "Genero actualizado"
            else:
                mensaje= "No existe genero con el ID para actualizar"
                
        
    except Exception as error:
        mensaje = str(error)


    return {"estado": estado, "mensaje": mensaje}

