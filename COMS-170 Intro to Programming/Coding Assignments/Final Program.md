```python

decrypt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
encrypt = ["G", "X", "3", "K", "P", "9", "D", "6", "N", "1", "S", "F", "L", "W", "2", "T", "A", "Z", "5", "Y", "0", "M", "C", "7", "U", "I", "R", "8", "E", ".", "O", "B", "V", "Q", "H", "4"]
charList = []

def main():  # menu
    menuSelect = ""
    print("********************************************************")
    print("             Welcome to the Cypher Module               ")
    print("********************************************************")
    
    while menuSelect != "T":
        print("\nTo encrypt a message press [E]")
        print("To decrypt a message press [D]")
        print("To terminate program press [T]\n")
 
        menuSelect = input("Please select an option from the menu: ").upper()
 
        if menuSelect == "E":
            cypher()
            outPut = "".join(charList) 
            print("\nYour Encrypted Message is:\n", outPut, sep = "")
 
            menuSelect = input("Press Enter to return to menu.")    
  
        elif menuSelect == "D":
            decypher()
            outPut = "".join(charList).capitalize()          
            print("\nYour decrypted Message is:\n", outPut, sep = "")          
  
            menuSelect = input("Press Enter to return to menu.")

def cypher(): # encodes user input
    charList.clear() #https://docs.python.org/3/library/stdtypes.html
    codeInp = input("\nPlease enter text to be encrypted:\n").upper()
    for s in codeInp:
        try:
            indexChar = encrypt[decrypt.index(s)] #https://docs.python.org/3/library/stdtypes.html
        except:
            charList.append(s)
        else:
            charList.append(indexChar)

def decypher(): # decodes user input 
    charList.clear() #https://docs.python.org/3/library/stdtypes.html
    codeInp = input("\nPlease enter text to be decrypted:\n").upper()
    for s in codeInp:
        try: 
            indexChar = decrypt[encrypt.index(s)] #https://docs.python.org/3/library/stdtypes.html
        except:
            charList.append(s)
        else:
            charList.append(indexChar)
            
    

main()



## output of program
# ********************************************************
#              Welcome to the Cypher Module
# ********************************************************

# To encrypt a message press [E]
# To decrypt a message press [D]
# To terminate program press [T]

# Please select an option from the menu: e

# Please enter text to be encrypted:
# I would like to encrypt this message to show that this program works properly! 

# Your Encrypted Message is:
# N C20FK FNSP Y2 PW3ZUTY Y6N5 LP55GDP Y2 562C Y6GY Y6N5 TZ2DZGL C2ZS5 TZ2TPZFU! 

# Press Enter to return to menu.d

# To encrypt a message press [E]
# To decrypt a message press [D]
# To terminate program press [T]

# Please select an option from the menu: d

# Please enter text to be decrypted:
# N C20FK FNSP Y2 PW3ZUTY Y6N5 LP55GDP Y2 562C Y6GY Y6N5 TZ2DZGL C2ZS5 TZ2TPZFU!

# Your decrypted Message is:
# I would like to encrypt this message to show that this program works properly!

# Press Enter to return to menu.

# To encrypt a message press [E]
# To decrypt a message press [D]
# To terminate program press [T]

# Please select an option from the menu: t

```