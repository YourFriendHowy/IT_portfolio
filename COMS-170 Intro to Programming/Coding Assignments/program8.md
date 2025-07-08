```python
# Matthew Howard
# 0559162
# Program 8
# COMS-170-01: Winter 2025
# Due: 4/18/25
# Program 8 - A simple program that uses user input to output corrected punctuiation in strings
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
#strInput               str       collect user input
#strList                list      saves strInput as list
#stpList                list      saves stipped version of strList
#endList                list      capitalizes the first letter of each string in stpList and saves it as a new list



proceed = "y"


while proceed == "y":
    strInput = input("Enter Sentences to be modified: \n")
    print("\n")
    strList = []
    stpList = []
    endList = []
    try:
        for s in strInput.split('.'):
            strList.append(s + ".")
        del strList[-1]

        for s in strList:
            stpList.append(s.lstrip()+ " ")
        
        for s in stpList:
            endList.append(s[0].upper() + s[1:])

        print("your modified sentence is: \n", ''.join(endList), "\n", sep='')


    except:
        print("Incorrect characters  entered!")
    
    proceed = input("Enter 'y' to try again: \n")    

# Add Output of final program as Comments


# Enter Sentences to be modified: 
# my name is Samantha. i go to Mott Community College.


# your modified sentence is:
# My name is Samantha. I go to Mott Community College.

# Enter 'y' to try again:
# y
# Enter Sentences to be modified: 
# my favorite character is Charlie Brown. he is a great sport.


# your modified sentence is:
# My favorite character is Charlie Brown. He is a great sport.

# Enter 'y' to try again:
# y
# Enter Sentences to be modified: 
# programming in Python is super FUN. i can't wait to learn more. 


# your modified sentence is:
# Programming in Python is super FUN. I can't wait to learn more.

# Enter 'y' to try again:
# n
```