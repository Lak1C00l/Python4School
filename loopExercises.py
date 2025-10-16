"""
Lara Atanasova
Loop exercises
"""
# Create a program that takes in input from a user and prints out the sum from 1 to whatever number the user puts in
userNum = int(input("please input a Number one larger than the number you wish to calculate the sum of a series: "));
sum = 0;
for i in range(0,userNum):
    sum = sum + i
    print(sum);

# Create a program that nests for loops that will print out all the prime numbers from 1-100
# potentialPrime = 0;
# potPrime = 0;
# for p in range(0,101):
#     for x in range(2,101):
#             potentialPrime = p % x 
#     if not(potentialPrime > 0) and p != 1:
#             print(p)

#Create a program that will print out a right angle triangle of stars. Number of rows to be taken in as user input
numberOfRows = int(input("How many rows do you want? : "))
for i in range(numberOfRows):
    for x in range(i+1):
        print("*",end=" ")
    print()

#Create a program that will take in a users name and then print it out in reverse using for loops
userName = input("what is your name: ")
userName = userName.split()
for i in reversed(userName):
    print(i)