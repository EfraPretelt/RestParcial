from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)

#configuración 
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/Data.db'
app.config['SQLALCHEMY_TRACK_MODIFICACTION'] = False

app.secret_key = "asdsaasdasadsadasdas"

#base de datos
db = SQLAlchemy(app)


from .views import app
 

def create_app():
    Bootstrap(app)
    return app