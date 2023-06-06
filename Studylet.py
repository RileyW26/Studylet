from tkinter import * 
from tkinter.ttk import *
import csv
import os
from os.path import exists
import random
import time
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
    playbtn = Button(frame, text = 'Play flashcard')
    '''
    addbtn = Button(frame, text = 'Add flashcard',
                    command = lambda:[addFlashcard(frame)])
    removebtn = Button(frame, text = 'Remove flashcard',
                       command = lambda:[removeMenu(frame)])
    '''
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[homeMenu(canvas)])
    
    titlelbl.pack()
    playbtn.pack()
    backbtn.pack()
def seperateTermsDefinitions(termsAndDefinitionsValues):
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
def splitQuestions(questionTerms):
    terms, definitions = questionTerms
    questions = []
    trueOrFalseQuestions = []
    for i in range(len(terms)):
        questions.append(i)
    halfLength = len(questions)//2
   
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
def quizChecker():
    pass
def quiz_window(window, num):
    #Visuals
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[int(num)]
    value = line.split("|")
    td2 = seperateTermsDefinitions(value)
    splitedQuestions = splitQuestions(td2)
    quizCheck = quizChecker()
    questionTF, questionTFWrong = makeTrueOrFalseQuestions(splitedQuestions, td2)
    questionsTF = {**questionTF, **questionTFWrong}
    questionMC = makeMultipleChoiceQuestions(splitedQuestions, td2)
    print('questionTF: ', questionTF)
    print('questionTFWrong: ', questionTFWrong)
    print("questionsTF: ", questionsTF)
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    score = 0 #Will be added to when a correct answer is submitted and compared with the fully correct score to find percentage
    print(type(questionTF), type(questionTFWrong))
    fullyCorrectScore = len(list(questionMC)) + len(list(questionTF)) + len(list(questionTFWrong)) #Adding len of questionMC, questionTF, questionTFWrong to find total score for the quiz
    start = time.time() #Start timer
    while questionMC != {}:
        frame = Frame(canvas)
        canvas_width_percentage = 50  # Width as a percentage of the window width
        canvas_height_percentage = 50  # Height as a percentage of the window height
        # Calculate the pixel values based on percentages
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()
        
        canvas_width = percentageWindow(canvas_width_percentage, window_width)

        canvas_height = percentageWindow(canvas_height_percentage, window_height)
        canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

        title = "Quiz"
        titlelbl = Label(frame, text = title)
        titlelbl.pack()
    
        dictQuestionMC = dict(questionMC) #Temporary variable to store questionMC, as when we pop questions from questionMC, we need to still be able to call the answers

        question = random.choice(list(questionMC)) #random term to act as question
        questionMC.pop(question)
        

        answer = dictQuestionMC.get(question)
        correctAnswer = answer[0]
        random.shuffle(answer)
        print("correct: ", correctAnswer)
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
            print("correct") 
            score += 1
        frame.destroy()
    while questionsTF !={}:
        frame = Frame(canvas)
        canvas_width_percentage = 50  # Width as a percentage of the window width
        canvas_height_percentage = 50  # Height as a percentage of the window height
        # Calculate the pixel values based on percentages
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()
        canvas_width = percentageWindow(canvas_width_percentage, window_width)
        canvas_height = percentageWindow(canvas_height_percentage, window_height)
        canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

        dictQuestionsTF = dict(questionsTF) #Temporary variable to store questionMC, as when we pop questions from questionMC, we need to still be able to call the answers

        question = random.choice(list(questionsTF)) #random term to act as question
        questionsTF.pop(question)
        

        answer = dictQuestionsTF.get(question)
        print(question)
        print(answer)
        correctAnswer = answer[1]
        print("correct: ", correctAnswer)
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
            print("correct") 
            score += 1
        frame.destroy()
    end = time.time()
    print('int score: ', score)
    timeCompletion = end-start
    scorePercentage = str((score/fullyCorrectScore)*100)
    print("Time taken to complete the quiz: ", timeCompletion, "seconds")
    print("score: ", scorePercentage + "%")
    leaderboard(canvas, fileName, num)
