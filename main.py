import random, time
from unicodedata import category 
from openFiles import *
from sequenceSearch import *

guesses = 0

print("Welcome to the Bosco Loving Guessing Game for KIDS!")
inputRole = input("Are you a (s)tudent or (t)eacher?: ")

def guessingStudentName():
    global guesses
    inputYear = input("What year of high school are you in? (frsh, sp, jn, sn): ")
    if inputYear == 'frsh':
        freshFind()
    elif inputYear == 'sp':
        spFind()
    elif inputYear == 'jn':
        juniorsFind()
    elif inputYear == 'sn':
        seniorsFind() 

def guessingTeacherName():
    global guesses 
    inputTeacher = input("Gotta ask you again, tech or academic?: ")
    if inputTeacher == 'tech':
        techsFind()
    elif inputTeacher == 'academic':
        academicsFind()

def teachers(inputStuff): 
    if inputStuff == 't' or inputStuff == 'T' or inputStuff == 'teacher' or inputStuff == 'Teacher':
        categoryTestDeparments = input("Are you an academic teacher or a tech teacher?: ")
        while True:
            if categoryTestDeparments == "academic teacher" or categoryTestDeparments == 'academic':
                print("You're an academic teacher.")
                break
            elif categoryTestDeparments == 'tech teacher' or categoryTestDeparments == 'tech':
                print("You are a tech teacher.")
                break
        if categoryTestDeparments:
            guessingTeacherName()


def students(inputStuff):
    urAnswer = 'n'
    global guesses

    technologyDepartments = ['ACE', 'CSEE', 'BMET', 'IDEA', 'MAT', 'MSET']
    if inputStuff == 's' or inputStuff == 'S' or inputStuff == 'Student' or inputStuff =='student':
        freshieTest = input("Are you a freshie?: ")
        while urAnswer != 'y':
            if freshieTest == 'y' or freshieTest == 'yes':
                print("Ew, a freshie.")
                break
            for wake in range(3):
                time.sleep(0.5)
                print('.')
            guesses+=1
            randomTech = random.sample(technologyDepartments, k=1)
            urAnswer = input('Is your technology ' + str(randomTech) + "?: ")
            print('Wow, took me ' + str(guesses) + " guess(es) to find what tech you're in ")
        if urAnswer:
            guessingStudentName()


teachers(inputRole)

        
students(inputRole)

