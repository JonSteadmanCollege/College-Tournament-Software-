#Open source and Free to use this code as much as you want.
# No longer since 13/06/2022 getting updates. Sorry.
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox
import sqlite3
import tkinter as tk
#Please install the Ubuntu font
#Jonathan Steadman.
#Tested mostly on Windows and Linux Mint. :)
#This code might have a few bugs. 
root = Tk()
root.title('College Tournament Software by Jonathan Steadman!')
root.geometry('1080x790')
root.configure(bg='pink')

root.resizable(0,0)

# connect to existing Database. If no database it will create one automatically. :) 
conn = sqlite3.connect('CollTour.db')

#Create a cursor
c = conn.cursor()

def query_database():
#Connect to existing
    conn = sqlite3.connect('CollTour.db')
    #Create a cursor
    c=conn.cursor()

    c.execute("SELECT * FROM tblTour")
    records = c.fetchall()
    global count
    count=0
    for record in records:
        my_tree.insert(parent='',index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3], record[4]))
        count=count+1
    


    
    #commit changes
    conn.commit()
    conn.close
#Title lol
label = ttk.Label(
    root,
    text='College Tournament Software!',
    font=(("Ubuntu", 24,"bold", "underline")),
    background=("pink")
    )

label.pack(ipadx=10, ipady=10)
label = ttk.Label(
    root,
    text='The Database:',
    font=("Ubuntu", 20),
    background=("pink")
    )

label.pack(ipadx=10, ipady=10)
#Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=30)

#Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
#tree_scroll.config(command=my_tree.yview)

#Create Treeview
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)
label = ttk.Label(
    root,
    text='Enter some data:',
    font=("Ubuntu", 20),
    background=("pink")
)
label.pack(ipadx=10, ipady=10)
#Define the number of columns in Treeview
Style().configure("Treeview.Heading", font=(17))
my_tree['columns']=("ID","Forename","Surname","Team","Points")

#Format columns
my_tree.column("#0",width=5)
my_tree.column("ID",anchor=CENTER, width=100)
my_tree.column("Forename",anchor=W,width=140)
my_tree.column("Surname",anchor=W,width=100)
my_tree.column("Team",anchor=W,width=100)
my_tree.column("Points",anchor=W,width = 100)

#Create headings
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Forename",text="Forename",anchor=W)
my_tree.heading("Surname",text="Surname",anchor=W)
my_tree.heading("Team",text="Team",anchor=W)
my_tree.heading("Points",text="Points",anchor=W)

#global count
#count=0
#for record in data:
  # my_tree.insert(parent='',index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]))
   #count=count+1

#Pack to the screen
my_tree.pack(pady=20)

#Add labels frame
add_frame = Frame(root)
add_frame.pack(pady=20)

#Add Labels
idl=Label(add_frame,text="ID")
idl.grid(row=0,column=0)

fnl=Label(add_frame,text="Forename")
fnl.grid(row=0,column=1)

lnl=Label(add_frame,text="Last Name")
lnl.grid(row=0,column=2)

tl=Label(add_frame,text="Team")
tl.grid(row=0,column=3)

pl=Label(add_frame,text="Points")
pl.grid(row=0,column=4)


#Add text Entry boxes
global id_box
global fn_box
global ln_box
global t_box
global p_box

id_box= Entry(add_frame)
id_box.grid(row=1,column=0)

fn_box= Entry(add_frame)
fn_box.grid(row=1,column=1)

ln_box= Entry(add_frame)
ln_box.grid(row=1,column=2)

t_box= Entry(add_frame)
t_box.grid(row=1,column=3)

p_box= Entry(add_frame)
p_box.grid(row=1,column=4)





#Add Record
def add_record():
    my_tree.insert(parent='',index='end', text="",values=(id_box.get(),fn_box.get(),ln_box.get(),t_box.get(),p_box.get()))

    conn = sqlite3.connect('CollTour.db')
    c=conn.cursor()
    #INSERT
    idx=id_box.get()
    fn=fn_box.get()
    ln=ln_box.get()
    t=t_box.get()
    p=p_box.get()

    
    c.execute('INSERT INTO tblTour (ID,Forename,Surname,Team,Points) VALUES(?,?,?,?,?)',(idx,fn,ln,t,p))
    conn.commit()
    conn.close()
    #Clear entry boxes
    id_box.delete(0, END)
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    t_box.delete(0,END)
    p_box.delete(0,END)

def update_record():
    print("Hello")
    print(fn_box.get())
    print(id_box.get())
    print(ln_box.get())
    print(t_box.get())
    print(p_box.get())

    selected = my_tree.focus()
    #save new data
    my_tree.item(selected, text="",values=(id_box.get(),fn_box.get(),ln_box.get(),t_box.get(),p_box.get()))

    conn = sqlite3.connect('CollTour.db')
    #Create a cursor
   
    c=conn.cursor()
    
    c.execute("""UPDATE tblTour SET First_Name = :first, Last_Name = :last, Team = :team,Points = :point WHERE ID = :oid""",
        {
            'first': fn_box.get(),
            'last': ln_box.get(),
            'team': t_box.get(),
            'point': p_box.get(),
            'oid': id_box.get(),
            

        
        })