def leaderboard(window, fileName, num):
    leaderboardFile = os.getcwd() + "\StudyletLeaderboard.csv"
    isFile = os.path.isfile(leaderboardFile)
    file = open(fileName, "r")
    text = file.readlines()
    if isFile == False:
        fileLB = open(leaderboardFile, "w")

    print(text)
    line = text[int(num)]
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
    playbtn = Button(frame, text = 'Play quizzes', command = lambda:[playQuizzesMenu(canvas)])
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[homeMenu(canvas)])
    titlelbl.pack()
    playbtn.pack()
    backbtn.pack()
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
    scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    frame = Frame(canvas)
    canvas.create_window((canvas_width, canvas_height), window=frame, anchor=NW)

    titlelbl = Label(frame, text = 'Remove Available Studysets')
    titlelbl.pack
    backbutton = Button(frame, text = "back",
                        command = lambda:[studysetMenu(canvas), toggle_scrollbar(scrollbar)])
    
    # Placing buttons
    for i in range(lines):
            button = Button(frame, text = titles(i),
                            command = lambda id = i:[quiz_window(canvas, id), toggle_scrollbar(scrollbar)])
            button.pack(side = "top", fill = X)
    backbutton.pack()
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
    titlelbl = Label(frame, text = "Studysets")
    addbtn = Button(frame, text = "Add Studyset", command = lambda:[addstudyset(canvas)])
    removebtn = Button(frame, text = "Remove Studyset", command = lambda:[removeMenu(canvas)])
    backbtn = Button(frame, text = "Back", command = lambda:[homeMenu(canvas)])
    titlelbl.pack()
    addbtn.pack()
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
    titlelbl.pack
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
    Returns a string of all the elements before | in studysets.csv
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
    return int(percentage / 100 * total_length)
def removeSet(window, num):
    window.delete('all')
    window.config(yscrollcommand=None)
   
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
    termlbl = Label(frame, text = 'Terms:')
    deflbl = Label(frame2, text = 'Definitions:')
    termlbl.pack()
    deflbl.pack()
    termEntry = []
    defEntry = []
    for i in range(len(terms)):
        entry = Entry(frame)
        entry.insert(END, terms[i])
        entry.pack()
        termEntry.append(entry)
    for i in range(len(defintions)):
        entry2 = Entry(frame2)
        entry2.insert(END, defintions[i])
        entry2.pack()
        defEntry.append(entry2)
    titlelbl = Label(frame3, text = 'Edit studyset "' + titles(num)+'"')
    titlelbl.pack()
    savebtn = Button(frame3, text = 'Save',
                     command = lambda:[save(termEntry, defEntry, num),toggle_scrollbar(scrollbar),removeLine(num)])
    savebtn.pack()
    backbtn = Button(frame, text = 'Back',
                     command = lambda:[removeMenu(canvas),toggle_scrollbar(scrollbar)])
    backbtn.pack()
    removebtn = Button(frame2, text = "Remove Entire Studyset",
                       command = lambda:[removeLine(num),toggle_scrollbar(scrollbar), removeMenu(canvas)])
    removebtn.pack()
    file.close()
def save(term, definition, num):
    fileName = os.getcwd() + '\\Studysets.csv'
    file = open(fileName, "r")
    text = file.readlines()
    line = text[int(num)]
    print(line)
    print(len(term))
    for i in range(len(term)):
        t = term[i].get()
        d = definition[i].get()
        print(t)
        print(d)
    file.close()
    
def removeLine(num):
    num = num + 1
    fileName = os.getcwd() + '\\Studysets.csv'
    remove_line_from_csv(fileName, num)
def remove_line_from_csv(file_path, line_number):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    filew = open(file_path, 'w', newline = '')
    for index, line in enumerate( lines, start = 1):
        if index != line_number:
            filew.write(line)
    filew.close()
def toggle_scrollbar(scrollbar):
        scrollbar.pack_forget()

# create main window 
root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu(root)