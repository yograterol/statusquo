__author__ = 'yograterol'
from flask.blueprints import Blueprint
from flask import render_template

site = Blueprint('site', __name__, static_folder='static', template_folder='templates')


@site.route('/', methods=['GET', ])
@site.route('/home/', methods=['GET', ])
@site.route('/index/', methods=['GET', ])
def index():
    return render_template('index.html')