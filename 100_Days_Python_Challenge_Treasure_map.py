"""
Dr.Angela's 100 days of Python Challenge Exercise
Treasure map. This could be expanded to tic-tac-toe.
By adding another player and mark O and use while loops?
What is while loops and for loops
"""
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print("Please choose the position you want to mark by type horizontal and vertical")
position = input("Where do you want to put the treasure?")


horizonal= int(position[0])
vertical= int(position[1])

map[vertical - 1][horizonal -1] ="x"
print(f"{row1}\n{row2}\n{row3}")
