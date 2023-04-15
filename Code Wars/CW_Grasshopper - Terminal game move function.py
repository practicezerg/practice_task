"""
Terminal game move function
In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated
by the dice two times.
Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return
the new position.
"""

def move(position, roll):
    return position + roll*2

position = 3
roll = 15
res = move(position, roll)
print(res)