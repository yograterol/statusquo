__author__ = 'yograterol'
from flask import Flask
from .views import site

app = Flask(__name__)
app.register_blueprint(site)
