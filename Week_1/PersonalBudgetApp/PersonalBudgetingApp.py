''' The goal of this project is to create a personal budgeting app that allows users to track their income and expenses, set budget goals, and view their spending habits.



Here are the steps you can take to create this project:



    Use the sqlite3 library to create a database to store the user's budget data.



    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons, text boxes and tables.



    Use the pandas library to manipulate the data and generate charts and tables to visualize the user's budget data.



    Use the datetime library to store and display the date and time of the transactions. '''

from os import getcwd
from os.path import join
import sqlite3
from tkinter import *
from tkinter import ttk

# database = join(getcwd(),"database.db")


# import sqlite3

# class Database:
#     def __init__(self, db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute(
#             "CREATE TABLE IF NOT EXISTS expense_record (tag_name text, amount float, entry_date date)")
#         self.conn.commit()

#     def fetchRecord(self, query):
#         self.cur.execute(query)
#         rows = self.cur.fetchall()
#         return rows

#     def insertRecord(self, tag_name, amount, entry_date):
#         self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?)",
#                          (tag_name, amount, entry_date))
#         self.conn.commit()

#     def removeRecord(self, rwid):
#         self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
#         self.conn.commit()

#     def updateRecord(self, tag_name, amount, entry_date, rid):
#         self.cur.execute("UPDATE expense_record SET tag_name = ?, amount = ?, entry_date = ? WHERE rowid = ?",
#                          (tag_name, amount, entry_date, rid))
#         self.conn.commit()

#     def __del__(self):
#         self.conn.close()

root = Tk()
root.title("Personal Budgeting")
root.geometry("1000x562")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Enter tag name", anchor='w', width=28).grid(column=0, row=0)
tag_name = StringVar()
ttk.Entry(frm, textvariable=tag_name).grid(column=1, row=0)

ttk.Label(frm, text="Entry type ( Expanse or Income )", anchor='w', width=28).grid(column=0, row=1)
type = StringVar()
ttk.Entry(frm, textvariable=type).grid(column=1, row=1)

ttk.Label(frm, text="Enter amount", anchor='w', width=28).grid(column=0, row=2)
amount = StringVar()
ttk.Entry(frm, textvariable=amount).grid(column=1, row=2)

ttk.Button(frm, text="Quit").grid(column=1, row=3, pady=20)

root.mainloop()

# def create_connection(database):
#     """ create a database connection to a SQLite database """
#     conn = None
#     try:
#         conn = sqlite3.connect(database)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# if __name__ == '__main__':
#     create_connection(database)
