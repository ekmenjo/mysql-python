from db import db, dbcursor

def create_vehicles():
    dbcursor = db.cursor()
    dbcursor.execute('USE cars')
    
    reg_number = input("Enter The Vehicle's Registration Number: ")
    owner = input("Enter driver's Name: ")
    model = input("Enter the Vehicle Type: ")
    color = input('Enter the color of the vehicle: ')
    chassis = input("Enter the vehicle Chasis Number: ")
    query = "INSERT INTO vehicles (reg_number, Owner, Model, Color, Chassis) VALUES (%s,%s,%s,%s,%s)"
    values = (reg_number, owner,model,color,chassis)
    dbcursor.execute(query, values)
    db.commit()
    dbcursor.close()
    

create_vehicles()

db.close()