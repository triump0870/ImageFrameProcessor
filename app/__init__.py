# app/__init__.py
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rohanroy:@localhost/image_processor'

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import api  # Importing here to avoid circular imports
