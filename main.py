import random, time 
from openFiles import *
from sequenceSearch import *

answer = 'n'
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
        pass
    elif inputYear == 'sn':
        pass 

def guessingTeacherName():
    pass

def students(inputStuff):
    global answer
    global guesses

    technologyDepartments = ['ACE','CSEE', 'BMET', 'IDEA', 'MAT', 'MSET']
    if inputRole == 's' or inputRole == 'S' or inputRole == 'Student' or inputRole =='student':
        freshieTest = input("Are you a freshie?: ")
        while answer != 'y':
            if freshieTest == 'y' or freshieTest == 'yes':
                print("Ew, a freshie.")
                break
            for wake in range(3):
                time.sleep(0.5)
                print('.')
            guesses+=1
            randomTech = random.choice(technologyDepartments)
            answer = input('Is your technology ' + randomTech + "?: ")
    print('Wow, took me ' + str(guesses) + " guess(es) to find what tech you're in ")
    guessingStudentName()

        
students(inputRole)

