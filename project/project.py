from flask import Flask, redirect, render_template, request
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(host='localhost', user='root', password='1234', charset='utf8', database='programming')

db = get_connection()
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS crud_information (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
''')
db.commit()
db.close()

def get_info(): 
    db = get_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM crud_information;')
    data = cursor.fetchall()
    db.close()
    return data

def add():
    info = get_info()
    add_info = ''
    for i in info:
        add_info += f"<h2><a href='/read/{i['id']}/'>{i['id']}-{i['title']}</a></h2><br>"
    return add_info

@app.route('/')
def main():
    return render_template('index.html', add_info=add())

@app.route('/read/<int:id>/')
def readpage(id):
    info = get_info()
    for i in info:
        if id == i['id']:
            return render_template('read.html', title=i['title'], description=i['description'], id=i['id'])

@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db = get_connection()
        cursor = db.cursor()
        cursor.execute('INSERT INTO crud_information (title, description) VALUES (%s, %s)', (title, description))
        db.commit()
        db.close()
        return redirect('/')

@app.route('/delete/<int:id>/')
def delete(id):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute(f'DELETE FROM crud_information WHERE id = {id};')
    db.commit()
    db.close()
    return redirect('/')

@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    info = get_info()
    for i in info:
        if id == i['id']:
            title = i['title']
            description = i['description']
    if request.method == 'GET':
        return render_template('update.html', id=id, title=title, description=description)
    elif request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(f'UPDATE crud_information SET title="{title}",description="{description}" WHERE id="{id}";')
        db.commit()
        db.close()
        return redirect('/')

@app.route('/allsearch/', methods=['POST', 'GET'])
def allsearch():
    sobject = request.form['object']
    db = get_connection()
    cursor = db.cursor()
    cursor.execute('SELECT title, id, description FROM crud_information')
    info = cursor.fetchall()
    value = ""
    for i in info:
        if sobject in i['title'] or sobject in i['description']:
            value += f"<h2><a href='/read/{i['id']}/'>{i['id']}-{i['title']}</a></h2><br>"
    db.close()
    return render_template('search.html', add_info=value)

@app.route('/titlesearch/', methods=['GET', 'POST'])
def titlesearch():
    sobject = request.form['object']
    db = get_connection()
    cursor = db.cursor()
    cursor.execute('SELECT title, id FROM crud_information')
    info = cursor.fetchall()
    value = ""
    for i in info:
        if sobject in i['title']:
            value += f"<h2><a href='/read/{i['id']}/'>{i['id']}-{i['title']}</a></h2><br>"
    db.close()
    return render_template('search.html', add_info=value)

@app.route('/descriptionsearch/', methods=['GET', 'POST'])
def discriptionsearch():
    sobject = request.form['object']
    db = get_connection()
    cursor = db.cursor()
    cursor.execute('SELECT title, id, description FROM crud_information')
    info = cursor.fetchall()
    value = ""
    for i in info:
        if sobject in i['description']:
            value += f"<h2><a href='/read/{i['id']}/'>{i['id']}-{i['title']}</a></h2><br>"
    db.close()
    return render_template('search.html', add_info=value)

app.run(port=7000, debug=True)
