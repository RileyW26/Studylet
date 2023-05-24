from tkinter import * 
from tkinter.ttk import *

# create main window 
root = Tk()

root.title("Text")
root.attributes('-fullscreen', True)

# Labe lis what output will be 
# show on window
#label = Label(root, text = "Hello World !").pack()

def newWindow():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    newWindow.title("new")

    newWindow.attributes('-fullscreen', True)

    root.withdraw()


btn = Button(root, text = 'Exit',
             command = root.destroy)#Exit 
studysetbtn = Button(root, text = 'Study sets',
                     command = lambda:[newWindow()])
btn.pack(side = 'right')
studysetbtn.pack(side = 'left')
# calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
mainloop()