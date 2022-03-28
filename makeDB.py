from tkinter import *
from tkinter import ttk
import sqlite3


#Create a db or connect to existing
conn = sqlite3.connect('CollTour.db')

#Create a cursor
c = conn.cursor()

#Create a table
c.execute("CREATE TABLE tblTour(ID integer,Forename text,Surname text,Team text,Points integer)")

c.execute("INSERT INTO tblTour VALUES ('1','Gary','Jones','Blue',12)")

c.execute("SELECT * FROM tblTour")

#output database table contents to screenviewer
print(c.fetchall())
#commit changes
conn.commit()

#close database
conn.close()  



