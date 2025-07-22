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
price = input("What is the price of the item you would like to purchase?\n")
discount = input("To calculate your total please enter your student number:\n")
discountInt = int(discount[-1]) # the [-1] is used to find the last number in the input string, reason for use was for fun and to allow entire last names and student numbers to be used. found on flexiple forum after searching out to find the last character in string
discountPercentage = (discountInt+10) / 100
discountTotal = float(price) - float(price) * discountPercentage
tax = input("To determine your taxes please provide your last name:\n")
taxes = tax[+0]

if taxes == "A" or "B" or "C" or "E" or "F":  #If statements and equal-to statements, this is previously known knowledge also listed in the statement chart in chapter 2, I wanted to make a universal program that any student could enter their name rather than keeping it completely simple, I wasnt sure how to do it and experimented with what i did know, the or statement may not be efficient but i didn't want to go overly complex
    taxAmount = .07 * discountTotal
    state = "(7% in Arkansas)"

if taxes == "G" or "H" or "I" or "J" or "k" or "L" or "M":
    taxAmount = .07 * discountTotal
    state = "(4% in Hawaii)"

if taxes == "N" or "O" or "P" or "Q" or "R" or "S":
    taxAmount = .07 * discountTotal
    state = "(6% in Maryland)"

if taxes == "T" or "U" or "V" or "W" or "X" or "Y" or "Z":
    taxAmount = .07 * discountTotal
    state = "5% in New Mexico" 

total = discountTotal + taxAmount

print("\n-------------------------")
print("Employee Discount Calculator")
print("-------------------------")
print("Original price:", price)
print("Discounted Price:", format(discountTotal, '.2f'))
print("Tax:", format(taxAmount, '.2f'), state)
print("Final Price:", format(total, '.2f'))
```