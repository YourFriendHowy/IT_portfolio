```python
# Matthew Howard
# 0559162
# Program 2
# COMS-170-01: Winter 2025
# Due: 1/31/25
# Program 2 - A simple program that uses user input to output stored values
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# discountPercentage   float     Stores the discount percentage
# tax                  float     Stores the tax rate
# originalPrice        str       Prompts user input than stores value as string
# discountPrice        str       Converts values to integers and float to processes the equation 
# taxAmount            str       Multiplies the discountPrice by tax to determine taxAmount
# total                str       adds tax amount to discount price

# Create variables and assign values
discountPercentage = (12)/100 # student number 0559162, 2 + 10 = 12%
tax = (4)/100 # Last name Howard, making tax based on hawaii which is 4%
originalPrice = input("What is the price of the item?\n")

# Perform calculations and operations
discountPrice = (originalPrice) - (originalPrice) * (discountPercentage)
taxAmount = discountPrice * tax
total = discountPrice + taxAmount

# Display output to user
print("\n-------------------------")
print("Employee Discount Calculator")
print("-------------------------")
print("Original price:", originalPrice)
print("Discounted Price:", format(discountPrice, '.2f'))
print("Tax:", format(taxAmount, '.2f'))
print("Final Price:", format(total, '.2f'))

# Add Output of final program as Comments
# What is the price of the item?
# 799

# -------------------------
# Employee Discount Calculator
# -------------------------
# Original price: 799
# Discounted Price: 703.12
# Tax: 28.12
# Final Price: 731.24
```