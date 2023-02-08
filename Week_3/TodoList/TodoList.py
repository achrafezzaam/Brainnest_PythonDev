from os import getcwd
from os.path import join
from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime

class Database:
    def __init__(self, db:str) -> None: # Creates the todos table if not existing and connecting to it
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todos (id integer primary key, todo text UNIQUE)")
        self.conn.commit()
    
    def getTodos(self) -> dict[str,int]:        # Select all the todos from the todos table and returns a dictionary 
        self.cur.execute("SELECT * FROM todos") # with the todo content and id ( this will be used for the listing 
        all_todos = self.cur.fetchall()         # and the deletion of todo items in the GUI)
        output_dict = {}
        for id,todo in all_todos:
            output_dict[todo] = id
        return output_dict

    def insertTodo(self, todo:str) -> None:                     # Insert a todo to the database
        self.cur.execute("INSERT INTO todos VALUES (NULL, ?)",
                        (todo,))
        self.conn.commit()

    def removeTodo(self, rwid: int) -> None:                        # Deletes a todo from the database
        self.cur.execute("DELETE FROM todos WHERE id=?", (rwid,))
        self.conn.commit()

    def __del__(self) -> None:  # Closes the connexion to the database
        self.conn.close()

class TodoApp:
    def __init__(self,db:Database) -> None: # Creates the Todo object, takes the Database object as argument
        self.db = db
        self.todos = self.db.getTodos()
        self.root = Tk()
        self.root.title("Todo App")
        self.root.geometry('500x450+500+200')
        self.root.resizable(width=False, height=False)
        self.root.config(bg='#333')
        self.frm1 = Frame(self.root)
        self.frm1.pack(pady=10)
        self.frm2 = Frame(self.root)
        self.frm2.pack(pady=20)
        self.BuildGUI()
    
    def BuildGUI(self) -> None:
        def newTask() -> None:
            task = my_entry.get()
            if task != "":
                if task not in self.todos:
                    self.db.insertTodo(task)
                    lb.insert(END, task)
                    my_entry.delete(0, "end")
                else:
                    messagebox.showwarning("warning", "This todo already exists.")
            else:
                messagebox.showwarning("warning", "Please enter some task.")
        
        def deleteTask() -> None:
            val = lb.get(lb.curselection())
            self.db.removeTodo(self.todos[val])
            lb.delete(ANCHOR)
            
        # Create the Listbox element that will contain the todo's list
        lb = Listbox(
            self.frm1,
            width=25,
            height=8,
            font=('Times', 14),
            bd=0,
            bg="#333",
            fg='#CCC',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none"
        )
        lb.pack(side=LEFT, fill=BOTH)

        sb = Scrollbar(self.frm1) # Adding a scroll bar to the Listbox element
        sb.pack(side=RIGHT, fill=BOTH)

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

        # Entry field where new todos will be created
        my_entry = Entry(
            self.root,
            font=('times', 16)
            )
        my_entry.pack(pady=20)

        # Button to add a todo
        addTask_btn = Button(
            self.frm2,
            text='Add Task',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=newTask
        )
        addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        # Button to delete a todo
        delTask_btn = Button(
            self.frm2,
            text='Delete Task',
            font=('times 14'),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=deleteTask
        )
        delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        #inserting the queried todos in the Listbox element
        for item in self.todos:
            lb.insert(END, item)

        self.root.mainloop()
    


if __name__=="__main__":
    database = join(getcwd(),"database.db")
    db = Database(database)
    TodoApp(db)