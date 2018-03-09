import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
win2=tk.Tk()
#label
aLabel=ttk.Label(win2,  text="unum")
aLabel.grid(column=0, row=2)
#textbox
unum=tk.StringVar()
unum=ttk.Entry(win2,  width=12,  textvariable=unum)
unum.grid(column=2,  row=2)
#function
def ef():
    unum1=unum.get()
    #name1=name.get()
    conn=sqlite3.connect("Fruitdatabase.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM FRUIT WHERE unum=?", (unum1))
    conn.commit()
    conn.close()
    print(conn)
    unum.bind('<Return>', ef)
    messagebox.showinfo("Confirmation", "Value deleted"  )
    #name.bind('<Return>', ef)
#button
action=ttk.Button(win2,  text="Delete",  command=ef)
action.grid(column=12,  row=12)
win2.mainloop()
