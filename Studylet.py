from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import csv
import os
from os.path import exists
import random
import time
from tkinter import filedialog as fd 
def seperateTermsDefinitions(termsAndDefinitionsValues):
    '''
    This function takes a list of the title, terms and definitions

    Sorts the terms and definitions into two seperate lists, and returns the two lists, discarding the title
    
    '''
    terms = []#declare list
    definitions = []#declare list
    for i in range (1, len(termsAndDefinitionsValues)):#start from 1 to ignore title
        if i % 2 == 0: #if index is even, it is a definition
            definitions.append(termsAndDefinitionsValues[i])
        elif i % 2 != 0: #if index is even, it is a term
            terms.append(termsAndDefinitionsValues[i])
    return terms, definitions

def splitQuestions(questionTerms):
    '''
    Takes the two lists terms and definitions

    splits the number of terms into two
    
    
    
    '''
    terms, definitions = questionTerms
    questions = []
    trueOrFalseQuestions = []
    for i in range(len(terms)):
        questions.append(i)
    halfLength = len(questions)/2
    for i in range(int(halfLength)):
        randomInteger = random.choice(questions)
        questions.remove(randomInteger)
        trueOrFalseQuestions.append(randomInteger)
    return questions, trueOrFalseQuestions

def makeTrueOrFalseQuestions(dividedQuestions, qt):
    trueOrFalseWrong = []
    trueOrFalseQuestion = {}
    trueOrFalseWrongQuestion = {}
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
    definitions[-1] = (definitions[-1])[:-1]
    halfLength = len(trueOrFalse)//2

    for i in range(int(halfLength)):
        randomInteger = random.choice(trueOrFalse)
        trueOrFalse.remove(randomInteger)
        trueOrFalseWrong.append(randomInteger)
    for j in range (len(trueOrFalse)):
        trueOrFalseQuestion.update({terms[trueOrFalse[j]] : [definitions[trueOrFalse[j]], "true"]})

    for k in range (len(trueOrFalseWrong)):
        randomElement = random.randint(0, len(definitions)-1)
        excludedElement = trueOrFalseWrong[k]
        while randomElement == excludedElement:
            randomElement = random.choice(trueOrFalseWrong)
        trueOrFalseWrongQuestion.update({terms[trueOrFalseWrong[k]] : [definitions[randomElement],"false"]})
    return trueOrFalseQuestion, trueOrFalseWrongQuestion
def makeMultipleChoiceQuestions(dividedQuestions, qt):
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
    definitions[-1] = (definitions[-1]).strip() #removes \n from last list element
    multipleChoiceQuestions = {}
    for i in range(len(multipleChoice)):
        multipleAnswers = []
        definitionNum = []
        for k in range(len(definitions)):
            definitionNum.append(k)
        multipleAnswers.append(definitions[multipleChoice[i]])
        temp = multipleChoice[i]
        definitionNum.remove(temp)
        for j in range(3): #repeat 3 times for 3 fake answers
            randomNumber = random.choice(definitionNum)
            definitionNum.remove(randomNumber)
            multipleAnswers.append(definitions[randomNumber])
        multipleChoiceQuestions.update({terms[multipleChoice[i]] : multipleAnswers })
    return multipleChoiceQuestions
def percentageWindow(percentage, total_length):
    return int(percentage / 100 * total_length)
def quizChecker(termsAndDefinitions):
    '''
    Checks if the amount of terms of a study set is less than four
    
    If it is not, 
    
    It will pop up a message box notifying the user that there needs to be atleast 4 pairs of terms and definitions

    it will return True so in quiz_window, it returns to avoid any errors
    '''
    if len(termsAndDefinitions[0]) < 4:
        messagebox.showinfo("Quiz Requirements", "To start a quiz with this study set, make sure there is atleast 4 pairs of terms and definitions")
        return True
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
                        command = lambda:[homeMenu(canvas), toggle_scrollbar(scrollbar)])
    
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
        termbutton.config()
        termbutton.pack()
        homebtn2.pack()
        nextbtn.pack()    
    else:
        termbutton.config()
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
def frames(canvas, window):
    frame = Frame(canvas)
    # Calculate the pixel values based on percentages
    canvas_width_percentage = 50  # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    canvas_width = percentageWindow(canvas_width_percentage, window_width)
    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    return frame
