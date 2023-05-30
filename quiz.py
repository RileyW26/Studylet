import csv
import os
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

from tkinter import * 
from tkinter.ttk import *

# create main window 
root = Tk()

root.title("Text")
root.attributes('-fullscreen', True)

# Labe lis what output will be 
# show on window
#label = Label(root, text = "Hello World !").pack()

def newWindow():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(root)

    newWindow.title("new")

    newWindow.attributes('-fullscreen', True)

    root.withdraw()


btn = Button(root, text = 'Exit',
             command = root.destroy)#Exit 
studysetbtn = Button(root, text = 'Study sets',
                     command = lambda:[newWindow()])
btn.pack(side = 'right')
studysetbtn.pack(side = 'left')
# calling mainloop method which is used when you rapplication is ready to run and it tells the code to keep displaying
mainloop()