import csv
import os
import random
fileName = os.getcwd() + '\\Studylet\\test.csv'
file = open(fileName, "r")
text = file.readline()
delimeter = "|"
termsAndDefinitions = text.split("|")
print(termsAndDefinitions)
terms = []
definitions = []
for i in range (1, len(termsAndDefinitions)):
    if i % 2 == 0:
        definitions.append(termsAndDefinitions[i])
    elif i % 2 != 0: 
        terms.append(termsAndDefinitions[i])
print(terms)
print(definitions)
questions = []
for i in range(len(terms)):
    questions.append(i)
print(questions)
randomInteger = random.randint(0, len(questions)-1)
print(randomInteger)
questions.remove(randomInteger)
print(questions)
if randomInteger == 0:
    print(terms[randomInteger])

elif randomInteger != 0:
    print(terms[randomInteger-1])
#True or false questions