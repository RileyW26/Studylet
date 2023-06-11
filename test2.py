import tkinter as tk
from tkinter import ttk

def create_table():
    root = tk.Tk()
    root.title("Table Example")
    
    # Create Treeview widget
    tree = ttk.Treeview(root)
    tree["columns"] = ("column1", "column2", "column3")
    
    # Define column headings
    tree.heading("column1", text="Column 1")
    tree.heading("column2", text="Column 2")
    tree.heading("column3", text="Column 3")
    
    # Insert data rows
    tree.insert("", tk.END, values=("Data 1", "Data 2", "Data 3"))
    tree.insert("", tk.END, values=("Data 4", "Data 5", "Data 6"))
    
    # Pack the Treeview widget
    tree.pack()

    root.mainloop()

# Call the function to create the table
create_table()
