from db import db, dbcursor

def create_drivers():
    dbcursor = db.cursor()
    dbcursor.execute("USE cars")

    
    Name = input("Enter driver's Names: ")
    Email = input("Enter driver's email address: ")
    query = "INSERT INTO drivers (Name, Email) VALUES (%s,%s)"
    values = (Name, Email)
    dbcursor.execute(query, values)
    db.commit()
    print('User successfully created!!')
   
    # print('unable to add name to database')
    dbcursor.close()


create_drivers()

db.close()