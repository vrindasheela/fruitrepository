import tkinter as tk
from tkinter import ttk
import sqlite3
win3=tk.Tk()
#Label
aLabel=ttk.Label(win3,  text="unum")
aLabel.grid(column=0, row=0)
#textbox
unum=tk.StringVar()
unum=ttk.Entry(win3, width=12,  textvariable=unum)
unum.grid(column=2,  row=0)
#function gf
def gf():
    unum1=unum.get()
    #name1=name.get()
    conn=sqlite3.connect("Fruitdatabase.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM FRUIT WHERE unum = ?", (unum1))
    for row in cur.fetchall():
        s=row
    unum.bind('<Return>',  gf)
    #name.bind('<Return>',  gf)
    conn.commit()
    conn.close()
    print(conn)
    aLabel=ttk.Label(win3,  text=s)
    aLabel.grid(column=4, row=4)
#button
action=ttk.Button(win3,  text="View",  command=gf)
action.grid(column=12,  row=12)
win3.mainloop()
