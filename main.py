from tkinter import *
from db import db, dbcursor

def search():
    global name

    driver_detail = name.get()
    dbcursor.execute('USE cars')
    query = "SELECT id,Name,Email from drivers WHERE id =%s"
    dbcursor.execute(query,(driver_detail,))
    result = dbcursor.fetchall()

    if result:
        for driver_detail in result:
            id1 = driver_detail[0]
            name1 = driver_detail[1]
            email1 = driver_detail[2]
            lbl_name.config(text=name1)
            lbl_email.config(text=email1)
            
            # print(f'Driver detail found {name1} with email {email1}')


window = Tk()
window.title('Car Rescue 254')
Label(window, bg='Black',height=4).pack(fill=X)
Label(window, text="CAR RESCUE DATABASE",bg='Yellow', fg='Black', font='Ariel 12 bold').pack(fill=X)

New_driver_frame = Frame(window, height=800, width=210, bg='lightgreen')
New_driver_frame.pack(side=LEFT)

driver_lbl = Label(New_driver_frame,text="Driver ID: ",font='calibri 15 bold')
driver_lbl.place(x=10, y= 50)

name = StringVar()
driver_entry = Entry(New_driver_frame, textvariable=name, font='calibri 10 bold', relief='ridge')
driver_entry.place(x= 10, y= 100)

search_bttn = Button(New_driver_frame, text="Search Database", relief='raised', font='calibri 12 bold', command=search)
search_bttn.place(x=10, y=150)

Display_frame = Frame(window, bg='lightblue' ,height=800, width=900)
Display_frame.pack(side=LEFT)

name_label = Label(Display_frame, text='Name:', font="calibri 10 bold")
name_label.place(x=20, y= 50)

lbl_name = Label(Display_frame, fg='black', text="", font='calibri 10 bold', width=20)
lbl_name.place(x=20, y=100)

email_label = Label(Display_frame, text='Email address', font='calibri 10 bold')
email_label.place(x=200, y= 50)

lbl_email = Label(Display_frame, fg='black', text="", font='calibri 10 bold', width=20)
lbl_email.place(x=200, y=100)

window.mainloop()
