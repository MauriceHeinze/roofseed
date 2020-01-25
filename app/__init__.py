from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.utils import Trees
api = Trees()

from app.user.views import *
from app.utils.filters import *
