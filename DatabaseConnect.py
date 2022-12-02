import mysql.connector 

class DatabaseConnect:

    def __init__(self):
        # p = input("Enter Database Password: ")
        # u = input("Enter Database Username: ")

        try:
            self.connection = mysql.connector.connect(user ='root', password = 'ajoke0306', host='127.0.0.1', database='471')

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

    def getTable(self, s, table):
        mycursor = self.connection.cursor()

        mycursor.execute(f"SELECT {s} FROM {table}")

        myresult = mycursor.fetchall()
        return myresult

    def performQuery(self, query):
        mycursor = self.connection.cursor()

        mycursor.execute(query)

        myresult = mycursor.fetchall()
        return myresult

    def insert(self, query):
        mycursor = self.connection.cursor()

        mycursor.execute(query)
        self.connection.commit()
        #return mycursor.rowcount, 'record inserted'

    def close(self):
        if self.connection.is_connected():
            self.connection.close()

if __name__ == "__main__":
    database = DatabaseConnect()
    database.close()
