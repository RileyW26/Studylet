from tkinter import * 
from tkinter.ttk import *
import os
from os.path import exists
from tkinter import filedialog as fd 
from tkinter import messagebox
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
                            command = lambda id = i:[flashcard(canvas, id), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
def flashcard(window, num):
    '''
    Creates a base for the flashcards to be displayed
    '''
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[int(num)]
    value = line.split("|")
    td2 = seperateTermsDefinitions(value)
    terms, definitions = td2
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    count = 0
    flashcardShow(canvas, num, terms, definitions, count)
def flashcardShow(window, num, t, d, count):
    '''
    Will display the flashcard as well as a next and back button 
    '''
    window.delete('all')
    canvas_width_percentage = 50 # Width as a percentage of the window width
    canvas_height_percentage = 20  # Height as a percentage of the window height
    canvas_height_percentage2 = 50
    canvas_height_percentage3 = 80
    canvas_width_percentage2 = 40
    canvas_width_percentage3 = 60
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas_height2 = percentageWindow(canvas_height_percentage2, window_height)
    canvas_height3 = percentageWindow(canvas_height_percentage3, window_height)
    canvas_width2 = percentageWindow(canvas_width_percentage2, window_width)
    canvas_width3 = percentageWindow(canvas_width_percentage3, window_width)
    max = len(t) - 1
    frame = Frame(window)
    window.create_window((canvas_width, canvas_height), window = frame, anchor = CENTER)
    titlelbl = Label(frame, text = 'Playing: "' + titles(num) + '"')
    titlelbl.pack()
    frame2 = Frame(window)
    window.create_window((canvas_width, canvas_height2), window = frame2, anchor = CENTER)
    termbutton = Button(frame2, text = strip(t[count]), command = lambda id = count:[showCorrosponding(id, d, termbutton, t)])
    frame3 = Frame(window)
    window.create_window((canvas_width2, canvas_height3), window = frame3, anchor = CENTER)
    frame4 = Frame(window)
    window.create_window((canvas_width3, canvas_height3), window = frame4, anchor = CENTER)
    backbutton = Button(frame3, text = "Back", 
                        command = lambda:[flashcardShow(window, num, t, d, count-2)])
    nextbtn = Button(frame4, text = "Next", command = lambda:[flashcardShow(window, num, t, d, count)])

    homebtn = Button(frame4, text = "Back Home", command = lambda:[flashcardList(window)])
    homebtn2 = Button(frame3, text = "Back Home", command = lambda:[flashcardList(window)])
    if count == max:
        termbutton.pack()
        backbutton.pack()
        homebtn.pack()
    elif count == 0:
        termbutton.pack()
        homebtn2.pack()
        nextbtn.pack()    
    else:
        termbutton.pack()
        backbutton.pack()
        nextbtn.pack()
    count += 1
def showCorrosponding(num, definitions, button, t):
   '''
   configures the flashcard to show the definition if the term is currently on the flashcard and vice versa
   '''
   if button.cget("text") == t[num]:
       button.config(text = strip(definitions[num]))
   else:
       button.config(text = strip(t[num]))
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
                    command = lambda:[addData(titlebox, termbox, defbox, canvas)])
    backbtn = Button(frame2, text = 'Back',
                     command = lambda:[studysetMenu(canvas),])
    titlePage.pack()
    titlelbl.pack()
    titlebox.pack()
    termlbl.pack()
    termbox.pack()
    deflbl.pack()
    defbox.pack()
    addbtn.pack()
    backbtn.pack()
def addData(title, term, definition, window):
    '''
    Checks if a file exists, if it does not then enters write mode and writes data taken from entry boxes.
    If file exists then enters append mode and appends data taken from entry boxes
    '''
    title = title.get()
    term = term.get()
    definition = definition.get()
    if (title == '') or (title.isspace()):
        messagebox.showerror("Error", "Title Field can not be blank")
    elif (term == '') or (term.isspace()):
        messagebox.showerror("Error", "Term Field can not be blank")
    elif (definition == '') or (definition.isspace()):
        messagebox.showerror("Error", "Definition Field can not be blank")
    else:
        folder = os.getcwd()
        file = folder + "\\Studysets.csv"
        fileExists = exists(file)
        print(file)
        if fileExists == True:
            f = open(file, "a")
            f.write(title +"|" + term + "|" + definition)
            f.close()
        else:
            f = open(file, "w")
            f.write(title +"|" + term + "|" + definition)
            f.close()
        addFlashcard2(window)
