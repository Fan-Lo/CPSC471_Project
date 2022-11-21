import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="student",
    passwd="ensf",
    database="471"
)

mycursor = db.cursor()

