from flask import *
import DAOs

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("base.html")

@app.route("/politicos")
def homepoliticos():
    return render_template("politicos.html")

@app.route("/politicos", methods = ['GET', 'DELETE', 'PUT', 'POST'])
def crud_cliente():

    cursor = DAOs.cursor

    # if request.method == 'DELETE':
    #     data = request.get_json()
    #     DAO().delete(cursor, data['cpf'])
    #     cnx.connection.commit()
    #     return '304'

    # if request.method == 'POST':
    #     data = request.get_json()
    #     print(data)
    #     cliente = Cliente(data['p0'], data['p1'], data['p2'], data['p3'], None, None)

    #     c = ClienteDAO().find_by_id(cursor, cliente.cpf)
    #     cliente.fk_endereco = c.fk_endereco
    #     cliente.fk_login = c.fk_login

    #     ClienteDAO().update(cursor, cliente, cliente.cpf)

    #     cnx.connection.commit()
    #     return '201'

    politicos = DAOs.PoliticosDAO().getall(cursor)

    print(politicos)

    return render_template("crud_cliente.html", politicos = politicos)

@app.route("/candidatos", methods = ['GET', 'DELETE', 'PUT', 'POST'])
def crud_cliente():

    cursor = DAOs.cursor

    candidatos = DAOs.PoliticosDAO().getCandidatos(cursor)

    return render_template("politicos.html", politicos = candidatos)