from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


database: SQLAlchemy = SQLAlchemy()
bcrypt: Bcrypt = Bcrypt()
csrf: CSRFProtect = CSRFProtect()
