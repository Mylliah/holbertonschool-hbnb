from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
