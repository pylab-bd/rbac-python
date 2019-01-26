from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

jwt = JWTManager(app)
