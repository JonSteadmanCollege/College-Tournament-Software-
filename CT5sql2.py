from tkinter import *
from tkinter import ttk
from tkinter.ttk import * 

import sqlite3


root = Tk()
root.title('College Tournament Software by Jonathan Steadman!')
root.geometry('700x580')
root.configure(bg='pink')

root.resizable(0,0)

# connect to existing
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
    font=("Ubuntu", 24))
label.pack(ipadx=10, ipady=10)
#Create Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

#Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
#tree_scroll.config(command=my_tree.yview)

#Create Treeview
my_tree = ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

#Define the number of columns in Treeview
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
    global count
    my_tree.insert(parent='',index='end', iid=count, text="",values=(id_box.get(),fn_box.get(),ln_box.get(),t_box.get(),p_box.get()))
    count=count+1
    #Clear entry boxes
    id_box.delete(0, END)
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    t_box.delete(0,END)
    p_box.delete(0,END)

#Connect to existing
def Add_Record():
    conn = sqlite3.connect('CollTour.db')
    
    c=conn.cursor()
    #INSERT
    c.execute('INSERT INTO tblTour (ID, Forename, Last Name, Team, Points) VALUES(?,?,?,?,?)',(id,fn,ln,t,p))
    {
            'id':id_box.get(),
            'fn':fn_box.get(),
            'ln':ln_box.get(),
            't':t_box.get(),
            'p':p_box.get()
    }




# Submit Customer To Database
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
    
    c:execute("""UPDATE tblTour SET
        First_Name = :first,
        Last_Name = :last,
        Team = :team,
        Points = :point

        WHERE ID = :oid""",
        {
            'first': fn_box.get(),
            'last': ln_box.get(),
            'team': t_box.get(),
            'point': p_box.get(),
            'oid': id_box.get(),
            

        
        })




        
	# Commit the changes to the database
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
    selected = my_tree.focus()
    #save new data
    my_tree.item(selected, text="",values=(id_box.get(),fn_box.get(),ln_box.get(),t_box.get(),p_box.get()))
    #Clear entry boxes
    id_box.delete(0, END)
    fn_box.delete(0, END)
    ln_box.delete(0, END)
    t_box.delete(0,END)
    p_box.delete(0,END)

#Customize the buttons to make it look
st = Style()
st.configure('W.TButton', background='#FFC0CB', foreground='black', font=('Ubuntu', 22 ))
#Buttons
add_record = Button(root,text="Add new Record",style="W.TButton",command=add_record) #Ran into this issue but seems to be working now. :)
add_record.pack(padx=10,pady=5, side=LEFT)

select_record = Button(root,text="Select Record",style="W.TButton",command=select_record)
select_record.pack(padx=10,pady=5, side=LEFT)

update_record = Button(root,text="Update Record",style="W.TButton",command=update_record)
update_record.pack(padx=10,pady=5, side=LEFT)

#run to pull in data
query_database()

    
root.mainloop()
