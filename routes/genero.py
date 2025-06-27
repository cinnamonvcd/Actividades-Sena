from flask import request,render_template,jsonify
from app import app, db
from models.genero import *
from sqlalchemy import exc

@app.route("/genero/", methods=['GET'])
def listarGeneros():
    try:
        mensaje = None
        # consulta para obtener todos los generos
        generos = Genero.query.all()
        listaGeneros = []
        for g in generos:
            genero = {
                "idGenero": g.idGenero,
                "genero": g.genNombre
            }
            listaGeneros.append(genero)
            
    except exc.SQLAlchemyError as error:
        mensaje = str(error)
    
    return {"mensaje": mensaje, "generos": listaGeneros}
