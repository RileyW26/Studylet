from tkinter import * 
from tkinter.ttk import *
import csv
import os
from os.path import exists
def back(window, title):
    '''
    One function which will return any page back a page
    '''
    window.destroy()
    if (title == "Flashcard Menu") or (title =="Quiz Menu"):
        root.deiconify()
    elif (title == "Creating Flashcard Set"):
        flashcardHome()
    elif (title == "Remove Studysets"):
        flashcardHome()
def flashcardHome():
    # Toplevel object which will be treated as a new window
    flashcardMenu = Toplevel(root)

    flashcardMenu.title('Flashcard Home Menu')

    flashcardMenu.attributes('-fullscreen', True)

    root.withdraw()  # closes the root window
    title = "Flashcard Menu"
    titlelbl = Label(flashcardMenu, text = title)
    playbtn = Button(flashcardMenu, text = 'Play flashcard')
    addbtn = Button(flashcardMenu, text = 'Add flashcard',
                    command = lambda:[addFlashcard(flashcardMenu)])
    removebtn = Button(flashcardMenu, text = 'Remove flashcard',
                       command = lambda:[removeMenu(flashcardMenu)])
    backbtn = Button(flashcardMenu, text = 'Back',
                     command = lambda:[back(flashcardMenu, title)])
    titlelbl.place(anchor = CENTER, relx = .5, rely = .1)
    playbtn.place(anchor = CENTER, relx = .3, rely = .3)
    addbtn.place(anchor = CENTER, relx = .5, rely = .3)
    removebtn.place(anchor = CENTER, relx = .7, rely = .3)
    backbtn.place(anchor = CENTER, relx = .5, rely = .4)
def quizMenu():
    # Toplevel object which will be treated as a new window
    quizMenu = Toplevel(root)

    quizMenu.title('Quiz Home Menu')

    quizMenu.attributes('-fullscreen', True)

    title = "Quiz Menu"
    titlelbl = Label(quizMenu, text = title)
    root.withdraw()  # closes the root window
    playbtn = Button(quizMenu, text = 'Play quizzes')
    addbtn = Button(quizMenu, text = 'Add quizzes')
    removebtn = Button(quizMenu, text = 'Remove quizzes')
    backbtn = Button(quizMenu, text = 'Back',
                     command = lambda:[back(quizMenu, title)])
    titlelbl.place(anchor = CENTER, relx = .5, rely = .1)
    playbtn.place(anchor = CENTER, relx = .3, rely = .3)
    addbtn.place(anchor = CENTER, relx = .5, rely = .3)
    removebtn.place(anchor = CENTER, relx = .7, rely = .3)
    backbtn.place(anchor = CENTER, relx = .5, rely = .4)
def homeMenu():
    title = "Studylet"
    titlelbl = Label(root, text = title)
    exitbtn = Button(root, text = 'Exit',
                command = root.destroy)#Exit 
    flashcardbtn = Button(root, text = 'Flashcard',
                        command = lambda:[flashcardHome()])
    quizbtn = Button(root, text = 'Quiz',
                    command = lambda:[quizMenu()])
    titlelbl.place(anchor = CENTER, relx = .5, rely = .1)
    flashcardbtn.place(anchor = CENTER, relx = .3, rely = .4)
    quizbtn.place(anchor = CENTER, relx = .7, rely = .4)
    exitbtn.place(anchor = CENTER, relx = .5, rely = .6)
    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()

