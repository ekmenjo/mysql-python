import mysql.connector as mysql

db = mysql.connect(host='localhost',
                user='root',
                password='Kaptuiya2023'
                ) 
dbcursor = db.cursor()

# def connect_db():
#     dbcursor = db.cursor()
#     dbcursor.execute('CREATE DATABASE cars')
#     dbcursor.close()

def create_tables():
    dbcursor = db.cursor()
    dbcursor.execute('USE cars')
    query = 'CREATE TABLE vehicles(id INT AUTO_INCREMENT PRIMARY KEY, reg_number VARCHAR(255), Owner VARCHAR(255), Model VARCHAR(255), Color VARCHAR(255), Chassis VARCHAR(255) UNIQUE)'
    # dbcursor.execute('CREATE TABLE drivers(id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255))' )
    dbcursor.execute(query)
    dbcursor.close()

# connect_db() - Do not activate unless creating a new Database
#create_tables() Do not activate unless creating new tables

