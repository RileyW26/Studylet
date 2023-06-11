from tkinter import *
from tkinter.ttk import *

def disable_column_resizing(event):
    # Prevent the Treeview widget from resizing columns
    return "break"

def create_treeview():
    root = Tk()
    root.title("Disable Column Resizing")

    tree = Treeview(root)
    tree["columns"] = ("Column1", "Column2", "Column3")

    tree.column("Column1", width=100)
    tree.column("Column2", width=150)
    tree.column("Column3", width=200)

    tree.heading("Column1", text="Column 1")
    tree.heading("Column2", text="Column 2")
    tree.heading("Column3", text="Column 3")

    # Insert data rows
    tree.insert("", END, values=("Data 1", "Data 2", "Data 3"))
    tree.insert("", END, values=("Data 4", "Data 5", "Data 6"))

    tree.bind("<ButtonPress-1>", disable_column_resizing)

    tree.pack()
    root.mainloop()

create_treeview()
