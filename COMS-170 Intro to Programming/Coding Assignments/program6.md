```python
# Matthew Howard
# 0559162
# Program 6
# COMS-170-01: Winter 2025
# Due: 4/4/25
# Program 6 - A program that reads from a file and does calculations using file data
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
#strChoice              string         defines and saves the string inputs to navigate the menus
#total                  float          saves  intTotal from CalcTotal()
#average                float          saves fltAverage from CalcTotal()
#count                  int            saves the count for lines in the file
#cards                  str            saves the task to open a file named cards.txt
#line                   str            defines the lines in a file and strips them of \n
#fltTotal               float          saves and adds up the total of all sales in the file
#fltAverage             floar          calculates intTotal/count to save the average of sales in the file cards.txt

def Main():
   strChoice = ""
  
   while strChoice != "x":
        print("=======================================================")
        print("*                  Pokemon Card Sales                 *")
        print("=======================================================")
        print("C: Calculate Card Total and Average Sales")
        print("D: Display Sales")
        print("X: Exit application")

        strChoice = input("\nEnter your menu selection: ")
        if strChoice == "D" or strChoice == "d":
            DisplayCardSales()
            strChoice = ""
        elif strChoice == "C" or strChoice == "c":
            try:
                total, average = CalcTotal()
            except:
                print("No value found.")
            else:
                print("Total Sales: $", format(total, '.2f'), sep="")
                print("Average Sale: $", format(average, '.2f'), sep="")
           
            finally:
             strChoice = ""

def  DisplayCardSales():
    count = 0
    try:
        cards = open('cards.txt', 'r')
    except:
        print("File not found.")
    else:    
        for line in cards:
            count = count + 1   
            print(count,": $",line.rstrip(), sep='')
            #continue

def  CalcTotal():
    fltTotal = 0
    count = 0
    try:
        cards = open('cards.txt', 'r')
    except:
        print("File Not Found.")
    else: 
        for line in cards:
            line = line.rstrip("\n")
            fltTotal = fltTotal + float(line)   
            count += 1    
        cards.close()
        fltAverage = (fltTotal)/(count)
        return fltTotal, fltAverage
    
Main()

# Output of final program


# =======================================================
# *                  Pokemon Card Sales                 *
# =======================================================
# C: Calculate Card Total and Average Sales
# D: Display Sales
# X: Exit application

# Enter your menu selection: d
# 1: $2.85 
# 2: $4.09 
# 3: $1.19 
# 4: $2.58 
# 5: $0.70 
# 6: $1.39 
# 7: $2.57 
# 8: $4.39 
# 9: $2.68 
# 10: $4.43
# 11: $3.05
# 12: $1.99
# 13: $1.88
# 14: $4.83
# 15: $1.48
# 16: $2.79
# 17: $0.11
# 18: $2.41
# 19: $1.64
# 20: $3.64
# 21: $2.05
# 22: $4.34
# 23: $0.48
# 24: $4.21
# 25: $4.55
# 26: $3.68
# 27: $4.63
# 28: $2.92
# 29: $0.67
# 30: $2.81
# 31: $2.47
# 32: $1.57
# 33: $3.35
# 34: $0.27
# 35: $4.87
# 36: $0.80
# 37: $4.47
# 38: $4.76
# 39: $3.34
# 40: $0.20
# 41: $3.12
# 42: $3.09
# 43: $2.98
# 44: $1.30
# 45: $4.69
# 46: $4.84
# 47: $4.31
# 48: $2.80
# 49: $0.51
# 50: $4.19
# 51: $4.00
# 52: $3.57
# 53: $3.20
# 54: $1.58
# =======================================================
# *                  Pokemon Card Sales                 *
# =======================================================
# C: Calculate Card Total and Average Sales
# D: Display Sales
# X: Exit application

# Enter your menu selection: c
# Total Sales: $151.31
# Average Sale: $2.80
# =======================================================
# *                  Pokemon Card Sales                 *
# =======================================================
# C: Calculate Card Total and Average Sales
# D: Display Sales
# X: Exit application

# Enter your menu selection: x
```