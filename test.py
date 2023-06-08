import tkinter as tk

def check_entry():
    text = entry.get()
    if text.isspace():
        print("The entry contains only spaces")
    else:
        print("The entry does not contain only spaces")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check Entry", command=check_entry)
button.pack()

root.mainloop()