def addFlashcard2(window):
    '''
    Window that has data boxes for adding a term and definition, only appears after the first flashcard add menu has been gone through
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
    termlbl = Label(frame, text = "Term:")
    termbox = Entry(frame2)
    deflbl = Label(frame, text = 'Definition:')
    defbox = Entry(frame2)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addData2(termbox, defbox, canvas)])
    backbtn = Button(frame2, text = 'Back',
                     command = lambda:[backStudyset(canvas)])
    titlePage.pack()
    termlbl.pack()
    termbox.pack()
    deflbl.pack()
    defbox.pack()
    addbtn.pack()
    backbtn.pack()
def backStudyset(canvas):
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "a")
    f.write("\n")
    f.close()
    studysetMenu(canvas)
def addData2(term, definition, window):
    '''
    Appends a term and definition onto studysets.csv, pulling them from entries 
    '''
    term = term.get()
    definition = definition.get()
    if (term == '') or (term.isspace()):
        messagebox.showerror("Error", "Term Field can not be blank")
    elif (definition == '') or (definition.isspace()):
        messagebox.showerror("Error", "Definition Field can not be blank")
    else:
        folder = os.getcwd()
        file = folder + "\\Studysets.csv"
        f = open(file, "a")
        f.write("|" + term + "|" + definition)
        f.close()
        addFlashcard2(window)
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
    canvas_height_percentage = 30  # Height as a percentage of the window height
    canvas_width_percentage2 = 70
    canvas_width_percentage3 = 50
    canvas_height_percentage3 = 10
    canvas_height_percentage4 = 30
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_width2 = percentageWindow(canvas_width_percentage2, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas_width3 = percentageWindow(canvas_width_percentage3, window_width)
    canvas_height3 = percentageWindow(canvas_height_percentage3, window_height)
    canvas_height4 = percentageWindow(canvas_height_percentage4, window_height)
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
    canvas.create_window((canvas_width3, canvas_height4), window = frame4, anchor = CENTER)
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
                     command = lambda:[save(termEntry, defEntry, num, canvas),toggle_scrollbar(scrollbar)])
    savebtn.pack()
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[removeMenu(canvas),toggle_scrollbar(scrollbar)])
    backbtn.pack()
    removebtn = Button(frame2, text = "Remove Entire Studyset",
                       command = lambda:[removeLine(num),toggle_scrollbar(scrollbar), removeMenu(canvas)])
    removebtn.pack()
def checkValid(term, definition):
    '''
    Checks if the term and definition boxes are empty
    if they are return false, if they have data return true
    '''
    for i in range(len(term)):
        t = term[i].get()
        d = definition[i].get()
        if (t =='') or (t.isspace()):
            messagebox.showerror("Error", "Term field can not be empty")
            return False
        elif (d=='') or (d.isspace()):
            messagebox.showerror("Error", "Definition field can not be empty")
            return False
        else: 
            continue
    return True
def save(term, definition, num,window):
    '''
    appends the term and definition values pulled from entries that the user can edit 
    '''
    title = titles(num)
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "a")
    if checkValid(term, definition) == True:
        file.write(title)
        for i in range(len(term)):
            t = term[i].get()
            d = definition[i].get()
            file.write("|" + t + "|" + strip(d))
        file.write("\n")
        file.close()
        removeLine(num)
        removeMenu(window)
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
            filew.write(strip(line)+"\n")
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

    titlelbl = Label(frame, text = "Add prexisitng studysets, through a csv")
    stepslbl = Label(frame, text = "Please note there must be a | between each term and definition\n Example: title|term|definition|term2|definition2")

    addbtn = Button(frame, text = 'Add',
                    command = lambda:[callFile(canvas)])
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[studysetMenu(canvas)])
    titlelbl.pack()
    stepslbl.pack()
    addbtn.pack()
    backbtn.pack()
def callFile(window):
    '''
    Opens a dialogue box, if the user selects a file that is not a csv it will not be allowed
    '''
    file=fd.askopenfilename() 
    if file != '':
        if file[-3:] == 'csv':
            addCsv(file)
            studysetMenu(window)
        else:
            messagebox.showinfo("ERROR", "Only csvs are allowed")
def addCsv(file):
    '''
    reads the csv that the user inputted and appends it onto the studysets.csv that the programs reads
    '''
    file = open(file, "r")
    text = file.readlines()
    file.close()
    studysets = os.getcwd() + "\\Studysets.csv"
    file = open(studysets, "a")
    for i in range(len(text)):
        file.writelines(text[i])
    file.writelines("\n") 
# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu(root)