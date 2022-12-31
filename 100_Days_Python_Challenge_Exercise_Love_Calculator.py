"""""
Dr.Angela's Python Exercise-Love calculator
To find the input letter in preset dataset and output as number
Counts the preset dataset letter
inserting the value in the string don't forget to add an f in front of statement.
"""""

print("Welcome to the Love Calculator!")
name1=input("What is your name? \n")
name2=input("What is their name? \n")

conbined_string = name1+name2
lowercasestring= conbined_string.lower()

t = lowercasestring.count("t")
r = lowercasestring.count("r")
u = lowercasestring.count("u")
e = lowercasestring.count("e")

true= t+r+u+e
l = lowercasestring.count("l")
o = lowercasestring.count("o")
v = lowercasestring.count("v")
e = lowercasestring.count("e")
love= l+o+v+e

love_score = str(true) + str(love)

if (love_score<10) or (love_score>90):
    print(f"Your love score is {love_score}, you go together like cake.")
elif (love_score>=40) or (love_score<=50):
    print(f"Your love score is {love_score}, you guys are alright.")
else:
    print(f"Your love score is {love_score}.")
