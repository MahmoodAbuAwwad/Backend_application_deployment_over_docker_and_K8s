from app import app
import sqlite3
import json

@app.route('/')
@app.route('/add')
def add():
    conn = sqlite3.connect('todoss.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS todo_db (todo text);")
    c.execute("INSERT INTO todo_db(todo) VALUES(?)",('Hello',))
    conn.commit()
    conn.close()
    return 'x'


@app.route('/fetch')
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