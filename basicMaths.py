"""
Lara Atanasova
Basic math functions in Python
"""

#Math
import math;
from random import randint;

# getting user input
# all input is default string
userString = input("Please enter a number");

# Casting user input
userNumber = int(input("Please enter another number"));

print(userString + " That was the first number.");
print(str(userNumber) + " That was our second number casted as an int.")

#Operators
userInNumOne = int(input("Please write the first number"));
userInNumTwo = int(input("Please write the second number"));

sumOfUserNums = userInNumOne + userInNumTwo;
diffrenceOfUserNums = userInNumOne - userInNumTwo;
prod = userInNumOne*userInNumTwo;
power = userInNumOne**4;
rootOne = math.sqrt(userInNumOne);
rootTwo = math.sqrt(userInNumTwo);
remander = userInNumOne%3;

print("The sum of"+ str(userInNumOne)+" and "+ str(userInNumTwo) +"is: "+ str(sumOfUserNums));
print("The diffrence of"+ str(userInNumOne)+" and "+ str(userInNumTwo) +"is: "+ str(diffrenceOfUserNums));
print("The product of"+ str(userInNumOne)+" and "+ str(userInNumTwo) +"is: "+ str(prod));
print("The power of"+ str(userInNumOne)+" and " + str(userInNumTwo) +"is:"+ str(power));
print("The First number's root is: "+ str(userInNumOne)+ str(rootOne));
print("The Second number's root is: "+ str(userInNumTwo)+ str(rootTwo));
print("The remainder of"+ str(userInNumOne)+" and "+ str(userInNumTwo) +"is: "+ str(remander));