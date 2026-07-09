# creating a number guessing game 
# let the user guess a number between 1 and 100
# print invalid input if we got valueError
# print "too low" if the user input less than the computer guess
# print "too high" if the user input more than the computer guess
# break the loop at the end


import random
number = random.randint (1,100)

while True:
    try:
      guessing = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print ("invalid input")
        continue
    if guessing > number:
      print ("too high")
    elif guessing < number :
      print ("too low")
    else :
     print("you got it")
    break