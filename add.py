import tkinter as tk
import sqlite3
from tkinter import  ttk
from tkinter import  messagebox
win1=tk.Tk()
#adding a label
aLabel=ttk.Label(win1,  text="unum")
aLabel.grid(column=0,  row=2)
#adding another label
aLabel=ttk.Label(win1,  text="name")
aLabel.grid(column=0,  row=4)
#adding textbox 
unum=tk.StringVar()
unum=ttk.Entry(win1,  width=12,  textvariable=unum)
unum.grid(column=2,  row=2)
name=tk.StringVar()
name=ttk.Entry(win1, width=12,  textvariable=name)
name.grid(column=2,  row=4)
#function
def mf():
    unum1=unum.get()
    name1=name.get()
    
    conn=sqlite3.connect("Fruitdatabase.db")
    cur=conn.cursor()
    #cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    #rows=cur.fetchall()
    #for column in rows:
        #print(column)
    #cur.execute("CREATE TABLE FRUIT(unum INTEGER PRIMARY KEY, name TEXT UNIQUE);")
    cur.execute("INSERT INTO FRUIT(unum, name)VALUES(?, ?);", (unum1,  name1) )
    unum.bind('<Return>',  mf) 
    name.bind('<Return>',  mf)
    conn.commit()
    conn.close() 
    print(conn)
    #messagebox.showwarning("Warning",  "Fruit exists")
    messagebox.showinfo("Validation", "Added to database")
#adding button
action=ttk.Button(win1, text="OK",  command=mf)
action.grid(column=10, row=10)
win1.mainloop()
