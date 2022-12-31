""""
Dr. Angela's 100 days 100 Python Practice Challenge

Tip calculator

Calculate the tips based on the original bill and calculate the splitting bill.
This challenge contain the calculation syntax and basic math
This challenge also present the way to perform variable in printing by adding a f in front of statement.
---
This lead me to a question: How do I prevent user not input correct data?

"""
import time
print("Welcome to tip calculator")
#Collect basic information
bill = float(input("How much is the bill?"))
tip = float(input("What percentage of tip do you want to pay?"))
#Calculation of bill amount
total_bill = bill + (bill*(tip*(0.01)))
print(f"The total amount of bill is $ {total_bill}")
#Collect and calculate 
split=int(input("How many people are splitting bill?"))
each_person_payment=total_bill/split
time.sleep(1)
print(f"Each person need to pay {each_person_payment} dollars." )