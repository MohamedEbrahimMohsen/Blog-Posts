from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa6e9ff863d8b1af936885261c390104' #generated key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

# from flaskblog.security import authentications
from flaskblog.routes import home, about, login, logout, register, account