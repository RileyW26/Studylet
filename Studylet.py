from tkinter import * 
from tkinter.ttk import *
import os
from os.path import exists

def flashcardHome(window):
    '''
    Flashcard menu where you can choose to start playing with flashcard sets.
    '''
    window.delete('all')
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 40  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    title = "Flashcard Menu"
    titlelbl = Label(frame, text = title)
    playbtn = Button(frame, text = 'Play flashcard',
                     command = lambda:[flashcardList(canvas)])
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[homeMenu(canvas)])
    
    titlelbl.pack()
    playbtn.pack()
    backbtn.pack()
def flashcardList(window):
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "r")
    lines = len(f.readlines())
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 20  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=NW)

    titlelbl = Label(frame, text = 'Available Studysets')
    titlelbl.pack()
    backbutton = Button(frame, text = "back",
                        command = lambda:[flashcardHome(canvas), toggle_scrollbar(scrollbar)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[flashcard(canvas), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
def flashcard(window):
    pass
def quizMenu(window):
    window.delete('all')
    # Toplevel object which will be treated as a new window
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 40  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

    title = "Quiz Menu"
    titlelbl = Label(frame, text = title)
    playbtn = Button(frame, text = 'Play quizzes')
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[homeMenu(canvas)])
    titlelbl.pack()
    playbtn.pack()
    backbtn.pack()
def homeMenu(window):
    '''
    The home menu of the program, where you can navigate to the flashcard section, quiz section and add and remove studyset section
    '''
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    title = "Studylet"
    titlelbl = Label(frame, text = title)
    exitbtn = Button(frame, text = 'Exit',
                command = root.destroy)#Exit 
    flashcardbtn = Button(frame, text = 'Flashcard',
                        command = lambda:[flashcardHome(canvas)])
    quizbtn = Button(frame, text = 'Quiz',
                    command = lambda:[quizMenu(canvas)])
    studysetbtn = Button(frame, text = "Studysets",
                         command = lambda:[studysetMenu(canvas)])
    titlelbl.pack()
    flashcardbtn.pack()
    quizbtn.pack()
    studysetbtn.pack()
    exitbtn.pack()
    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()
def studysetMenu(window):
    '''
    allows users to add or remove study sets
    '''
    window.delete('all')
    window.config(yscrollcommand=None)
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    titlelbl = Label(frame, text = "Studyset Menu")
    addbtn = Button(frame, text = "Add Studyset", command = lambda:[addstudyset(canvas)])
    removebtn = Button(frame, text = "Remove Studyset", command = lambda:[removeMenu(canvas)])
    add2btn = Button(frame,text = "Adding prexisitng studysets, through a csv", command = lambda:[addExisting(canvas)])
    backbtn = Button(frame, text = "Back", command = lambda:[homeMenu(canvas)])
    titlelbl.pack()
    addbtn.pack()
    add2btn.pack()
    removebtn.pack()
    backbtn.pack()
def addstudyset(window):
    '''
    Prompts the user for a title, term and definiton with an add and back button
    '''
    window.delete('all')
    canvas_width_percentage = 40 # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height
    canvas_width_percentage2 = 60
    canvas_width_percentage3 = 50
    canvas_height_percentage3 = 20
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas_width2 = percentageWindow(canvas_width_percentage2, window_width)
    canvas_width3 = percentageWindow(canvas_width_percentage3, window_width)
    canvas_height3 = percentageWindow(canvas_height_percentage3, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    frame2 = Frame(canvas)
    canvas.create_window((canvas_width2, canvas_height), window=frame2, anchor=CENTER)
    frame3 = Frame(canvas)
    canvas.create_window((canvas_width3, canvas_height3), window=frame3, anchor = CENTER)
    title = "Creating Flashcard Set"
    titlePage = Label(frame3, text = title)
    titlelbl = Label(frame, text = "Title:")
    titlebox = Entry(frame2)
    termlbl = Label(frame, text = "Term:")
    termbox = Entry(frame2)
    deflbl = Label(frame, text = 'Definition:')
    defbox = Entry(frame2)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addData(titlebox, termbox, defbox), addFlashcard2(canvas)])
    backbtn = Button(frame2, text = 'Back',
                     command = lambda:[studysetMenu(canvas)])
    titlePage.pack()
    titlelbl.pack()
    titlebox.pack()
    termlbl.pack()
    termbox.pack()
    deflbl.pack()
    defbox.pack()
    addbtn.pack()
    backbtn.pack()
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
    window.delete('all')
    canvas_width_percentage = 40 # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height
    canvas_width_percentage2 = 60
    canvas_width_percentage3 = 50
    canvas_height_percentage3 = 20
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas_width2 = percentageWindow(canvas_width_percentage2, window_width)
    canvas_width3 = percentageWindow(canvas_width_percentage3, window_width)
    canvas_height3 = percentageWindow(canvas_height_percentage3, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    frame2 = Frame(canvas)
    canvas.create_window((canvas_width2, canvas_height), window=frame2, anchor=CENTER)
    frame3 = Frame(canvas)
    canvas.create_window((canvas_width3, canvas_height3), window=frame3, anchor = CENTER)
    title = "Creating Flashcard Set"
    titlePage = Label(frame3, text = title)
    termlbl = Label(frame, text = "Term:")
    termbox = Entry(frame2)
    deflbl = Label(frame, text = 'Definition:')
    defbox = Entry(frame2)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addData2(termbox, defbox), addFlashcard2(canvas)])
    backbtn = Button(frame2, text = 'Back',
                     command = lambda:[studysetMenu(canvas)])
    titlePage.pack()
    termlbl.pack()
    termbox.pack()
    deflbl.pack()
    defbox.pack()
    addbtn.pack()
    backbtn.pack()
