import csv
import os
import random
def openFile():
    fileName = os.getcwd() + '\\Studylet\\test.csv'
    file = open(fileName, "r")
    text = file.readline()
    delimeter = "|"
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
    multipleChoice, trueOrFalse = dividedQuestions
    terms, definitions = qt
    print(dividedQuestions)
    halfLength = len(trueOrFalse)/2
    if type(halfLength) == float:
        halfLength = round(halfLength)
    #for i in range(int(halfLength)):

def makeMultipleChoiceQuestions(dividedQuestions, qt):
    multipleChoice, trueOrFalse = dividedQuestions
td = openFile()
td2 = seperateTermsDefinitions(td)
splitedQuestions = splitQuestions(td2)
makeTrueOrFalseQuestions(splitedQuestions, td2)

