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


### Set input type to integer
```Python
x = int(input("input number!")) 
x = x + 1

print(x)
```

### Create Counter Base
```Python
x = 0 ## This line defines and initializes x
x = x+1 ## This line takes x = 0 and adds a 1 to it, outputting a x = 1

print(x) ## Prints 1 
```

### Create loop counter, decending
```Python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

### Prints sum of list
```python
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
```

### Prints largest integer in list
```Python
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
```

### Prints smallest integer in list
```Python
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
```
