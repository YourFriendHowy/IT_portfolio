```python
# Matthew Howard
# 0559162
# Program 4
# COMS-170-01: Winter 2025
# Due: 2/28/25
# Program 4 - A simple loop program that uses an imported library (random) to create addition 
# equations for the user to solve and decide to continue or end the program.
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# proceed              String       Saves user input to continue
# randInt1             integer      Saves first random integer using "random" library
# randInt2             Integer      Saves seconf random integer using "random" library
# i                    Integer      Saves sum of both random integers
# userSum              Integer      Saves user answer input to equation. 

import random

proceed = 'y'


while proceed == 'Y' or proceed == 'y':
    randInt1 = random.randint(20,29)
    randInt2 = random.randint(20,29)
    i = randInt1 + randInt2    
    userSum = int(input(f"What is the sum of {randInt1} + {randInt2}?\n"))
    if userSum == i:
        print("Correct!")
        proceed = input("Continue: Y or N?\n")
    else:
        print("Incorrect!")
        proceed = input("Continue: Y or N?\n")

print("Thanks for using this addition practice program!")

# Add Output of final program as Comments

# What is the sum of 22 + 22?
# 44
# Correct!
# Continue: Y or N?
# y
# What is the sum of 21 + 28?
# 49
# Correct!
# Continue: Y or N?
# y
# What is the sum of 24 + 20?
# 44
# Correct!
# Continue: Y or N?
# n
# Thanks for using this addition practice program!
```