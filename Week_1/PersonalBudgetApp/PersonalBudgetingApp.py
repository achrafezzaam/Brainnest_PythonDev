''' The goal of this project is to create a personal budgeting app that allows users to track their income and expenses, set budget goals, and view their spending habits.



Here are the steps you can take to create this project:



    Use the sqlite3 library to create a database to store the user's budget data.



    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons, text boxes and tables.



    Use the pandas library to manipulate the data and generate charts and tables to visualize the user's budget data.



    Use the datetime library to store and display the date and time of the transactions. '''

from os import getcwd
from os.path import join
from tkinter import *
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import datetime

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS expense_record (id integer primary key, tag_name text, amount float, entry_date text)")
        self.conn.commit()

    def insertRecord(self, tag_name, amount, entry_date):
        self.cur.execute("INSERT INTO expense_record VALUES (NULL, ?, ?, ?)",
                        (tag_name, amount, entry_date.strftime("%d %B %Y - %H:%M")))
        self.conn.commit()

    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE id=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, tag_name, amount,rwid):
        self.cur.execute("UPDATE expense_record SET tag_name = ?, amount = ? WHERE id = ?",
                        (tag_name, amount, rwid))
        self.conn.commit()
    
    def showTable(self,root):
        expenses = pd.read_sql_query("SELECT * FROM expense_record",self.conn)
        amounts_list = []
        for elem in expenses.index:
            if (elem-1)<0:
                amounts_list.append(expenses["amount"][elem])
            else:
                value = expenses["amount"][elem] + amounts_list[elem-1]
                amounts_list.append(value)
        df = pd.DataFrame(amounts_list,columns=['Budget'])
        fig1 = df.plot().get_figure()
        my_graph = Toplevel(root)
        my_graph.title("My Budget")
        plot1 = FigureCanvasTkAgg(fig1, my_graph)
        plot1.get_tk_widget().grid(row=0,column=0)
    
    def showRecords(self, root):
        df = pd.read_sql("SELECT * FROM expense_record",self.conn)
        expenses_table = Toplevel(root)
        expenses_table.title("My expenses logs")
        my_table = ttk.Treeview(expenses_table)
        my_table.grid(row=1,column=1,padx=20,pady=20)
        my_table.tag_configure('pass', background='#A7D94A')
        my_table.tag_configure('fail', background='#D94F34')
        vs = ttk.Scrollbar(expenses_table,orient="vertical", command=my_table.yview)
        my_table.configure(yscrollcommand=vs.set)
        vs.grid(row=1,column=2,sticky='ns') 
        my_table['columns'] = ('1','2','3','4')
        my_table['show'] = 'headings'
        my_table.column("1", anchor ='c')
        my_table.column("2", anchor ='c')
        my_table.column("3", anchor ='c')
        my_table.column("4", anchor ='c')
        my_table.heading("1", text ="Id")
        my_table.heading("2", text ="Tag name")
        my_table.heading("3", text ="Amount")
        my_table.heading("4", text ="Date")
        for elem in df.index:
            my_tag='pass' if df["amount"][elem] >= 0 else 'fail'
            my_table.insert("",'end',values=(df["id"][elem], df["tag_name"][elem],\
                df["amount"][elem], df["entry_date"][elem]), tags=(my_tag))
        Button(expenses_table,text="Update Record", width=14, command=lambda:self.changeRecord(expenses_table,root)).grid(column=1,row=0,padx=20, pady=10)
        
    def changeRecord(self, parent, root):
        frm3 = Toplevel(root, padx=10, pady=10)
        frm3.title("Record update")
        def changeRecord():
            tag_name = tag_field.get()
            amount = amount_field.get()
            row = row_field.get()
            self.updateRecord(tag_name,amount,row)
            parent.destroy()
            self.showRecords(root)
            frm3.destroy()
        def deleteRecord():
            row = row_field.get()
            self.removeRecord(row)
            parent.destroy()
            self.showRecords(root)
            frm3.destroy()
        tag_field = StringVar()
        Label(frm3,text="Update tag name",anchor='w',width=20).grid(column=0,row=0)
        Entry(frm3,textvariable=tag_field).grid(column=1,row=0,padx=4)

        Label(frm3,text="Update amount",anchor='w',width=20).grid(column=0,row=1)
        amount_field = DoubleVar()
        Entry(frm3,textvariable=amount_field).grid(column=1,row=1,padx=4)

        Label(frm3,text="Enter record id",anchor='w',width=20).grid(column=0,row=2)
        row_field = IntVar()
        Entry(frm3,textvariable=row_field).grid(column=1,row=2,padx=4)

        Button(frm3,text="Update Record", width=14, command=changeRecord).grid(column=2,row=1,padx=20)
        Button(frm3,text="Delete Record", width=14, command=deleteRecord).grid(column=2,row=2,padx=20)

    def __del__(self):
        self.conn.close()

class BudgetApp:
    def __init__(self,db):
        self.db = db
        self.root = Tk()
        self.root.title("Personal Budgeting")
        self.frm1 = ttk.Frame(self.root, padding=10)
        self.frm1.grid()
        self.frm2 = ttk.Frame(self.root, padding=10)
        self.frm2.grid()
        self.BuildGUI()
    
    def BuildGUI(self):
        def addRecord():
            tag_name = tag_field.get()
            amount = amount_field.get()
            date = datetime.datetime.now()
            self.db.insertRecord(tag_name,amount,date)
            tag_field.set("")
            amount_field.set("")
        tag_field = StringVar()
        Label(self.frm1,text="Enter tag name",anchor='w',width=20).grid(column=0,row=0)
        Entry(self.frm1,textvariable=tag_field).grid(column=1,row=0,padx=4)

        Label(self.frm1,text="Enter amount",anchor='w',width=20).grid(column=0,row=1)
        amount_field = DoubleVar()
        Entry(self.frm1,textvariable=amount_field).grid(column=1,row=1,padx=4)

        Button(self.frm1,text="Add Record", command=addRecord, width=14).grid(column=2,row=0,padx=20)
        Button(self.frm1,text="View Records", command=lambda:self.db.showRecords(self.root), width=14).grid(column=2,row=1,padx=20)
        Button(self.frm1,text="Show plot", command=lambda:self.db.showTable(self.root), width=14).grid(column=2,row=3,pady=10)
        Button(self.frm1, text="Quit", command=self.root.destroy).grid(column=2,row=4,pady=30)

        self.root.mainloop()

if __name__=="__main__":
    database = join(getcwd(),"database.db")
    db = Database(database)
    BudgetApp(db)