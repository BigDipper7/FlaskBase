from flask import Flask, g
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)

# models
from app.models.adminModel import Admin


# routes
from app.routes import adminRoute


