# if statements
#examples:
age = int(input("Please enter you age: "))
# basic = if elif else
if age>=18 and age< 180:
    print("You may vote")
elif age <18 and age>0:
    print("You cannot vote")
else:
    print("You are non-corporial a mortal") 

secret = "mysEri0Us"
password = input("Please enter thy password: ")
if password == secret:
    print("You're in agent")
else:
    print("INCORECT fscility is now on lockdown")

userNum = int(input("please give me a number"))
userNum2 = int(print("Please enter another number"))

if userNum<=userNum2:
    print("Num2 was grater than Num1")
if userNum%2 or userNum2%3:
    print("One number is even")
# if is checking is something is NOT true 
# these both have the same function but diffret ways of accomplising it
if not(userNum2%2==0):
    print("Your first number is not even")
if userNum2 !=0:
    print("Your second number is not even")