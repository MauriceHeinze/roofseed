from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

from app.utils import Trees
api = Trees()

db = SQLAlchemy(app)
from app.models import *
db.create_all()

from app.user.views import *
from app.utils.filters import *
