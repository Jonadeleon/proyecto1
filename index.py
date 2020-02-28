from flask import Flask, render_template, request, redirect
# traemos dependecia de pymongo para la conexion a la base de datos
from pymongo import MongoClient

app = Flask(__name__)
# ponemos la conexion y la base de datos MUY IMPORTANTE TENER VERSION DE PYTHON ACTUALIZADO Y CONFIGURADO EN PYCHARM O NO FUNCIONARÁ EL ENLACE
client = MongoClient("mongodb+srv://karmaster:acm1ptcactm@cluster0-gsee8.mongodb.net/test?retryWrites=true&w=majority")
db = client.Rol_test

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/clases', methods=['GET'])
def clases():
    clases = db.clases.find().limit(10)
    return render_template('clases.html', clases=clases)

@app.route('/razas')
def razas():
    razas = db.razas.find().limit(10)
    return render_template('razas.html', razas=razas)

@app.route('/armaduras')
def armaduras():
    return render_template('armaduras.html')

@app.route('/armas')
def armas():
    return render_template('armas.html')

@app.route('/items')
def items():
    return render_template('items.html')

@app.route('/update')
def update():
    if request.method == 'POST':
        name = request.args['name']
        stat = request.args['stat']
        hab1 = request.args['hab1']
        flash(str(name))
        flash(str(stat))
        flash(str(hab1))
    return render_template('update.html')

@app.route('/subida')
def subida():
    name = request.args['name']
    stat = request.args['stat']
    hab1 = request.args['hab1']

    db.clases.insert_one(
        {
            "name": name,
            "stat": stat,
            "hab1":hab1
        }
    )
    return redirect('/update')

if __name__ == "__main__":
    app.run(debug=True)