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
# Program 5
# COMS-170-01: Winter 2025
# Due: 1/31/25
# Program 5 - An incomplete program to learn the use of functions while using a menu system. Sorry it is not complete I ended up with alot of hours this week this was the best I could get in the time i had. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------


def main():
    strChoice = ""
   
    while strChoice != "x":
        print("=======================================================")
        print("*                The Coffee Connection                *")
        print("=======================================================")
        print("C: Calculate price for coffee drink being ordered")
        print("D: Display coffee menu price information")
        print("X: Exit application")

        strChoice = input("Enter your menu selection: ")

    if strChoice == "D" or strChoice == "d":
        DisplayMenu()
        strChoice = input("Press Enter to return to menu.")
    elif strChoice == "C" or strChoice == "c":
        taxAmount = CalcTotal()
        print("Total:", format(taxAmount, ".2f"))
        strChoice = input("Press Enter to return to menu.")

        

def DisplayMenu():   
    print("=======================================================")
    print("*             The Coffee Connection Menu              *")
    print("=======================================================")
    print("All prices before tax.:")
    print("Black Coffee: $1.59")
    print("Cappuccino: $3.79")
    print("Latte: $2.99")
    print("Mocha Latte: $3.59")
    print("Shot of Espresso: $1.99")
            
def CalcTotal():
    menuChoice = input ("Enter the drink you would like to order: (B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso: ")
    if menuChoice == "B" or menuChoice == "b":
        subtotal = 1.59    
           
    elif menuChoice == "C" or menuChoice == "c":
        subtotal = 3.79
                
    elif menuChoice == "L" or menuChoice == "l":
        subtotal = 2.99
            
    elif menuChoice == "M" or menuChoice == "m":
        subtotal = 3.59
            
    elif menuChoice == "S" or menuChoice == "s":
        subtotal = 1.99
    
    
    fltTax = (subtotal)+(CalcTax(subtotal))   
    return fltTax

   
def CalcTax(subtotal):
    taxRate = subtotal * 0.04
    return taxRate


main()

# the results im getting

# =======================================================
# *                The Coffee Connection                *
# =======================================================
# C: Calculate price for coffee drink being ordered
# D: Display coffee menu price information
# X: Exit application
# Enter your menu selection: c
# Enter the drink you would like to order: (B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso: c
# 3.79
# 0.1516
# Press Enter to return to menu.
```