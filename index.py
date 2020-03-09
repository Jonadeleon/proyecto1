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

@app.route('/clases', methods=['GET', 'POST'])
def clases():
    clases = db.clases.find().sort("name", 1)
    return render_template('clases.html', clases=clases)

@app.route('/razas')
def razas():
    razas = db.razas.find()
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

@app.route('/subida')
def subida():
    name = request.args['name']
    description = request.args['descripcion']
    stat_bonus = request.args['stat_bonus']
    dice_pv = request.args['dados_pv']
    dice_pm = request.args['dados_pm']
    licencias = request.args['licencias']
    hab1 = request.args['hab1']

    db.clases.insert_one(
        {
            "name": name,
            "descripcion": description,
            "stat_bonus": stat_bonus,
            "dice_pv": dice_pv,
            "dice_pm": dice_pm,
            "licencias": licencias,
            "hab1": hab1
        }
    )
    return redirect('/clases')

# @app.route('/delete', methods=['POST'])
# def delete_clase():
#     delete = db.clases.delete_many({"'name':'w52345'"})
#
#     return redirect('/clases', delete=delete)

if __name__ == "__main__":
    app.run(debug=True)