import os

# Load data from .env file if avaible
from dotenv import load_dotenv
load_dotenv()

# Config for basedir
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # App infos
    SITENAME = "roofseed"
    APP_LOCAL = "de"
    APP_PORT = 80
    TEMPLATES_AUTO_RELOAD = True
    ENV = os.getenv("ENV") or "local development"
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True
    EXPIRES = 10800
    PERMANENT_SESSION_LIFETIME = 10800
    FOOTER = False

    # Basedir
    BASEDIR = basedir

    # Caching
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300

    # Secret key for sessions of flask users
    # change it before using in anything that could be attacked
    SECRET_KEY = os.getenv("SECRET_KEY") or "secretÜstkey6+5+655+65+5+65ß0656"

    # Database Url
    # Default is a file based sqlite3 databse in the static/databse folder
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User settings
    USER_ENABLE_EMAIL = False
    USER_ENABLE_USERNAME = True
    USER_ENABLE_CHANGE_USERNAME = True
    USER_ENABLE_CHANGE_PASSWORD = True
    USER_ENABLE_REGISTER = True

    # the retype password field is not supported but could be used with default
    # flask user settings
    USER_REQUIRE_RETYPE_PASSWORD = False
    USER_LOGIN_TEMPLATE = "flask_user/login.html"
    USER_REGISTER_TEMPLATE = "flask_user/register.html"

    # Content Settings pelican oriented
    MENUITEMS = (
    ("Map", "/map"),
    ("About", "/about")
    )


class development(Config):
    USER_ENABLE_REGISTER = True
    DEBUG = True
