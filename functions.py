
from random import randint

rando = [] 
for i in range(10): rando.append(randint(1,100))

"""sum all numbers in list and return list"""
def retSum(myList):
    sum = 0 
    for item in myList:
        sum+=item
    return sum
print(rando)
print(retSum(rando))

"""To multiply all the numbers"""
def retProd(myList):
    sum = 1 
    for item in myList:
        sum*=item
    return sum
print(rando)
print(retProd(rando))

"""To reverse string"""
def revStr(myString):
    retString = ""
    for i in range(len(myString)-1,-1,-1):
        retString += myString[i]
    return retString
print(revStr("Computation"))

"""Num in givin range"""
def rangeFinder(num,Min,Max):
    if num > min and num < max:
        return True
    return False
min = 0
max = 100
userNum = int(input("Please enter a number inbettwen 0 and 100: "))
print(rangeFinder(userNum,min,max))

"""Prints even nums from list"""
def evenNums(myList):
    for item in myList:
        if item % 2 == 0:
            print(item)
print(rando)
evenNums(rando)

"""palindrome tester"""
def isPalendrome(message):
    trimMessage = message.replace(" ","").lower()
    revrseStr = revStr(trimMessage)
    for i in range(len(trimMessage)):
        if trimMessage[i] != revrseStr[i]:
            return False
        # if trimMessage[i] != revStr[len(message)-i-1]:
        #     return False
    return True
print(isPalendrome("Rise to vote sir"))

def isPangram(message):
    trim = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyx"
    for letter in trim:
        alpha = alpha.replace(letter,"")
    if len(alpha) == 0:
        return True
    return False
print(isPangram("quick brown fox jumps over the lazy dog"))