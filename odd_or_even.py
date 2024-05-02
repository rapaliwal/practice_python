num = int(input("Please input first number: \n"))
den = int(input("Please input second number to check dibisibility: \n"))

if num % den == 0:
    print (f'{num} is perfectly divisble by {den}!')
else:
    print (f'{num} is not perfectly divisble by {den}!')

