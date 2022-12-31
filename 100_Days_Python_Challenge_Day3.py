"""
Dr. Angela's 100 days 100 Python Practice Challenge
Treasure land: A simple interactive RPG.
Using if, elif and else statement to present the game effect.
In addition, ASCII art is also utilised in the game. source: https://ascii.co.uk/art
Combination of  if cycle.
---
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
---

"""
print("Welcome to treasure island.\n" )
print("There is a treasure on the island and this is the last three steps to find the treasure.")
first_step = input("Please choose you are going to left or right?").lower() #in case someone input Left or Right
if first_step == "left":
    print("You're safe.")
    second_step = input("Please choose you are going to left or right?").lower()
    if second_step == "right":
        print("You are safe.")
        third_step = input("Please choose you are going to left, middle or right?").lower()
        if third_step == "right":
            print("You are safe. And Congratulation you got the treasure.")
        elif third_step == "middle":
            print("You straight to a hole. Game Over.")
        else:
            print("Game Over.")
else:
    print("Game Over.")

