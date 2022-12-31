#Dice roll simulator
import random

#set minimum and maximum
min_val=1
max_val=6

#to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again =="yes" or roll_again =="y":
    print("Rolling the dice...")
    print("The value is " )
    print(random.randint(min_val, max_val))
    roll_again= input("Rolling dice again? If yes, please type yes or y")