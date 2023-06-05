import tkinter as tk

def toggle_scrollbar():
    if scrollbar.cget('width') == 0:
        scrollbar.config(width=10)
    else:
        scrollbar.config(width=0)

root = tk.Tk()

# Create a canvas with a scrollbar
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

button = tk.Button(root, text="Toggle Scrollbar", command=toggle_scrollbar)
button.pack()

root.mainloop()
