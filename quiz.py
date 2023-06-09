from tkinter import * 
from tkinter.ttk import *
import csv
import os
from os.path import exists
import random
import time
def openFile():
    fileName = os.getcwd() + '\\Studylet\\test.csv'
    file = open(fileName, "r")
    text = file.readline()
    termsAndDefinitions = text.split("|")
    return termsAndDefinitions
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
    print("2: ", questions, trueOrFalseQuestions)
    return questions, trueOrFalseQuestions
def makeTrueOrFalseQuestions(dividedQuestions, qt):
    trueOrFalseWrong = []
    trueOrFalseQuestion = {}
    trueOrFalseWrongQuestion = {}
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
    halfLength = len(trueOrFalse)/2
    if type(halfLength) == float:
        halfLength = round(halfLength)
    for i in range(int(halfLength)):
        randomInteger = random.choice(trueOrFalse)
        trueOrFalse.remove(randomInteger)

    for j in range (len(trueOrFalse)):
        trueOrFalseQuestion.update({terms[trueOrFalse[j]] : definitions[trueOrFalse[j]]})

    for k in range (len(trueOrFalseWrong)):
        randomElement = random.randint(0, len(definitions)-1)
        excludedElement = trueOrFalseWrong[k]
        print(excludedElement)
        while randomElement == excludedElement:
            randomElement = random.choice(trueOrFalseWrong)
        trueOrFalseWrongQuestion.update({terms[trueOrFalseWrong[k]] : definitions[randomElement]})
    print(trueOrFalseQuestion, trueOrFalseWrongQuestion)
    return trueOrFalseQuestion, trueOrFalseWrongQuestion
def makeMultipleChoiceQuestions(dividedQuestions, qt):
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
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

td = openFile()
td2 = seperateTermsDefinitions(td)
print("td2: ", td2)
splitedQuestions = splitQuestions(td2)
questionTF, questionTFWrong = makeTrueOrFalseQuestions(splitedQuestions, td2)
questionMC = makeMultipleChoiceQuestions(splitedQuestions, td2)
print("splitedQuestions: ", splitedQuestions)
print("questionTF: ", questionTF, questionTFWrong)
print('questionMC: ', questionMC)
def percentageWindow(percentage, total_length):
    return int(percentage / 100 * total_length)
def quizMenu(questionTF, questionMC, window):
    # Toplevel object which will be treated as a new window
    
    '''quizMenu = Toplevel(root)

    quizMenu.title('Quiz Home Menu')

    quizMenu.attributes('-fullscreen', True)
'''

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
    title = "Quiz Menu"

    titlelbl = Label(frame, text = title)

    startbtn = Button(frame, text = 'Start', command = lambda:[quiz_window(quizMenu, questionTF, questionMC, canvas)])
    titlelbl.pack()
    startbtn.pack()


def quiz_window(quizMenu, questionTF, questionMC, window):
    #Visuals
    canvas = Canvas(window)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    score = 0
    fullyCorrectScore = len(list(questionMC))
    print(fullyCorrectScore)
    start = time.time()
    while questionMC != {}:
        frame = Frame(canvas)
        canvas_width_percentage = 50  # Width as a percentage of the window width
        canvas_height_percentage = 50  # Height as a percentage of the window height
        canvas_width_percentage2 = 70

        # Calculate the pixel values based on percentages
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()
        
        canvas_width = percentageWindow(canvas_width_percentage, window_width)

        canvas_height = percentageWindow(canvas_height_percentage, window_height)
        canvas.create_window((canvas_width, canvas_height), window=frame, anchor=CENTER)

        title = "Quiz"
        titlelbl = Label(frame, text = title)
        titlelbl.pack()

        listQuestionMC = dict(questionMC)

        question = random.choice(list(questionMC)) #random term to act as question
        questionMC.pop(question)
        

        answer = listQuestionMC.get(question)
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
    end = time.time()
    print('int score: ', score)
    print("Time taken to complete the quiz: ", end-start, "seconds")
    print("score: ", str((score/fullyCorrectScore)*100) + "%")



    
def homeMenu(questionTF, questionMC):
    title = "Studylet"
    titlelbl = Label(root, text = title)
    exitbtn = Button(root, text = 'Exit',
                command = root.destroy)#Exit 
    quizbtn = Button(root, text = 'Quiz', command = lambda:[quizMenu(questionTF, questionMC, root)])
    
    quizbtn.place(anchor = CENTER, relx = 0.5, rely = 0.5)

    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()

root = Tk()


root.title("Studylet")
root.attributes('-fullscreen', True)


homeMenu(questionTF, questionMC)