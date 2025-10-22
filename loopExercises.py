"""
Lara Atanasova
Loop exercises
"""
#
rows = int(input("max num of stars: "))
for i in range(1,rows+1):
    print("*"*i)
for i in range(rows-1,0,-1):
    print("*"*i)

#find factorial of num enerted by user
num = int(input("Please enert number: "))
fact = 1;
for i in range(num,0,-1):
    fact*= i
print(fact)



userNum = int(input("Please enter number to count: "))
count = 0
for digits in str(userNum):
    count+= 1
print(count)

# Create a program that will take in a number from the user, then a second number
# and it will display the multiplication tables of the first number from 1-Second Number

num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

for i in range(1,num1+1):
    line = " "
    for k in range(1,num2+1):
        times = i +"X" + {k} +" = " +{i*k} +","
    print(line)
    
#Create a program that will take in a users name and then print it out in reverse using for loops
userName = input("what is your name: ")
revName =""
userName
for i in range(len(userName)-1,-1,-1):
    revName += userName[i]
print(revName)

# Create a program that nests for loops that will print out all the prime numbers from 1-10

#Other ways of doing it
# for i in range(0,numberOfRows+1):
#     row="*"*i
#     if row !="":
#         print(row)

# for i in range(0,numberOfRows+1):
#     row=""
#     for k in range(0,i):
#         row+= "*"
#     if row !="":
#         print(row)

#Create a program that will print out a right angle triangle of stars. Number of rows to be taken in as user input
numberOfRows = int(input("How many rows do you want? : "))
for i in range(numberOfRows):
    for x in range(i+1):
        print("*",end=" ")
    print()

# Create a program that takes in input from a user and prints out the sum from 1 to whatever number the user puts in
userNum = int(input("please input a Number : "));
sum = 0;
step = 1;
adder = 1;
if userNum < 0:
    step = -1
    adder = -1
for i in range(0,userNum+adder,step):
    sum = sum + i
    print(sum);
