from app import app
from flask_cors import CORS
from flask import request
from flask import Flask
from flaskext.mysql import MySQL
import os, json



CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
mysql = MySQL()

app.config['MYSQL_HOST'] = os.environ['HOST']
app.config['MYSQL_PORT'] = os.environ['PORT']
app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask'
app.config['MYSQL_DB'] = 'backend'
app.config['MYSQL_ROOT_PASSWORD'] = 'flask'
mysql.init_app(app)


@app.route('/api/v1/add/<name>',methods=['GET', 'POST'])
def add(name):

    if request.method == 'POST':
        name=request.data

        # conn = sqlite3.connect('todoss.db')
        # c = conn.cursor()

        cur = mysql.connect().cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
        cur.execute("INSERT INTO todo_db(todo) VALUES(?);",(name,))
        mysql.connection.commit()
        cur.close()
       
         # conn.commit()
        # conn.close()
    return 'Ok'



@app.route('/api/v1/fetch', methods=['GET', 'POST'])
def fetch():
    # conn = sqlite3.connect('todoss.db')
    # c = conn.cursor()
    # c.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
    c = mysql.connect().cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
    c.execute("SELECT * FROM todo_db;")
    data = c.fetchall()
    mysql.connection.commit()
    c.close()
          
    # conn.commit()
    # conn.close()
    # print(data)
    
    list_of_data =[]
    for row in data:
        list_of_data.append(row[0])
        
    y = json.dumps(list_of_data)
    return y

