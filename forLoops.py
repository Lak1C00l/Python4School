"""
Lara Atanasova
Exploring how to use For Loops
"""
import time;

# simple for loop ex
sum = 0;
for i in range(0,101):
    sum = sum + i
    print(sum)

# counting up by 5s
for i in range(0,101,5):
    print(i)

# counting down by 4s
for i in range(100,-1,-4):
    print(i)

#print all twos time table numbers
for i in range(1,12):
    prod = 2*i
    print(f"2 x {str(i)} = {str(prod)}")
    
# count down from ten with one second inbetween
for i in range(10,-1,-1):
    print(i)
    time.sleep(1)
print("KABOOOOM")

#print multiples of 7 between one and onehundred
for i in range(1,101):
    if i % 7 == 0:
        print(i)

# print cubes of 3 from 50 to 1
for i in range(50,0,-1):
    print(f"The cube of {i} is equal to {i**3}")

#sample foreach loop
message = "Jade Monkey"
for letter in message:
    print(letter)

