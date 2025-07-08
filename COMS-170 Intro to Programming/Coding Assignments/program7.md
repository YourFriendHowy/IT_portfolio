```python
# Matthew Howard
# 0559162
# Program 7
# COMS-170-01: Winter 2025
# Due: 4/11/25
# Program 6 - A simple program utilizing lists
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
#fltVal                 float       saves user input, used to add input to list
#fltTime                float       empty list that can have objects added to it

fltVal = 999
fltTime = []

while fltVal != -1:
    try:
        fltVal = float(input("Enter completion time(in seconds) or -1 to calculate results: "))
        fltTime.append(fltVal)
    except:
        print("ERROR invalid character entered, please enter a number.")
                   
del fltTime[-1]       

print("")
print("Fastest completetion time:", format(min(fltTime), '.2f'))
print("slowest completetion time:", format(max(fltTime), '.2f'))
print("Average completetion time:", format(sum(fltTime)/len(fltTime), '.2f'))
print("")
print("All Competitor Times:")

for i in range(len(fltTime)):
    print(i+1,": ",format(fltTime[i], '.2f'), " Seconds", sep="")



# Output of final program

# program7.py
# Enter completion time(in seconds) or -1 to calculate results: 465.62
# Enter completion time(in seconds) or -1 to calculate results: 485.915
# Enter completion time(in seconds) or -1 to calculate results: 2064.847
# Enter completion time(in seconds) or -1 to calculate results:
# ERROR invalid character entered, please enter a number.
# Enter completion time(in seconds) or -1 to calculate results: 503.76
# Enter completion time(in seconds) or -1 to calculate results: 479.341
# Enter completion time(in seconds) or -1 to calculate results: -1

# Fastest completetion time: 465.62
# slowest completetion time: 2064.85
# Average completetion time: 749.91

# All Competitor Times:
# 1: 465.62 Seconds
# 2: 485.92 Seconds
# 3: 499.99 Seconds
# 4: 2064.85 Seconds
# 5: 503.76 Seconds
# 6: 479.34 Seconds
# program7.py
# Enter completion time(in seconds) or -1 to calculate results: 565
# Enter completion time(in seconds) or -1 to calculate results: 512
# Enter completion time(in seconds) or -1 to calculate results: 594
# Enter completion time(in seconds) or -1 to calculate results: 577
# Enter completion time(in seconds) or -1 to calculate results: 543
# Enter completion time(in seconds) or -1 to calculate results: -1

# Fastest completetion time: 512.00
# slowest completetion time: 594.00
# Average completetion time: 558.20

# All Competitor Times:
# 1: 565.00 Seconds
# 2: 512.00 Seconds
# 3: 594.00 Seconds
# 4: 577.00 Seconds
# 5: 543.00 Seconds

# Enter completion time(in seconds) or -1 to calculate results: 2065.94
# Enter completion time(in seconds) or -1 to calculate results: 2217.37
# Enter completion time(in seconds) or -1 to calculate results: 1979.62
# Enter completion time(in seconds) or -1 to calculate results: -1

# Fastest completetion time: 1979.62
# slowest completetion time: 2217.37
# Average completetion time: 2087.64

# All Competitor Times:
# 1: 2065.94 Seconds
# 2: 2217.37 Seconds
# 3: 1979.62 Seconds

```