from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
import os

def flashcardHome(type):
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
    addbtn = Button(flashcardMenu, text = 'Add flashcard',
                    command = lambda:[addFlashcard(flashcardMenu)])
    removebtn = Button(flashcardMenu, text = 'Remove flashcard')
    backbtn = Button(flashcardMenu, text = 'Back',
                     command = lambda:[backHome(flashcardMenu)])
    playbtn.pack(side = 'top')
    addbtn.pack(side='top')
    removebtn.pack(side = 'top')
    backbtn.pack(side='bottom')
def quizMenu(type):
    # Toplevel object which will be treated as a new window
    quizMenu = Toplevel(root)

    quizMenu.title(type)

    quizMenu.attributes('-fullscreen', True)

    root.withdraw()  # closes the root window
    playbtn = Button(quizMenu, text = 'Play quizzes')
    addbtn = Button(quizMenu, text = 'Add quizzes')
    removebtn = Button(quizMenu, text = 'Remove quizzes')
    backbtn = Button(quizMenu, text = 'Back',
                     command = lambda:[backHome(quizMenu)])
    playbtn.pack(side = 'top')
    addbtn.pack(side='top')
    removebtn.pack(side = 'top')
    backbtn.pack(side='bottom')
def homeMenu():
    flashcard = "flashcard"
    quiz = "quiz"
    exitbtn = Button(root, text = 'Exit',
                command = root.destroy)#Exit 
    flashcardbtn = Button(root, text = 'Flashcard',
                        command = lambda:[flashcardHome(flashcard)])
    quizbtn = Button(root, text = 'Quiz',
                    command = lambda:[quizMenu(quiz)])

    flashcardbtn.pack(side = 'top')
    quizbtn.pack(side = 'top')
    exitbtn.pack(side = 'top')
    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()
def backHome(window):
    window.destroy()
    root.deiconify()
def addFlashcard(window):
    window.destroy()
    addingFlashcard = Toplevel()

    addingFlashcard.title('Adding Flashcard')

    addingFlashcard.attributes('-fullscreen', True)
    addbtn = Button(addingFlashcard, text = 'Add',
                    command = addData(title)).place(anchor = CENTER, relx = .4, rely = .2)
    backbtn = Button(addingFlashcard, text = 'Back').place(anchor = CENTER,relx = .5, rely = .2 )
    titlelbl = Label(addingFlashcard, text = "Title:").place(anchor = CENTER, relx = .4, rely = .1)
    titlebox = Entry(addingFlashcard).place(anchor = CENTER, relx = .5, rely = .1)
    titlelbl.pack()
    titlebox.pack()
    addbtn.pack()
    backbtn.pack()
    title = titlebox.get()
    print(titlebox)
def addData(data):
    print(data)
# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu()