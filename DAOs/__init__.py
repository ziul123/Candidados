import mysql.connector

# with open("login.txt", "r") as f:
# usr, passwd = f.readlines()
usr = 'admin'
passwd = '8sIL3h7iPTuw##lFNA8!'
cnx = mysql.connector.connect(user=usr, password=passwd,
        host="localhost", database="candidados")
cursor = cnx.cursor()
