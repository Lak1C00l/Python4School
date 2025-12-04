"""
Lara Atanasova

Dictionary exercises
"""
from random import randint
#six
rand1 = {}
length = int(input("How long do you want your dictionary to be? : "))
while len(rand1.keys())< length:
    try:
        key = randint(0,10)
        value = randint(0,10)
        rand1[key] = value
    except Exception as ex:
        test = ""
print(rand1)
sum = 0
for value in rand1.values():
    sum += value
print(sum)
input()
#five
square1 ={}
for i in range(1,16):
    square1[i] = i**2

for key,value in square1.items():
    print(f"{key} : {value}")

input()
#four
rand1 = {}
length = int(input("How long do you want your dictionary to be? : "))
while len(rand1.keys())< length:
    try:
        key = randint(0,1000)
        value = randint(0,1000)
        rand1[key] = value
    except Exception as ex:
        test = ""
print(rand1)

findKey = int(input("Enter key: "))
isIn = False
for key in rand1.keys():
    if findKey == key:
        isIn = True
print(isIn)
if findKey in rand1.keys():
    print(True)

input()

# three
rand1 = {}
rand2 = {}
concat = {}
for i in range(10):
    rand1[i] = randint(0,100)
    rand2[i] = randint(0,100)
print(rand1)
print(rand2)

for i in range(len(rand1)):
    concat[i] = rand1[i]
    concat[i+len(rand1)] = rand2
print(concat)

 
input()

randNums = {}
lengthOfList = int(input("How long do you want your dictionary to be? : "))
for i in range(0,lengthOfList):
    randNums[f"Number {i + 1} "] = randint(0,100)
print(randNums)

# one 
#script to sort (ascending and descending) a dictionary by value 

# normal order
for item in sorted(randNums.values()):
    print(item)

# reverse order
for item in sorted(randNums.values(), reverse=True):
    print(item)

# two
#Write a Python script to add a key/value pair to a dictionary
cats = input("Enter a key: ")


