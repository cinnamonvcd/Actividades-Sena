from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#datos conexión a la base de datos
user, password, host, database= "root","CTPIADSO2024*","localhost","flask_peliculas"

#cadena de Conexión mysql
cadenaConexion= f'mysql+pymysql://{user}:{password}@{host}/{database}'

app.config["SQLALCHEMY_DATABASE_URI"]=cadenaConexion

#crear objeto de tipo SqlAlchemy para la aplicación
db = SQLAlchemy(app)

#Iniciar la aplicación
if __name__=="__main__":
    #importar las rutas
    from routes.genero import *
    from routes.pelicula import *

    #crear las tablas a la base de datos
    with app.app_context():
        db.create_all()

    #ejecutar la aplicación
    app.run(port=5400, debug=True)

