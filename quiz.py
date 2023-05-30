from tkinter import * 
from tkinter.ttk import *
import csv
import os
from os.path import exists
import random
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
    halfLength = len(questions)/2
    if type(halfLength) == float:
        halfLength = round(halfLength)
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
    halfLength = len(trueOrFalse)/2
    if type(halfLength) == float:
        halfLength = round(halfLength)
    for i in range(int(halfLength)):
        randomInteger = random.choice(trueOrFalse)
        trueOrFalse.remove(randomInteger)
        trueOrFalseWrong.append(randomInteger)
    for j in range (len(trueOrFalse)):
        trueOrFalseQuestion.update({terms[trueOrFalse[j]] : definitions[trueOrFalse[j]]})
    for k in range (len(trueOrFalseWrong)):
        randomElement = random.randint(0, len(definitions)-1)
        excludedElement = trueOrFalseWrong[k]
        while randomElement == excludedElement:
            randomElement = random.choice(trueOrFalseWrong)
        trueOrFalseWrongQuestion.update({terms[trueOrFalseWrong[k]] : definitions[randomElement]})
        return trueOrFalseQuestion, trueOrFalseWrongQuestion
def makeMultipleChoiceQuestions(dividedQuestions, qt):
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
    multipleChoiceQuestions = {}
    print(multipleChoice)
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
    print(multipleChoiceQuestions)
    return multipleChoiceQuestions


td = openFile()
td2 = seperateTermsDefinitions(td)
splitedQuestions = splitQuestions(td2)
questionTF = makeTrueOrFalseQuestions(splitedQuestions, td2)
questionMC = makeMultipleChoiceQuestions(splitedQuestions, td2)

def quizMenu():
    # Toplevel object which will be treated as a new window
    quizMenu = Toplevel(root)

    quizMenu.title('Quiz Home Menu')

    quizMenu.attributes('-fullscreen', True)

    title = "Quiz Menu"
    titlelbl = Label(quizMenu, text = title)
    root.withdraw()  # closes the root window

def homeMenu():
    title = "Studylet"
    titlelbl = Label(root, text = title)
    exitbtn = Button(root, text = 'Exit',
                command = root.destroy)#Exit 
    quizbtn = Button(root, text = 'Quiz',
                    command = lambda:[quizMenu()])
    
    quizbtn.place(anchor = CENTER, relx = 0.5, rely = 0.5)

    # calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
    mainloop()

root = Tk()

root.title("Studylet")
root.attributes('-fullscreen', True)

homeMenu()