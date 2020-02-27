from flask import Flask, render_template, request, flash, redirect
# traemos dependecia de pymongo para la conexion a la base de datos
from pymongo import MongoClient

app = Flask(__name__)
# ponemos la conexion y la base de datos
client = MongoClient("mongodb+srv://karmaster:acm1ptcactm@cluster0-gsee8.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/clases')
def clases():
    return render_template('clases.html')

@app.route('/razas')
def razas():
    return render_template('razas.html')

@app.route('/armaduras')
def armaduras():
    return render_template('armaduras.html')

@app.route('/armas')
def armas():
    return render_template('armas.html')

@app.route('/items')
def items():
    return render_template('items.html')

if __name__ == "__main__":
    app.run(debug=True)