def quiz_window(window, num):
    #Visuals
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[int(num)]
    value = line.split("|")
    td2 = seperateTermsDefinitions(value)
    splitedQuestions = splitQuestions(td2)
    quizCheck = quizChecker(td2)
    if quizCheck == True:
        return
    questionTF, questionTFWrong = makeTrueOrFalseQuestions(splitedQuestions, td2)
    questionsTF = {**questionTF, **questionTFWrong}
    questionMC = makeMultipleChoiceQuestions(splitedQuestions, td2)
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    score = 0 #Will be added to when a correct answer is submitted and compared with the fully correct score to find percentage
    fullyCorrectScore = len(list(questionMC)) + len(list(questionTF)) + len(list(questionTFWrong)) #Adding len of questionMC, questionTF, questionTFWrong to find total score for the quiz
    start = time.time() #Start timer
    while questionMC != {}:
        frame = frames(canvas, window)

        title = "Quiz"
        titlelbl = Label(frame, text = title)
        titlelbl.pack()
    
        dictQuestionMC = dict(questionMC) #Temporary variable to store questionMC, as when we pop questions from questionMC, we need to still be able to call the answers

        question = random.choice(list(questionMC)) #random term to act as question
        questionMC.pop(question)
        

        answer = dictQuestionMC.get(question)
        correctAnswer = answer[0]
        random.shuffle(answer)
        questionDescription = Label(frame, text = "Multiple Choice: Choose the matching definition")
        questionDescription.pack()
            

        questionDisplay = Label(frame, text = question)
        questionDisplay.pack()
        button_pressed = BooleanVar()
        answer_submitted = StringVar()
        answerOneBtn = Button(frame, text = answer[0], command=lambda id = answer[0]:[answer_submitted.set(id), button_pressed.set(True)])
        answerTwoBtn = Button(frame, text = answer[1], command=lambda id = answer[1]:[answer_submitted.set(id), button_pressed.set(True)])
        answerThreeBtn = Button(frame, text = answer[2], command=lambda id = answer[2]:[answer_submitted.set(id), button_pressed.set(True)])
        answerFourthBtn = Button(frame, text = answer[3], command=lambda id = answer[3]:[answer_submitted.set(id), button_pressed.set(True)])
        answerOneBtn.pack()
        answerTwoBtn.pack()
        answerThreeBtn.pack()
        answerFourthBtn.pack()
        frame.wait_variable(button_pressed)
        if answer_submitted.get() == correctAnswer:
            score += 1
        frame.destroy()
    while questionsTF !={}:
        frame = frames(canvas, window)


        dictQuestionsTF = dict(questionsTF) #Temporary variable to store questionMC, as when we pop questions from questionMC, we need to still be able to call the answers

        question = random.choice(list(questionsTF)) #random term to act as question
        questionsTF.pop(question)
        

        answer = dictQuestionsTF.get(question)
        correctAnswer = answer[1]
        title = "Quiz"
        titlelbl = Label(frame, text = title)
        titlelbl.pack()
        questionDescription = Label(frame, text = "True or False: Decide whether the definition is true or false")
        questionDescription.pack()
        questionDisplay = Label(frame, text = question)
        questionDisplay.pack()
        answerDisplay = Label(frame, text = answer[0])
        answerDisplay.pack()
        button_pressed = BooleanVar()
        answer_submitted = StringVar()
        trueBtn = Button(frame, text = "True", command=lambda id = "true":[answer_submitted.set(id), button_pressed.set(True)])
        falseBtn = Button(frame, text = "False", command=lambda id = "false":[answer_submitted.set(id), button_pressed.set(True)])
        trueBtn.pack()
        falseBtn.pack()
        frame.wait_variable(button_pressed)
        if answer_submitted.get() == correctAnswer:
            score += 1
        frame.destroy()
    end = time.time()
    timeCompletion = end-start
    scorePercentage = str((score/fullyCorrectScore)*100)
    leaderboard(canvas, fileName, num, timeCompletion, scorePercentage)
