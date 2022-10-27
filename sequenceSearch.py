import random, time
from openFiles import *

def freshFind():
  guesses = 0
  while True:
    for wake in range(3):
      time.sleep(0.3)
      print('.')
    guesses+=1
    randomStudentFresh = random.choice(freshlist)
    answer = input('Is your name ' + randomStudentFresh + '?: ')
    if answer == 'y' or answer == 'yes':
      print("It took me " + str(guesses) + " guess(es) to find your name is " + randomStudentFresh + " and you have no technologies lol. Typical freshie")
      break
    else:
      continue

def spFind():
  guesses = 0
  iForgor = input("Sorry, I forgor your tech, please input it again 😅: ")
  if iForgor == 'CSEE':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses +=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/CSEE/soph', 'r') as techSophomores:
        sophomoreListCSEE = [sophomoreListCSEE.rstrip() for sophomoreListCSEE in techSophomores]
        randomStudentSophomore = random.choice(techSophomores)
        answer = input('Is your name ' + randomStudentSophomore + "?: ")
        if answer == 'y' or answer=='yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore} and you're in the technology CSEE. You're a sophomore btw.")
          break
        else:
          continue
  elif iForgor == 'IDEA':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses +=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/IDEA/soph', 'r') as techSophomores1:
        sophomoreListIDEA = [sophomoreListIDEA.rstrip() for sophomoreListIDEA in techSophomores1]
        randomStudentSophomore1 = random.choice(sophomoreListIDEA)
        answer = input('Is your name ' + randomStudentSophomore1 + "?: ")
        if answer == 'y' or answer=='yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore1} and you're in the technology IDEA. You're a sophomore btw.")
          break
        else:
          continue
  elif iForgor == 'MAT':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/MAT/soph', 'r') as techSophomores2:
        sophomoreListMAT = [sophomoreListMAT.rstrip() for sophomoreListMAT in techSophomores2]
        randomStudentSophomore2 = random.choice(sophomoreListMAT)
        answer = input(f"Is your name {randomStudentSophomore2}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore2} and you're in the technology MAT. You're a sophomore btw.")
          break
        else: 
          continue
  elif iForgor == 'MSET':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/MSET/soph', 'r') as techSophomores3:
        sophomoreListMSET = [sophomoreListMSET.rstrip() for sophomoreListMSET in techSophomores3]
        randomStudentSophomore3 = random.choice(sophomoreListMSET)
        answer = input(f"Is your name {randomStudentSophomore3}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore3} and you're in the technology MSET. You're a sophomore btw.")
          break
        else: 
          continue
  elif iForgor == 'BMET':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/BMET/soph', 'r') as techSophomores4:
        sophomoreListBMET = [sophomoreListBMET.rstrip() for sophomoreListBMET in techSophomores4]
        randomStudentSophomore4 = random.choice(sophomoreListBMET)
        answer = input(f"Is your name {randomStudentSophomore4}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore4} and you're in the technology BMET. You're a sophomore btw.")
          break
        else: 
          continue
  elif iForgor == 'ACE':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/ACE/soph', 'r') as techSophomores5:
        sophomoreListACE = [sophomoreListACE.rstrip() for sophomoreListACE in techSophomores5]
        randomStudentSophomore5 = random.choice(sophomoreListACE)
        answer = input(f'Is your name {randomStudentSophomore5}?: ')
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentSophomore5} and you're in the technology ACE. You're a sophomore btw.")
          break
        else: 
          continue        

def juniorsFind():
  pass

def seniorsFind():
  pass

def academicsFind():
  pass

def techsFind():
  pass