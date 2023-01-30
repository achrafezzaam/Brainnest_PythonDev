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
        self.cur.execute("CREATE TABLE IF NOT EXISTS expense_record (tag_name text, amount float, entry_date date)")
        self.conn.commit()

    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, tag_name, amount, entry_date):
        self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?)",
                        (tag_name, amount, entry_date))
        self.conn.commit()
    
    def showtable(self,root):
        expenses = pd.read_sql_query("SELECT * FROM expense_record",self.conn)
        fig1 = expenses.plot().get_figure()
        my_graph = Toplevel(root)
        my_graph.title("My Budget")
        plot1 = FigureCanvasTkAgg(fig1, my_graph)
        plot1.get_tk_widget().grid(row=0,column=0)
        Button(my_graph, text="Quit", command=my_graph.destroy).grid(row=1,column=0)
        # my_graph.mainloop()

    '''
    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, tag_name, amount, entry_date,rid):
        self.cur.execute("UPDATE expense_record SET tag_name = ?, amount = ?, entry_date = ? WHERE rowid = ?",
                        (tag_name, amount, entry_date, rid))
        self.conn.commit()
    '''

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
        tag_field = StringVar()
        Label(self.frm1,text="Enter tag name",anchor='w',width=20).grid(column=0,row=0)
        Entry(self.frm1,textvariable=tag_field).grid(column=1,row=0,padx=4)

        Label(self.frm1,text="Enter amount",anchor='w',width=20).grid(column=0,row=1)
        amount_field = DoubleVar()
        Entry(self.frm1,textvariable=amount_field).grid(column=1,row=1,padx=4)

        Button(self.frm1,text="Add Record", command=addRecord, width=14).grid(column=2,row=0,padx=20)
        Button(self.frm1,text="Update Record", width=14).grid(column=2,row=1,padx=20)
        Button(self.frm1,text="Delete Record", width=14).grid(column=2,row=2,padx=20)
        Button(self.frm1,text="Show plot", command=lambda:self.db.showtable(self.root), width=14).grid(column=2,row=3,pady=10)
        Button(self.frm1, text="Quit", command=self.root.destroy).grid(column=2,row=4,pady=30)

        self.root.mainloop()

if __name__=="__main__":
    database = join(getcwd(),"database.db")
    db = Database(database)
    BudgetApp(db)