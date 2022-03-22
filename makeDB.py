from tkinter import *
from tkinter import ttk
import sqlite3
#Shows all peoples data in the database.
records = [("1","Jonathan", "Steadman", "Pink", 12),
             ("6","Billy", "Jones", "Team", 12)
           ]

#Create a db or connect to existing
conn = sqlite3.connect('CollTour.db')

#Create a cursor
c = conn.cursor()



         

#Create a table
c.execute("CREATE TABLE tblTour(ID text,First_Name text,Last_Name text,Team text, Points integer)")


#c.execute("INSERT INTO tblTour VALUES ('1','Gary','Jones','Blue',5)")
c.executemany("INSERT INTO tblTour VALUES(?,?,?,?,?,?);", records);

c.execute("SELECT * FROM tblTour")

#output database table contents to screenviewer
print(c.fetchall())
#commit changes
conn.commit()


conn.close()  



