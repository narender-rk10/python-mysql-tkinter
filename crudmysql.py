import tkinter as tk 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox 

connection = mysql.connector.connect(host="localhost",
                            user="root",
                            port=3308,
                            password="yourpassword",
                            database="py11")

def create():  
    name = a1.get()  
    uid = b1.get()
    mobile = c1.get()
    email = d1.get()
    address = e1.get()
    mySql_insert_query ="insert into student values(%s, %s, %s, %s, %s)"
    val = (name,uid,mobile,email,address)  
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query,val)
    connection.commit()
    messagebox.showinfo("MESSAGE", "Record inserted successfully into student table") 
    cursor.close()

def get_details():  
    sql_select_Query = "SELECT * FROM Student WHERE uid LIKE '"+au1.get()+"'"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for row in records:
        tk.Label(root ,text = "UPDATE DETAILS FOR UID: "+au1.get() ).grid(row = 13,column = 0,columnspan=2)
        ag1 = tk.Label(root ,text = "NAME: ").grid(row = 14,column = 0)
        bg1= tk.Label(root ,text = "MOBILE").grid(row = 15,column = 0)
        cg1 = tk.Label(root ,text = "EMAIL").grid(row = 16,column = 0)
        dg1 = tk.Label(root ,text = "ADDRESS").grid(row = 17,column = 0)

        a1g1 = tk.Entry(root)
        a1g1.grid(row = 14,column = 1)
        a1g1.insert(0,""+row[0])
        b1g1 = tk.Entry(root)
        b1g1.grid(row = 15,column = 1)
        b1g1.insert(0,""+row[2])
        c1g1 = tk.Entry(root)
        c1g1.grid(row = 16,column = 1)
        c1g1.insert(0,""+row[3])
        d1g1 = tk.Entry(root)
        d1g1.grid(row = 17,column = 1)
        d1g1.insert(0,""+row[4])

    btnU2 = ttk.Button(root ,text="UPDATE",command=update).grid(row=18,column=0,columnspan=2,sticky='we')

def update():  
    name = a1g1.get()  
    uid = au1.get()
    mobile = b1g1.get()
    email = c1g1.get()
    address = d1g1.get()
    update_query = """ UPDATE student
                    SET name = %s,
                    mobile = %s,
                    email = %s,
                    address = %s
                    WHERE uid = %s """
    val = (name,mobile,email,address,uid)  
    cursor = connection.cursor()
    cursor.execute(update_query,val)
    connection.commit()
    messagebox.showinfo("MESSAGE", "Record updated successfully into student table") 
    cursor.close()
    
def delete():
    uid = b1.get()
    del_query ="delete from student WHERE uid LIKE '"+ad1.get()+"'"
    cursor = connection.cursor()
    cursor.execute(del_query)
    connection.commit()
    messagebox.showinfo("MESSAGE", "RECORD DELETED SUCCESSFULLY!") 
    cursor.close()
   
  

root = tk.Tk() 
root.title("CRUD MYSQL APP")

a1g1 = tk.Entry(root)
b1g1 = tk.Entry(root)
c1g1 = tk.Entry(root)
d1g1 = tk.Entry(root)
tk.Label(root ,text = "INSERT INTO DATABASE: ").grid(row = 0,column = 0,columnspan=2)
a = tk.Label(root ,text = "NAME: ").grid(row = 1,column = 0)
b = tk.Label(root ,text = "UID: ").grid(row = 2,column = 0)
c = tk.Label(root ,text = "MOBILE").grid(row = 3,column = 0)
d = tk.Label(root ,text = "EMAIL").grid(row = 4,column = 0)
e = tk.Label(root ,text = "ADDRESS").grid(row = 5,column = 0)

a1 = tk.Entry(root)
a1.grid(row = 1,column = 1)
b1 = tk.Entry(root)
b1.grid(row = 2,column = 1)
c1 = tk.Entry(root)
c1.grid(row = 3,column = 1)
d1 = tk.Entry(root)
d1.grid(row = 4,column = 1)
e1 = tk.Entry(root)
e1.grid(row = 5,column = 1)

btnC = ttk.Button(root ,text="INSERT",command=create).grid(row=6,column=0,columnspan=2,sticky='we')

tk.Label(root ,text = "DELETE INTO DATABASE: ").grid(row = 7,column = 0,columnspan=2)
ad = tk.Label(root ,text = "UID: ").grid(row = 8,column = 0)
ad1 = tk.Entry(root)
ad1.grid(row = 8,column = 1)

btnD = ttk.Button(root ,text="DELETE",command=delete).grid(row=9,column=0,columnspan=2,sticky='we')

tk.Label(root ,text = "UPDATE INTO DATABASE: ").grid(row = 10,column = 0,columnspan=2)
au = tk.Label(root ,text = "UID: ").grid(row = 11,column = 0)
au1 = tk.Entry(root)
au1.grid(row = 11,column = 1)

btnU1 = ttk.Button(root ,text="GET DETAILS",command=get_details).grid(row=12,column=0,columnspan=2,sticky='we')

root.mainloop()

root.mainloop() 
