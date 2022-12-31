""""
Dr. Angela's 100 days 100 Python Practice Challenge

Create a Band name generator by asking user two simple questions

This could be a good toolbox and memo for not capable to memorise the simple syntax and function person like me.
---
This include an input, print, sleep and combination function
In addition, we import time library to fulfill the delay(sleep) function.
"""
import time
#Greeting
print("Welcome to Band name generator.")
#First question
print("Please tell us...")
city=input("Where do you live?")
#Second question
animal=input("What is your favourite animal?")
#Add some lapsing time for fun
time.sleep(1)
print("Calculating...")
time.sleep(3)
################# Final result #################
print("Your band name can be "+ city + " " + animal)