#Commit the changes to the database
    conn.commit()
    #c.execute("SELECT * FROM tblTour")
    print(c.fetchall())
    conn.close()
    #query_database()

#Select record
def select_record():
    #Clear entry boxes
    id_box.delete(0, END)
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    t_box.delete(0,END)
    p_box.delete(0,END)
    
    #get record number
    selected = my_tree.focus()
    #Get record number values
    values = my_tree.item(selected,'values')

    
    #Output to entry boxes
    id_box.insert(0,values[0])
    fn_box.insert(0,values[1])
    ln_box.insert(0,values[2])
    t_box.insert(0,values[3])
    p_box.insert(0,values[4])

#Save updates record
def update_record ():
    idx=id_box.get()
    fn=fn_box.get()
    ln=ln_box.get()
    t=t_box.get()
    p=p_box.get()
    selected = my_tree.focus()
    #save new data
    my_tree.item(selected, text="",values=(id_box.get(),fn_box.get(),ln_box.get(),t_box.get(),p_box.get()))

    #connect to the database :). The one it created or you got allready will be used. 
    conn = sqlite3.connect('CollTour.db')
    c=conn.cursor()
    c.execute('UPDATE tblTour SET Forename = ?, Surname = ?, Team = ?,Points=? WHERE ID=?',(fn,ln,t,p,idx))
    conn.commit()
    conn.close()



    #Clear entry boxes
    id_box.delete(0, END)
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    t_box.delete(0,END)
    p_box.delete(0,END)

def results_database():
    wx = Tk()
    wx.title("College Tournament Software by Jonathan Steadman - Results!")
    wx.geometry('700x480')
    wx.configure(bg='pink')
    wx.resizable(0,0)

    labelone =Label(wx,text="College Tournament Software - Results:",font=("Ubuntu", 24,"bold","underline"),background="pink")
    labelone.pack()
    labeltwo = ttk.Label(wx,text='Here is all your data that you got from the database:', font=("Ubuntu", 20,"bold"),background="pink")
    labeltwo.pack()
    #Create a new treeview frame. :)
    resultstree_frame = Frame(wx)
    resultstree_frame.pack(pady=40)
    conn = sqlite3.connect('CollTour.db')
        #Treeview Scrollbar
    myresults_scroll = Scrollbar(resultstree_frame)
    myresults_scroll.pack(side=RIGHT,fill=Y)
    #Create Treeview
    myresults_tree = ttk.Treeview(resultstree_frame,yscrollcommand=myresults_scroll.set)
    myresults_tree.pack()

    #Define the number of columns in treeview
    myresults_tree['columns']=("ID","Forename","Surname","Team","Points")
    #format headings.
    myresults_tree.column("#0",width=5)
    myresults_tree.column("ID",anchor=CENTER, width=100)
    myresults_tree.column("Forename",anchor=W,width=100)
    myresults_tree.column("Surname",anchor=W,width=100)
    myresults_tree.column("Team",anchor=W,width=100)
    myresults_tree.column("Points",anchor=W,width = 100)
#Create headings
    myresults_tree.heading("#0",text="",anchor=W)
    myresults_tree.heading("ID",text="ID",anchor=CENTER)
    myresults_tree.heading("Forename",text="Forename",anchor=W)
    myresults_tree.heading("Surname",text="Surname",anchor=W)
    myresults_tree.heading("Team",text="Team",anchor=W)
    myresults_tree.heading("Points",text="Points",anchor=W)
    #connect a cusor
    c=conn.cursor()
    c.execute("SELECT * FROM tblTour")
    records = c.fetchall()
    global count
    count=0
    for record in records:
        myresults_tree.insert(parent='',index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4]))
        count=count+1
    conn.commit()
    conn.close

    
#Customize the buttons to make it look
#Only really works in Linux and FreeBSD. This software is compiled to run on Linux and Windows. Windows cant have the buttons customized.
st = Style()
st.configure('W.TButton', background='purple', foreground='black', font=('Ubuntu', 22,"bold" ))
#Buttons
label = ttk.Label(
    root,
    text='Click on those buttons to do an action with the new data or the data you selected:',
    font=("Ubuntu", 20,"bold"),
    background=("pink")
)
label.pack(ipadx=10, ipady=10)
add_record = Button(root,text="Add new Record",style="W.TButton",command=add_record)
add_record.pack(padx=10,pady=5, side=LEFT)

select_record = Button(root,text="Select Record",style="W.TButton",command=select_record)
select_record.pack(padx=10,pady=5, side=LEFT)

update_record = Button(root,text="Update Record",style="W.TButton",command=update_record)
update_record.pack(padx=10,pady=5, side=LEFT)
results_database = Button(root,text="Results", style="W.TButton",command=results_database)
results_database.pack(padx=10, pady=5, side=LEFT)
query_database()
#When you press on the X buttion then the GUI window will show up a popup.
#Yes = Exit the software.
#No = Stay in the software. 
def on_closing():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Confirm to exit the Software:")


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the software:")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this software?")

    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Yes",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.quit)

    B2 = tk.Button(root, text="No",font=("ubuntu",28),bg="pink",activebackground='#23d18b', command = root.destroy)
    B1.pack(side=tkinter.LEFT, anchor=CENTER)
    B2.pack(side=tkinter.RIGHT, anchor=CENTER)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
