from tkinter import tk
from tkinter.ttk import *

root = Tk()

# Create a frame
frame = Frame(root, width=200, height=200)
frame.pack()
longtext = """
I'm obviously just a button.
It doesn't take much to be a button.
The text is used to tell the user when
It happens when I get pushed.
What's the matter, but why me?
That long?
"""

b = tk.Button(frame, text=longtext, anchor ="w", justify="left", padx=2, command= callback)
b.pack()


root.mainloop()
