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
        randomStudentSophomore = random.choice(sophomoreListCSEE)
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
  guesses = 0
  iForgor = input("Sorry, what is your tech again?: ")
  if iForgor == 'CSEE':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/CSEE/juniors', 'r') as techJuniors:
        juniorsListCSEE = [juniorsListCSEE.rstrip() for juniorsListCSEE in techJuniors]
        randomStudentJuniors = random.choice(juniorsListCSEE)
        answer = input(f'Is your name {randomStudentJuniors}?: ')
        if answer == 'y' or answer=='yes':
          print(
            f"Your name is {randomStudentJuniors} and it took me {guesses} guess(es) to find your name. Your tech is CSEE btw :>. Just letting you know that you're a junior." 
            )
          break
        else:
          continue
  elif iForgor == 'IDEA':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/IDEA/juniors', 'r') as techJuniors1:
        juniorsListIDEA = [juniorsListIDEA.rstrip() for juniorsListCSEE in techJuniors1]
        randomStudentJuniors1 = random.choice(juniorsListIDEA)
        answer = input(f'Is your name {randomStudentJuniors1}?: ')
        if answer == 'y' or answer == 'yes':
          print(f"Yes, your name is {randomStudentJuniors1} and it took me {guesses} to find it. You're in the technology of IDEA and a junior.")
          break
        else:
          continue
  elif iForgor == 'MAT':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/MAT/juniors', 'r') as techJuniors2:
        juniorsListMAT = [juniorsListMAT.rstrip() for juniorsListMAT in techJuniors2]
        randomStudentJuniors2 = random.choice(juniorsListMAT)
        answer = input(f"Is your name {randomStudentJuniors2}?: ")
        if answer == 'yes' or answer == 'y':
          print(f'Your name is {randomStudentJuniors2} and you belong in the technology MAT as a junior. Took me {guesses} guess(es) to figure you out.')
          break
        else:
          continue
  elif iForgor == 'MSET':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/MSET/juniors', 'r') as techJuniors3:
        juniorsListMSET = [juniorsListMSET.rstrip() for juniorsListMSET in techJuniors3]
        randomStudentJunior3 = random.choice(juniorsListMSET)
        answer = input(f'Is your name {randomStudentJunior3}?: ')
        if answer == 'yes' or answer == 'y':
          print(f'Okay, your name is {randomStudentJunior3} while it took me {guesses} guess(es) to guess your name and you\'re in the technology MSET. You\'re a junior, too. So I guess a W?')
          break
        else:
          continue
  elif iForgor == "BMET":
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/BMET/juniors', 'r') as techJuniors4:
        juniorsListBMET = [juniorsListBMET.rstrip() for juniorsListBMET in techJuniors4]
        randomStudentJunior4 = random.choice(juniorsListBMET)
        answer = input(f"Is your name {randomStudentJunior4}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"Your name is {randomStudentJunior4} and it took me {guesses} guess(es) to determine your name. You're a junior while being in BMET.")
          break
        else:
          continue
  elif iForgor == "ACE":
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1 
      with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/tech.txt/ACE/juniors', 'r') as techJuniors5:
        juniorsListACE = [juniorsListBMET.rstrip() for juniorsListBMET in techJuniors5]
        randomStudentJunior5 = random.choice(juniorsListACE)
        answer = input(f"Is your name {randomStudentJunior5}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"Your name is {randomStudentJunior5} and it took me {guesses} guess(es) to determine your name. You're a junior while being in ACE.")
          break
        else:
          continue

def seniorsFind():
  guesses = 0
  iForgor = input("Sorry, I forgor your tech, please input it again 😅: ")
  if iForgor == 'CSEE':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses +=1 
      with open('/home/doormat/Documents/Tech-Guessing-Game/Techs.txt/CSEE/senior', 'r') as techseniors:
        seniorListCSEE =[seniorListCSEE.rstrip() for seniorListCSEE in techseniors]
        randomStudentsenior = random.choice(seniorListCSEE)
        answer = input('Is your name ' + randomStudentsenior + "?: ")
        if answer == 'y' or answer=='yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior} and you're in the technology CSEE. You're a senior btw.")
          break
        else:
          continue
  elif iForgor == 'IDEA':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses +=1 
      with open('/home/doormat/Documents/Tech-Guessing-Game/Techs.txt/IDEA/senior', 'r') as techseniors1:
        seniorListIDEA = [seniorListIDEA.rstrip() for seniorListIDEA in techseniors1]
        randomStudentsenior1 = random.choice(seniorListIDEA)
        answer = input('Is your name ' + randomStudentsenior1 + "?: ")
        if answer == 'y' or answer=='yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior1} and you're in the technology IDEA. You're a senior btw.")
          break
        else:
          continue
  elif iForgor == 'MAT':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Tech-Guessiing-Game/Techs.txt/MAT/senior', 'r') as techseniors2:
        seniorListMAT = [seniorListMAT.rstrip() for seniorListMAT in techseniors2]
        randomStudentsenior2 = random.choice(seniorListMAT)
        answer = input(f"Is your name {randomStudentsenior2}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior2} and you're in the technology MAT. You're a senior btw.")
          break
        else: 
          continue
  elif iForgor == 'MSET':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Tech-Guessing-Game/Techs.txt/MSET/senior', 'r') as techseniors3:
        seniorListMSET = [seniorListMSET.rstrip() for seniorListMSET in techseniors3]
        randomStudentsenior3 = random.choice(seniorListMSET)
        answer = input(f"Is your name {randomStudentsenior3}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior3} and you're in the technology MSET. You're a senior btw.")
          break
        else: 
          continue
  elif iForgor == 'BMET':
    while True:
      for wake in range(3):
        time.sleep(0.3) 
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Tech-Guessing-Game/Techs.txt/BMET/senior', 'r') as techseniors4:
        seniorListBMET = [seniorListBMET.rstrip() for seniorListBMET in techseniors4]
        randomStudentsenior4 = random.choice(seniorListBMET)
        answer = input(f"Is your name {randomStudentsenior4}?: ")
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior4} and you're in the technology BMET. You're a senior btw.")
          break
        else: 
          continue
  elif iForgor == 'ACE':
    while True:
      for wake in range(3):
        time.sleep(0.3)
        print('.')
      guesses+=1
      with open('/home/doormat/Documents/Tech-Guessing-Game/Techs.txt/ACE/senior', 'r') as techseniors5:
        seniorListACE = [seniorListACE.rstrip() for seniorListACE in techseniors5]
        randomStudentsenior5 = random.choice(seniorListACE)
        answer = input(f'Is your name {randomStudentsenior5}?: ')
        if answer == 'y' or answer == 'yes':
          print(f"It took me {guesses} guess(es) to find your name is {randomStudentsenior5} and you're in the technology ACE. You're a senior btw.")
          break
        else: 
          continue        
          

def academicsFind():
  guesses = 0
  while True:
    for wake in range(3):
      time.sleep(0.5)
      print('.')
    guesses+=1
    randomAcademics = random.choice(academics)
    answer = input(f"Is your name {randomAcademics}?: ")
    if answer == 'yes' or answer == 'y':
      print(f'It took me {guesses} guess(es) to determine your name is {randomAcademics}.')
      break
    else:
      continue

def techsFind():
  guesses = 0
  while True:
    for wake in range(3):
      time.sleep(0.5)
      print('.')
    guesses+=1
    randomTech = random.choice(techs)
    answer = input(f"Is your name {randomTech}?: ")
    if answer == 'yes' or answer == 'y':
      print(f'It took me {guesses} guess(es) to determine your name is {randomTech}.')
      break
    else:
      continue