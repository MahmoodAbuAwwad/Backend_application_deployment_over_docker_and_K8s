from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__,template_folder="templates")
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.config['MYSQL_HOST'] = '192.168.204.226'
app.config['MYSQL_PORT'] = 6604
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask'
app.config['MYSQL_DB'] = 'backend'
app.config['MYSQL_ROOT_PASSWORD'] = 'flask'
mysql = MySQL(app)


app.config['SECRET_KEY']= 'Hello Python!'
from app import routes