import mysql.connector

db = mysql.connector.connect(
    user="student",
    password='ensf',
    host='localhost',
    database='471',
    auth_plugin='mysql_native_password')

db.close()

