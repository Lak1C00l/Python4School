"""
Lara Atanasova
List excersises
"""
from random import randint


#Write a Python program to remove duplicates from a list (hint: create a copy of the list to remove items from, or use a list to keep track of the indices of duplicates)

userList = []
for i in range(0,10):
    userList.append(randint(1,10))

nonRepeats = []
for x in userList:
    if x in userList:
        nonRepeats.append(x)
#     inList = False
#     for rep in nonRepeats:
#         if rep == x:
#             inList = True
#     if not(inList):
#         nonRepeats.append(x)
# print(userList)
# print(nonRepeats)
print(nonRepeats)


userList = []
lSize = int(input("How big should the list be: "))

for i in range(0,lSize):
    userList.append(randint(0,10000))
print(userList)

#Write a Python program to sum all the items in a user defined list (use loops not built in sum functions)

sum = 0
for i in userList:
    sum+=i
print(sum)

#Write a Python program to multiplies all the items in a user defined list (use loops not built in product functions)

prod = 1
for i in userList:
    prod *= i
print(prod)

#Write a Python program to get the largest number from a user defined list (use loops not built in min/max functions)

largest = userList[0]

for i in userList:
    if i>largest:
        largest = i
print(largest)

#Write a Python program to get the smallest number from a user defined list (use loops not built in min/max functions)

smallest = userList[0]
for item in userList:
    if item<smallest:
        smallest = item
print(smallest)

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

strList = []
lSise = int(input("Please enter length of string"))
for i in range(lSise):
    myString = input("Please enter string")
    strList.append(myString)

largeStrings = 0
for item in strList:
    if len(item)> 2 and (item [0] == item[len(item)-1]):
        largeStrings += 1
print(largeStrings)

