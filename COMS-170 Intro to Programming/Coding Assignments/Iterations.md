Below I learned you can set an inputs type by wrapping the input in it, below you see the input is being converted to an integer.

```Python
x = int(input("input number!")) 
x = x + 1

print(x)
```


```Python
x = 0 ## This line defines and initializes x
x = x+1 ## This line takes x = 0 and adds a 1 to it, outputting a x = 1

print(x) ## Prints 1 
```

```Python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
```

```python
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
```

```Python
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
```

```Python
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)
```

```Python

```