from app.controllers import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')

marsh = Marshmallow(app)
sqlDB = SQLAlchemy(app)

CORS(app)

sqlDB.create_all()