def addFlashcard(window):
    window.destroy()
    addingFlashcard = Toplevel()

    addingFlashcard.title('Adding Flashcard')

    addingFlashcard.attributes('-fullscreen', True)
    title = "Creating Flashcard Set"
    titlePage = Label(addingFlashcard, text = title)
    titlelbl = Label(addingFlashcard, text = "Title:")
    titlebox = Entry(addingFlashcard)
    termlbl = Label(addingFlashcard, text = "Term:")
    termbox = Entry(addingFlashcard)
    deflbl = Label(addingFlashcard, text = 'Definition:')
    defbox = Entry(addingFlashcard)
    addbtn = Button(addingFlashcard, text = 'Add',
                    command = lambda:[addData(titlebox, termbox, defbox), addFlashcard2(addingFlashcard)])
    backbtn = Button(addingFlashcard, text = 'Back',
                     command = lambda:[back(addingFlashcard, title)])
    titlePage.place(anchor = CENTER, relx = .5, rely = .1)
    titlelbl.place(anchor = CENTER, relx = .4, rely = .2)
    titlebox.place(anchor = CENTER, relx = .5, rely = .2)
    termlbl.place(anchor = CENTER, relx = .4, rely= .3 )
    termbox.place(anchor = CENTER, relx = .5, rely= .3 )
    deflbl.place(anchor = CENTER, relx = .4, rely = .4)
    defbox.place(anchor = CENTER, relx = .5, rely = .4)
    addbtn.place(anchor = CENTER, relx = .4, rely = .5)
    backbtn.place(anchor = CENTER,relx = .5, rely = .5 )
def addData(title, term, definition):
    title = title.get()
    term = term.get()
    definition = definition.get()
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    fileExists = exists(file)
    print(file)
    if fileExists == True:
        f = open(file, "a")
        f.write("\n" + title +"|" + term + "|" + definition)
        f.close()
    else:
        f = open(file, "w")
        f.write(title +"|" + term + "|" + definition)
        f.close()
def addFlashcard2(window):
    window.destroy()
    addingFlashcard = Toplevel()

    addingFlashcard.title('Adding Flashcard')

    addingFlashcard.attributes('-fullscreen', True)
    title = "Creating Flashcard Set"
    titlePage = Label(addingFlashcard, text = title)
    termlbl = Label(addingFlashcard, text = "Term:")
    termbox = Entry(addingFlashcard)
    deflbl = Label(addingFlashcard, text = 'Definition:')
    defbox = Entry(addingFlashcard)
    addbtn = Button(addingFlashcard, text = 'Add',
                    command = lambda:[addData2(termbox, defbox), addFlashcard2(addingFlashcard)])
    backbtn = Button(addingFlashcard, text = 'Back',
                     command = lambda:[back(addingFlashcard, title)])
    titlePage.place(anchor = CENTER, relx = .5, rely = .1)
    termlbl.place(anchor = CENTER, relx = .4, rely= .2 )
    termbox.place(anchor = CENTER, relx = .5, rely= .2 )
    deflbl.place(anchor = CENTER, relx = .4, rely = .3)
    defbox.place(anchor = CENTER, relx = .5, rely = .3)
    addbtn.place(anchor = CENTER, relx = .4, rely = .4)
    backbtn.place(anchor = CENTER,relx = .5, rely = .4 )
def addData2(term, definition):
    term = term.get()
    definition = definition.get()
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "a")
    f.write("|" + term + "|" + definition)
    f.close()
def removeMenu(window):
    window.destroy()
    removeMenu = Toplevel()

    removeMenu.title('Adding Flashcard')

    removeMenu.attributes('-fullscreen', True)
    
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "r")
    lines = len(f.readlines())
    # Create a Canvas widget
    canvas = Canvas(removeMenu)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = Scrollbar(removeMenu, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=NW)

    # Page title
    title = "Remove Studysets"
    titlelbl = Label(removeMenu, text = title)
    titlelbl.place(anchor = CENTER, relx = .5, rely = .1)
    backbutton = Button(removeMenu, text = "back",
                        command = lambda:[back(removeMenu, title)])
    backbutton.place(anchor = CENTER, relx = .5, rely = .8)
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i))
            button.pack(side = "top", fill = X)

    
def titles(lines):
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[lines]
    termsAndDefinitions = line.split("|")
    title = termsAndDefinitions[0]
    return title
# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu()