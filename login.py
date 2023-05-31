from db import db, dbcursor
import time

def usercheck():
    
    dbcursor.execute('USE cars')
    name = input('Enter driver name to check email: ')
    query = "SELECT Email FROM drivers WHERE Name = %s"
    dbcursor.execute(query,(name,))
    result = dbcursor.fetchall()

    if result:    
        for name in result:
            email = name[0]
            if email:
                print('Email Found', email)
    else:
        time.sleep(1)
        print('User does not exist!!')  

usercheck()
