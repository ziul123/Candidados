from flask import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("page.html")

@app.route("/candidatos")
def candidatos():
    return render_template("candidatos.html")
