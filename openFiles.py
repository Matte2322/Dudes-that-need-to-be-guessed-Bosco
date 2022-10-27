#students
with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/student.txt/freshmen.txt', 'r') as students:
    freshlist = [freshlist.rstrip() for freshlist in students]

#teachers
with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/teachers.txt/academics.txt', 'r') as academic:
    academics = [academics.rstrip() for academics in academic]

with open('/home/doormat/Documents/Dudes that need to be guessed Bosco/teachers.txt/techteachers.txt', 'r') as tech:
    techs = [techs.rstrip() for techs in tech]


