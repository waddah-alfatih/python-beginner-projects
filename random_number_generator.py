# taking input from the user ( yes or no)
# generate random number from 1 to 10 if user said yes
# print ( it's okay) and break the loop  if user said no
# any other input print an error message 

import random

while  True :
    choice = input("let's play a game (yes / no) :").lower()
    if choice == "yes" :
        number_1 = random.randint (1,10)
        number_2 = random.randint (1,10)
        print (f"({number_1} , {number_2})")
    elif choice == "no" :
        print ("okay , maybe next time")
        break
    else :
        print ("invalid input")


