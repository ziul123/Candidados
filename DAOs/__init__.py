import mysql.connector

with open("../login.txt", "r") as f:
    usr, passwd = f.readlines()
    cnx = mysql.connector.connect(user=usr, password=passwd,
            host="localhost", database="candidados")
    cursor = cnx.cursor
