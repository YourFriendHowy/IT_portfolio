---
obsidianUIMode: preview
Language: Python 3
Category: Programming
Topic: COMS-170 Intro to Programming
Type: Completed Code
System: Any
Element type: Code Block
Source: Matthew Howard(Myself)
Complexity: Intermediate
Last Edited: 2025-07-22
---
```python
# Matthew Howard
# 0559162
# Program 3
# COMS-170-01: Winter 2025
# Due: 2/7/25
# Program 3 - A simple program to understand Booleans, using input the program selects the proper print options determined by the int value.
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# strCredits            input/str   Prompt user inpuit for number of credits, stores input as variable
# intCredits            Integer     Converts input string to integer   
 
   
print("********************************************************************************")
print("  Michigan University of Computer Science and ONLY Computer Science (MUCSOCS)")
print("********************************************************************************")

print("CLASS STANDING EVALUATOR\n")

strCredits = input("Enter the number of credits earned: ")

intCredits = int(strCredits)

if int(intCredits) <=0:
    print("ERROR: Negative Credits Entered")
elif intCredits >= 0 and intCredits <= 30:
    print("Freshman: Welcome to MUCSOCS")
elif intCredits >= 30 and intCredits <= 60:
    print("Sophomore: You’re making progress")
elif intCredits >= 60 and intCredits <= 90:
    print("Junior: Getting close. Don’t give up now.")
elif intCredits >= 90 and intCredits <= 120:
    print("Senior: Almost done!")
elif intCredits >= 120:
    print("Welcome to the MUCSOCS Alumni Association")

## 63 Credits


# ********************************************************************************
#   Michigan University of Computer Science and ONLY Computer Science (MUCSOCS)   
# ********************************************************************************
# CLASS STANDING EVALUATOR

# Enter the number of credits earned: 63
# Junior: Getting close. Don’t give up now.

## 125 Credits

# ********************************************************************************
#   Michigan University of Computer Science and ONLY Computer Science (MUCSOCS)
# ********************************************************************************
# CLASS STANDING EVALUATOR

# Enter the number of credits earned: 125
# Welcome to the MUCSOCS Alumni Association


## 21 Credits


# ********************************************************************************
#   Michigan University of Computer Science and ONLY Computer Science (MUCSOCS)   
# ********************************************************************************
# CLASS STANDING EVALUATOR

# Enter the number of credits earned: 21
# Freshman: Welcome to MUCSOCS
```