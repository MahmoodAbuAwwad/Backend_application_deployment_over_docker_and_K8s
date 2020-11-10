from flask import Flask

from flask_cors import CORS


app = Flask(__name__,template_folder="templates")
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})





app.config['SECRET_KEY']= 'Hello Python!'
from app import routes