def updateleaderboardEdit(num):
    leaderboardFile = os.getcwd() + "\\StudyletLeaderboard.csv"
    temp_file = "temp.csv"  # Temporary file to store modified data
    with open(leaderboardFile, 'r') as file:
        lines = file.readlines()  # Read all lines from the CSV file

    lineSeperatedList = lines[num].split("|")
    title = lineSeperatedList[0]
    if len(lineSeperatedList) == 1:
        lines[num] = title
    else: 
        lines[num] = title + "\n"
    with open(temp_file, 'w') as file:
        file.writelines(lines)  # Write all modified lines to the temporary file

    # Replace the original file with the modified file

    os.remove(leaderboardFile)
    os.rename(temp_file, leaderboardFile)
def updateLeaderboardAdd(title):
    leaderboardFile = os.getcwd() + "\\StudyletLeaderboard.csv"
    with open(leaderboardFile, 'a') as file:
        file.write(title + "\n")
def updateLeaderboard(leaderboardFile, num, time, score):
    temp_file = "temp.csv"  # Temporary file to store modified data
    with open(leaderboardFile, 'r') as file:
        lines = file.readlines()  # Read all lines from the CSV file

    # Modify the desired line with the new data
    scoreEntry = score + "|" + str(time)
    lines[num] = lines[num].strip() + "|" + scoreEntry + "\n"
    lineSeperatedList = lines[num].split("|")
    lineSeperatedList[-1] = (lineSeperatedList[-1]).strip()
    title = lineSeperatedList[0]
    scores, times = seperateTermsDefinitions(lineSeperatedList)
    orderedScores, orderedTimes = bubbleSort(scores, times)
    lines[num] = title
    for i in range(len(orderedScores)):
        lines[num] = lines[num].strip() + "|" + orderedScores[i] + "|" + orderedTimes[i] +"\n"
    with open(temp_file, 'w') as file:
        file.writelines(lines)  # Write all modified lines to the temporary file

    # Replace the original file with the modified file

    os.remove(leaderboardFile)
    os.rename(temp_file, leaderboardFile)
    return orderedScores, orderedTimes
def bubbleSort(arr, secondArr):
    #outer loop neeeds to run one time less than the length of the list
    #this loop dictates the number of times we push elements to the end
    for i in range(len(arr)-1):
        # innner loop responsible for swaps
        for j in range(len(arr) - i - 1):
            #swap element
            if float(arr[j]) < float(arr[j+1]): #If not float(), would order it based on lexicographic order
                temp = arr[j] #hold left variable
                tempTwo = secondArr[j]
                arr[j] = arr[j+1]#replaces left with right
                secondArr[j] = secondArr[j+1]#replaces left with right
                arr[j+1] = temp#replaces right with left
                secondArr[j+1] = tempTwo
    secondArrModified = bubbleSortTime(arr, secondArr)
    return arr, secondArrModified
def bubbleSortTime(arr, secondArr):
    for i in range(len(arr)-1):
        # innner loop responsible for swaps
        for j in range(len(arr) - i - 1):
            #swap element
            if float(arr[j]) == float(arr[j+1]): #If not float(), would order it based on lexicographic order
                if float(secondArr[j]) > float(secondArr[j+1]):
                    tempTwo = secondArr[j]
                    secondArr[j] = secondArr[j+1]#replaces left with right
                    secondArr[j+1] = tempTwo
    return secondArr
def leaderboard(window, fileName, num, time, score):
    leaderboardFile = os.getcwd() + "\StudyletLeaderboard.csv"
    orderedScores, orderedTimes = updateLeaderboard(leaderboardFile, num, time, score)
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    frame = Frame(canvas)
    canvas_width_percentage = 50  # Width as a percentage of the window width
    canvas_height_percentage = 50  # Height as a percentage of the window height
    # Calculate the pixel values based on percentages
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    
    canvas_width = percentageWindow(canvas_width_percentage, window_width)

    canvas_height = percentageWindow(canvas_height_percentage, window_height)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

    title = "Quiz Leaderboard"
    titlelbl = Label(frame, text = title)
    titlelbl.pack()
    tree = Treeview(frame)
    tree["columns"] = ("Score", "Time")
    tree.column("#0", width=0, stretch=NO)  # Adjust the width of the default column
    # Define column headings
    tree.heading("#0", text="", anchor=W)  # Specify an empty string for the default column heading
    tree.heading("Score", text="Score")
    tree.heading("Time", text="Time")
    tree.bind("<ButtonPress-1>", disable_column_resizing)
    for i in range(len(orderedScores)):
    
    # Insert data rows
      tree.insert("", END, values=(str(round(float(orderedScores[i]), 2)) + "%", str(round(float(orderedTimes[i]), 2)) + " " + "seconds" ))
      
    
    # Pack the Treeview widget
    tree.pack()
    backbtn = Button(frame, text = 'Back',command = lambda:[homeMenu(canvas)])
    backbtn.pack()
