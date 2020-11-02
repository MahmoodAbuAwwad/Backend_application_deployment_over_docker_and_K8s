from app import app
import sqlite3
import json
from flask_cors import CORS
from flask import request


CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})




@app.route('/api/v1/add/<name>',methods=['GET', 'POST'])
def add(name):

    if request.method == 'POST':
        name=request.data
        conn = sqlite3.connect('todoss.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
        c.execute("INSERT INTO todo_db(todo) VALUES(?);",(name,))
        conn.commit()
        conn.close()
    return 'Ok'



@app.route('/api/v1/fetch', methods=['GET', 'POST'])
def fetch():
    conn = sqlite3.connect('todoss.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
    
    c.execute("SELECT * FROM todo_db;")
    data = c.fetchall()
    conn.commit()
    conn.close()
    # print(data)
    
    list_of_data =[]
    for row in data:
        list_of_data.append(row[0])
        
    # print(list_of_data)
    y = json.dumps(list_of_data)
    return y

