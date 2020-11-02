from flask import Flask
from flask import Blueprint
app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY']= 'Hello Python!'
bp = Blueprint('api', __name__)
from app import routes