def leaderboardFileCreation(fileName):
    leaderboardFile = os.getcwd() + "\StudyletLeaderboard.csv"
    isFile = os.path.isfile(leaderboardFile)
    file = open(fileName, "r")
    text = file.readlines()
    if isFile == False:
        fileLB = open(leaderboardFile, "w")
        for i in range(len(text)):
            line = text[i]
            value = line.split("|")
            title = value[0]
            fileLB.writelines(title + "\n")
        fileLB.close()
def disable_column_resizing(event):
    # Prevent the Treeview widget from resizing columns
    return "break"

def playQuizzesMenu(window):
    folder = os.getcwd()
    file = folder + "\\Studysets.csv"
    f = open(file, "r")
    lines = len(f.readlines())
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

    # Create a Scrollbar widget
    #scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    #scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    #canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)
    quizTitle = Label(frame, text = "Quizzes")
    quizTitle.pack()
    quizDescription = Label(frame, text = "Choose a study set to create a quiz for. The study set must have atleast 4 terms to create a quiz")
    quizDescription.pack()
    backbutton = Button(frame, text = "back",
                        command = lambda:[homeMenu(canvas)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[quiz_window(canvas, id)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
    f.close()
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
                        command = lambda:[flashcardList(canvas)])
    quizbtn = Button(frame, text = 'Quiz',
                    command = lambda:[playQuizzesMenu(canvas)])
    studysetbtn = Button(frame, text = "Manage Studysets",
                         command = lambda:[studysetMenu(canvas)])
    titlelbl.pack()
    flashcardbtn.pack()
    quizbtn.pack()
    studysetbtn.pack()
    exitbtn.pack()
    fileName = os.getcwd() + "\Studysets.csv"
    leaderboardFileCreation(fileName)
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
    removebtn = Button(frame, text = "Remove/Edit Studysets", command = lambda:[removeMenu(canvas)])
    addto = Button(frame, text = "Add to Existing Studysets", command = lambda:[addToExisting(canvas)])
    add2btn = Button(frame,text = "Adding Prexisting Studysets, through a csv", command = lambda:[addExisting(canvas)])
    backbtn = Button(frame, text = "Back", command = lambda:[homeMenu(canvas)])
    titlelbl.pack()
    addbtn.pack()
    add2btn.pack()
    addto.pack()
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
        if fileExists == True:
            f = open(file, "a")
            f.write(title +"|" + term + "|" + definition)
            f.close()
        else:
            f = open(file, "w")
            f.write(title +"|" + term + "|" + definition)
            f.close()
        addFlashcard2(window, title)
def addFlashcard2(window, title):
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
    titlePage = Label(frame3, text = "Creating Flashcard Set")
    termlbl = Label(frame, text = "Term:")
    termbox = Entry(frame2)
    deflbl = Label(frame, text = 'Definition:')
    defbox = Entry(frame2)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addData2(termbox, defbox, canvas, title)])
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
        addFlashcard2(window, title)
