from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from  flask_login import LoginManager, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('config')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db = SQLAlchemy(session_options={"autoflush": False})

login_manager = LoginManager()
login_manager.init_app(app)

# allows us to use databases
migrate = Migrate(app, db, render_as_template=True)

from .models import User
from app import views, models

with app.app_context():
    db.create_all()
