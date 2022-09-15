from flask import *

@app.route("/lista_politico", methods = ['GET', 'DELETE', 'PUT', 'POST'])
def crud_cliente():
    cursor = cnx.connection.cursor()       

    if request.method == 'DELETE':
        data = request.get_json()
        ClienteDAO().delete(cursor, data['cpf'])
        cnx.connection.commit()
        return '304'

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        cliente = Cliente(data['p0'], data['p1'], data['p2'], data['p3'], None, None)

        c = ClienteDAO().find_by_id(cursor, cliente.cpf)
        cliente.fk_endereco = c.fk_endereco
        cliente.fk_login = c.fk_login

        ClienteDAO().update(cursor, cliente, cliente.cpf)

        cnx.connection.commit()
        return '201'
    

    clientes = ClienteDAO().find_all(cursor)

    return render_template("crud_cliente.html", clientes = clientes)

