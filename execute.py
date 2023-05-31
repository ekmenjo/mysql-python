from db import db, dbcursor

def execute():
    dbcursor = db.cursor()
    dbcursor.execute('USE cars')
    dbcursor.execute("SELECT * FROM drivers")
    result = dbcursor.fetchall()

    for row in result:
        print(row)

print(execute())