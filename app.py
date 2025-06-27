from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os

load_dotenv()

#1crear el objeto flask
app = Flask(__name__)
#3 crear las carpetas y en que rutas iran las fotos de las peliculas 
app.config["UPLOAD_FOLDER"] = "./static/imagenes"
# crea la lista y el objeto json en db como se va a llamar la base de datos
app.config['MONGODB_SETTINGS'] = [{
    "db": "GestionPeliculas",
    "host": os.environ.get("URI")
    ## no lo necesitamos para atlas"port": 27017
}]
#2 crear el objeto db 
db = MongoEngine(app)
#4 para arrancar la aplicacion 
if __name__ == "__main__":
    from routes.genero import *
    from routes.pelicula import *
    app.run(port=5400, host="0.0.0.0", debug=True)
