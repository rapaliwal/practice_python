from datetime import datetime
name = input("What's your name?\n")
age = input("What is you age?\n")
age = int(age)
print ("\nYour name is ", name, " and you are ", age, " years old\n")

current_year = datetime.now().year
result_year  = 100 - age
result_year = datetime.now().year + result_year
repeat = input("How many times do you want the message repeated?")
repeat = int(repeat)
print (repeat * 'You will be 100 years old in : {}\n'.format(result_year))
