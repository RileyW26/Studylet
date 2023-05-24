from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
# create main window 
root = Tk()

root.title("Text")
root.attributes('-fullscreen', True)

def flashcardMenu(type):
    # Toplevel object which will be treated as a new window
    flashcardMenu = Toplevel(root)

    flashcardMenu.title(type)

    flashcardMenu.attributes('-fullscreen', True)

    root.withdraw()  # closes the root window
    #Display text
    '''t = Text(flashcardMenu, height=5, width = 52)
    t.pack()
    t.insert(tk.END, type)
    '''
    playbtn = Button(flashcardMenu, text = 'Play flashcard')
    addbtn = Button(flashcardMenu, text = 'Add flashcard')
    removebtn = Button(flashcardMenu, text = 'Remove flashcard')
    backbtn = Button(flashcardMenu, text = 'Back',
                     command = lambda:[backHome()])
    playbtn.pack(side = 'top')
    addbtn.pack(side='top')
    removebtn.pack(side = 'top')
    backbtn.pack(side='bottom')
def quizMenu():
    # Toplevel object which will be treated as a new window
    quizMenu = Toplevel(root)

    quizMenu.title(type)

    quizMenu.attributes('-fullscreen', True)

    root.withdraw()  # closes the root window
    #Display text
    '''t = Text(quizMenu, height=5, width = 52)
    t.pack()
    t.insert(tk.END, type)'''
    playbtn = Button(quizMenu, text = 'Play quiz')
    playbtn.pack(side = 'bottom')
def homeMenu():
    flashcard = "flashcard"
    quiz = "quiz"
    exitbtn = Button(root, text = 'Exit',
                command = root.destroy)#Exit 
    flashcardbtn = Button(root, text = 'Flashcard',
                        command = lambda:[flashcardMenu(flashcard)])
    quizbtn = Button(root, text = 'Quiz',
                    command = lambda:[quizMenu(quiz)])

    flashcardbtn.pack(side = 'top')
    quizbtn.pack(side = 'top')
    exitbtn.pack(side = 'top')
    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()
def backHome():
    root.deiconify()
homeMenu()