def addData2(term, definition):
    '''
    Appends a term and definition onto studysets.csv, pulling them from entries 
    '''
    term = term.get()
    definition = definition.get()
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "a")
    f.write("|" + term + "|" + definition)
    f.close()
def removeMenu(window):
    '''
    SHows the user a list of the available study sets, clicking on one will bring them to a page where they can edit or remove the entire studyset
    '''    
    window.delete('all')
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "r")
    lines = len(f.readlines())
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 20  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=NW)

    titlelbl = Label(frame, text = 'Remove Available Studysets')
    titlelbl.pack()
    backbutton = Button(frame, text = "back",
                        command = lambda:[studysetMenu(canvas), toggle_scrollbar(scrollbar)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[removeSet(canvas, id), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
    
def titles(lines):
    '''
    Returns a string of all the elements before | in studysets.csv, the title of the studyset
    '''
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[lines]
    termsAndDefinitions = line.split("|")
    title = termsAndDefinitions[0]
    file.close()
    return title
def seperateTermsDefinitions(termsAndDefinitionsValues):
    '''
    Returns terms and definitions
    '''
    terms = []
    definitions = []
    for i in range (1, len(termsAndDefinitionsValues)):
        if i % 2 == 0:
            definitions.append(termsAndDefinitionsValues[i])
        elif i % 2 != 0: 
            terms.append(termsAndDefinitionsValues[i])
    #print(terms)
    #print(definitions)
    return terms, definitions
def percentageWindow(percentage, total_length):
    '''
    Creates percentages of the screen, allowing percentages to be applied to frames on a canvas
    '''
    return int(percentage / 100 * total_length)
def removeSet(window, num):
    '''
    Screen that shows list of terms and definitions on a studyset, in an entry box where the user can modify them as they would like.  
    They can save the entries, or remove the entire studyset
    '''
    window.delete('all')
   
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[int(num)]
    value = line.split("|")
    values = seperateTermsDefinitions(value)
    terms, defintions = values
    canvas_width_percentage = 30  # Width as a percentage of the window width
    canvas_height_percentage = 20  # Height as a percentage of the window height
    canvas_width_percentage2 = 70
    canvas_width_percentage3 = 50
    canvas_height_percentage3 = 10
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_width2 = percentageWindow(canvas_width_percentage2, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas_width3 = percentageWindow(canvas_width_percentage3, window_width)
    canvas_height3 = percentageWindow(canvas_height_percentage3, window_height)
     # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    
    frame2 = Frame(canvas)
    canvas.create_window((canvas_width2, canvas_height), window =frame2, anchor = CENTER)
    
    frame3 = Frame(canvas)
    canvas.create_window((canvas_width3, canvas_height3), window=frame3, anchor = CENTER)

    frame4 = Frame(canvas)
    canvas.create_window((canvas_width3, canvas_height), window = frame4, anchor = CENTER)
    termlbl = Label(frame, text = 'Terms:')
    deflbl = Label(frame2, text = 'Definitions:')
    termlbl.pack()
    deflbl.pack()
    termEntry = []
    defEntry = []
    titlelbl = Label(frame3, text = 'Edit studyset "' + titles(num)+'"')
    titlelbl.pack()
    blank = Label(frame4, text = '')
    blank.pack()
    file.close()
    for i in range(len(terms)):
        entry = Entry(frame)
        entry.insert(END, terms[i])
        entry.pack()
        termEntry.append(entry)
        blank = Label(frame4, text = '')
        blank.pack()
    for i in range(len(defintions)):
        entry2 = Entry(frame2)
        entry2.insert(END, defintions[i])
        entry2.pack()
        defEntry.append(entry2)
    savebtn = Button(frame4, text = 'Save',
                     command = lambda:[save(termEntry, defEntry, num),toggle_scrollbar(scrollbar), removeMenu(canvas)  ])
    savebtn.pack()
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[removeMenu(canvas),toggle_scrollbar(scrollbar)])
    backbtn.pack()
    removebtn = Button(frame2, text = "Remove Entire Studyset",
                       command = lambda:[removeLine(num),toggle_scrollbar(scrollbar), removeMenu(canvas)])
    removebtn.pack()
def save(term, definition, num):
    '''
    appends the term and definition values pulled from entries that the user can edit 
    '''
    title = titles(num)
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "a")
    
    file.write(title)
    for i in range(len(term)):
        t = term[i].get()
        d = definition[i].get()
        stripd = d.replace('\n', '')
        file.write("|" + t + "|" + stripd)
    file.close()
    removeLine(num)
def strip(line):
    '''
    Strips lines of the line break
    '''
    newLine = line.replace('\n', '')
    return newLine
def removeLine(num):
    '''
    Function that removes a line
    '''
    num = num + 1
    fileName = os.getcwd() + '\\Studysets.csv'
    remove_line_from_csv(fileName, num)
def remove_line_from_csv(file_path, line_number):
    '''
    Removes a line from a csv
    '''
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    filew = open(file_path, 'w', newline = '')
    for index, line in enumerate( lines, start = 1):
        if index != line_number:
            filew.write(strip(line) + '\n')
    filew.close()
def toggle_scrollbar(scrollbar):
    '''
    removes the scrollbar
    '''
    scrollbar.pack_forget()
def addExisting(window):
    '''
    Window that gives the user their current direcctory and has an entry box for a csv file to be input
    '''
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 40  # Height as a percentage of the window height

    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    # Create a Canvas widget
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

    titlelbl = Label(frame, text = "Add prexisitng studysets, through a csv")
    currentdirectory = Label(frame, text = "Directory: " + os.getcwd())
    csventry = Entry(frame)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addCsv(csventry),studysetMenu(canvas)])
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[studysetMenu(canvas)])
    titlelbl.pack()
    currentdirectory.pack()
    csventry.pack()
    addbtn.pack()
    backbtn.pack()
def addCsv(entry):
    '''
    reads the csv that the user inputted and appends it onto the studysets.csv that the programs reads
    '''
    fileName = os.getcwd() + "\\" + entry.get()
    file = open(fileName, "r")
    text = file.readlines()
    file.close()
    studysets = os.getcwd() + "\\Studysets.csv"
    file = open(studysets, "a")
    file.writelines(text + "\n") 
# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu(root)