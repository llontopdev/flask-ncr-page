from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='locales_kraken'

mysql = MySQL(app)

@app.route('/')
def index():
  return "Flask NCR Page"

@app.route('/stores')
def stores():
  return "Locales"

@app.route('/stores/add')
def add_store():  
  return render_template('add_store.html')

@app.route('/stores/add', methods=['POST'])
def add():
  if request.method == 'POST':
    num_local= request.form['num_local']
    nombre_local=request.form['nombre_local']
    formato = request.form['formato']
    telefono = request.form['telefono']
    ciudad = request.form['ciudad']
    direccion = request.form['direccion']
    
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO locales (numero, nombre, telefono, direccion, ciudad, formato) VALUES(%s,%s,%s,%s,%s,%s)', (num_local,nombre_local,telefono,direccion,ciudad,formato))
    mysql.connection.commit()
    
    return 'registro exitoso'
  

@app.route('/stores/edit')
def edit_store():
  return 'editar local'

@app.route('/store/delete')
def delete_store():
  return 'eliminar Local'



if __name__ == '__main__':
  app.run(port=3000, debug=True)