def removeMenu(window):
    '''
    SHows the user a list of the available study sets, clicking on one will bring them to a page where they can edit or remove the entire studyset
    '''    
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
    warninglbl = Label(frame, text = '*Editing or removing an existing studyset will delete the saved leaderboard scores')
    titlelbl.pack()
    warninglbl.pack()
    backbutton = Button(frame, text = "back",
                        command = lambda:[studysetMenu(canvas), toggle_scrollbar(scrollbar)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[removeSet(canvas, id), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()

def addToExisting(window):
    '''
    Shows the user a list of the available study sets, clicking on one will bring them to a page where they can see the list of all available studysets
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

    titlelbl = Label(frame, text = 'Add to an existing studyset')
    warninglbl = Label(frame, text = '*Adding to an existing studyset will delete the saved leaderboard scores')
    titlelbl.pack()
    warninglbl.pack()
    backbutton = Button(frame, text = "back",
                        command = lambda:[studysetMenu(canvas), toggle_scrollbar(scrollbar)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[addTo(canvas, id), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
def addTo(window, num):
    '''
    Where the user can enter information to add to an existing studyset
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
    title = 'Editing "' + titles(num) + '"'
    titlePage = Label(frame3, text = title)
    termlbl = Label(frame, text = "Term:")
    termbox = Entry(frame2)
    deflbl = Label(frame, text = 'Definition:')
    defbox = Entry(frame2)
    addbtn = Button(frame, text = 'Add',
                    command = lambda:[addDataToExisting(termbox, defbox, canvas, num)])
    backbtn = Button(frame2, text = 'Back',
                     command = lambda:[backStudyset(canvas)])
    titlePage.pack()
    termlbl.pack()
    termbox.pack()
    deflbl.pack()
    defbox.pack()
    addbtn.pack()
    backbtn.pack()
def addDataToExisting(term, definition, window, num):
    '''
    will add data taken from entries onto an existing studyset
    '''
    term = term.get()
    definition = definition.get()
    if (term == '') or (term.isspace()):
        messagebox.showerror("Error", "Term Field can not be blank")
    elif (definition == '') or (definition.isspace()):
        messagebox.showerror("Error", "Definition Field can not be blank")
    else:
        fileName = os.getcwd() + "\\Studysets.csv"
        temp_file = "temp.csv" 
        with open(fileName, 'r') as f:
            line = f.readlines()
            line[num] = line[num].strip() + "|" + term + "|" + definition + "\n"
        with open(temp_file, 'w') as file:
            file.writelines(line)


        os.remove(fileName)
        os.rename(temp_file, fileName)
        updateleaderboardEdit(num)
        addTo(window, num)
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
    savebtn = Button(frame4, text = 'Save',
                     command = lambda:[save(termEntry, defEntry, num, canvas),toggle_scrollbar(scrollbar)])
    for i in range(len(defintions)):
        entry2 = Entry(frame2)
        entry2.insert(END, defintions[i])
        entry2.pack()
        defEntry.append(entry2)

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

    if checkValid(term, definition) == True:
        editLine(term, definition, num)
        updateleaderboardEdit(num)
        removeMenu(window)
def editLine(term, definition, num):
    fileName = os.getcwd() + "\\Studysets.csv"
    temp_file = "temp.csv"  # Temporary file to store modified data
    with open(fileName, 'r') as file:
        lines = file.readlines()  # Read all lines from the CSV file

    # Modify the desired line with the new data
    lineSeperatedList = lines[num].split("|")
    lineSeperatedList[-1] = (lineSeperatedList[-1]).strip()
    title = lineSeperatedList[0]
    lines[num] = title
    for i in range(len(term)):
        t = term[i].get()
        d = definition[i].get()
        lines[num] = lines[num].strip() + "|" + t + "|" + strip(d) +"\n"
        file.close()
    with open(temp_file, 'w') as file:
        file.writelines(lines)  # Write all modified lines to the temporary file

    # Replace the original file with the modified file

    os.remove(fileName)
    os.rename(temp_file, fileName)
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
    leaderboardFileName = os.getcwd() + "\\StudyletLeaderboard.csv"
    remove_line_from_csv(leaderboardFileName, num)
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
    leaderboardFile = os.getcwd() + "\\StudyletLeaderboard.csv"
    file = open(studysets, "a")
    for i in range(len(text)):
        file.writelines(text[i])
    file.writelines("\n") 
    fileLB = open(leaderboardFile, "a")
    for i in range(len(text)):
        line = text[i].split("|")
        fileLB.writelines(line[0])
        fileLB.writelines("\n") 
    file.close()
    fileLB.close()
# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu(root)