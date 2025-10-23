import os
from random import randint
#nim
# Print the instructions
print("The game Nim starts out with seven sticks on the table.")
print("Each player takes turns picking up 1, 2 or 3 sticks and cannot pass.")
print("Whoever picks up the last stick loses (the other player wins).")

numberOfSticks = 7;
computerMove = randint(1,3);
userMove = input("Would you like to go second or first: ").lower()
if userMove == 'second':
    numberOfSticks -= 2
print(f"Number of sticks left is: {numberOfSticks}")
while numberOfSticks > 0:
        userSticks = int(input("How many sticks would you like to take between three between one? "))
        if userSticks > 3 or userSticks < 1 or userSticks > numberOfSticks or userSticks == 0:
            userSticks = int(input("Invalid number"))
        else:
            numberOfSticks -= userSticks
            print(f"Number of sticks left is: {numberOfSticks}")
            if numberOfSticks - computerMove == 0:
                print("Congradulations user you win!")
    
        while (numberOfSticks - computerMove) < 0 :
            computerMove = randint(1,3)

        numberOfSticks -= computerMove
        print(f"Computer move was: {computerMove}")
        print(f"Number of sticks left is: {numberOfSticks}")
        if numberOfSticks - userSticks == 0:
            print("HAHAHA you looosseee!!")


    
        
   

# accepts any number of grades. When the user enters “exit” terminate the loop and calculate the average, 
# printing the average to the screen
calculateing = True;
while calculateing:
    grades = []
    while exit != "exit":
        grade = float(input("Please input your grade: "))
        grades.append(grade)
        exit = input("Say exit if you would like to calculate your average: ").lower();

    average = 0;
    for i in grades:
        average = i + average
        numberOfElements = len(grades)
        average = average/numberOfElements
        calculateing = False;
    print(average)

#accepts a sequence of lines (blank line to terminate to exit) as input 
# and prints the lines as output (all characters in lower case)
ex = False 
finailMesssage = ''
while not ex:
    lines = input("Please give a series of sentences (nothing to exit).").lower
    finailMesssage += lines + "\r\n"
    if line == "":
        ex = True
print(finailMesssage)



#iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz"
for i in range(1,51):
    if i%3 ==0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 ==0 :
        print("Fizz")
    else:
        print(i);
count = 1;
while count<=50:
    if count%3 ==0 and count%5 == 0:
        print("FizzBuzz")
    elif count%5 == 0:
        print("Buzz")
    elif count%3 ==0 :
        print("Fizz")
    else:
        print(i);
    

    count += 1;

# Create a game where one user enters a number and the other  user guesses a number from, and the program tells them if its too high or low. Game ends when the user selected the correct number
userNum1 = int(input("Please enter number to be guessed between 1 and 1000: "))
clear = lambda: os.system('cls')
userNum2 = int(input("Please enter your guess: "))
os.system('cls')
while userNum1<1 or userNum1>1000:
    userNum1 = int(input("Please enter number to be guessed that is between 1 and 1000: "))
while userNum1 != userNum2:
        if userNum2 > userNum1:
            print("Number is too high")
            userNum2 = int(input("Please enter your guess: "))
        elif userNum2 < userNum1:
            print("Number is too small")
            userNum2 = int(input("Please enter your guess: "))
print("Congratulations!")
