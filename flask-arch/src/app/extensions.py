from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


database = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()
