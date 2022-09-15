from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("base.html")

@app.route("/homepoliticos")
def homepoliticos():
    return render_template("lista_politico.html")

@app.route("/homepartido")
def homepartido():
    return render_template("lista_partido.html")
