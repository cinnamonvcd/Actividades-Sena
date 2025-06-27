from flask import request,jsonify
from app import app, db
from models.genero import *
from models.pelicula import *
from sqlalchemy import exc

@app.route("/pelicula/", methods=['GET','POST'])
def listarPeliculas():
    try:
        mensaje = None
        if request.method == 'GET':
            #peliculas una lista de objetos tipo peliculas
            peliculas = Pelicula.query.all()
            #cada vez q recorra crea una pelicula
            listaPeliculas = []
            #crea el diccionario
            for p in peliculas:
                pelicula = {
                    "idPelicula": p.idPelicula,
                    "codigo": p.pelCodigo,
                    "titulo": p.pelTitulo,
                    "protagonista": p.pelProtagonista,
                    "duracion": p.pelDuracion,
                    "genero": {
                        
                        "idGenero": p.genero.idGenero,
                        "nombre": p.genero.genNombre
                    },
                    "foto": p.pelFoto
                }
                listaPeliculas.append(pelicula)
            return jsonify({"mensaje": mensaje,"pelicula":listarPeliculas})
        elif request.method=='POST':
            datos=request.get_json()
            print(datos)
            #creacion del objeto a nivel python
            p = Pelicula(pelCodigo= datos['codigo'],
                         pelTitulo=datos['titulo'],
                         pelProtagonista=datos['protagonista'],
                         pelDuracion=datos['duracion'],
                         pelResumen=datos['resumen'],
                         pelFoto=datos['foto'],
                         pelGenero=datos['genero'])
            db.session.add(p)
            db.session.commit()
            mensaje="Pelicula agragada correctamente"
            return jsonify({"mensaje": mensaje})
    
    except exc.SQLAlchemyError as error:
        mensaje = str(error)

    return jsonify({"mensaje": mensaje})

@app.route("/pelicula/<int:id>",methods=['GET']) 
def consultarPeliculaPorId(id):
    try:
        mensaje = None
        if request.method =='GET':
            p = Pelicula.query.get(id)
            if (p is None):
                mensaje ="No existe pelicula con ese Codigo"
                pelicula = p
            
            else: 
                pelicula = {
                    "idPelicula": p.idPelicula,
                    "codigo": p.pelCodigo,
                    "titulo": p.pelTitulo,
                    "protagonista": p.pelProtagonista,
                    "duracion": p.pelDuracion,
                    "genero": {
                       
                        "idGenero": p.genero.idGenero,
                        "nombre": p.genero.genNombre
                    },
                    "foto": p.pelFoto
                }
                
    except exc.SQLAlchemyError as error:
        mensaje = str(error) 
        
    return jsonify({"mensaje":mensaje,"pelicula":pelicula})

@app.route("/eliminarPelicula/<int:id>",methods=['DELETE'])
def eliminarPelicula(id):
    try:
        if request.method == 'DELETE':
            peliculaEliminar = Pelicula.query.get(id)
            if peliculaEliminar is None:
                mensaje= "No existe pelicula con este codigo"
                
            else:
                db.session.delete(peliculaEliminar)
                db.session.commit()
                mensaje="Pelicula Eliminada"
        
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    return jsonify({"mensaje":mensaje})


@app.route("/actualizarPelicula/<int:id>", methods=['PUT'])
def actualizarPelicula(id):
    try:
        mensaje = None
        if request.method == 'PUT':
            datos = request.get_json()
            p = Pelicula.query.get(datos['id'])
            if (p is None):
                mensaje = "No existe pelicula con ese Codigo"
            else:
                p.pelCodigo = datos['codigo']
                p.pelTitulo = datos['titulo']
                p.pelProtagonista = datos['protagonista']
                p.pelDuracion = datos['duracion']
                p.pelResumen = datos['resumen']
                p.pelFoto = datos['foto']
                p.pelGenero = datos['genero']
                
                db.session.commit()
                mensaje = "Pelicula actualizada correctamente"
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    
    return jsonify({"mensaje": mensaje})