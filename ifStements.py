import math;
# givin co ordnets find which quad on the cartiasn plan it lands
x = int(input("Please eneter x coordenete:"))
y = int(input("Please eneter y coordenete:"))

if x ==0 and y == 0:
    print("You are at the origin")
elif x==0 and y >0:
    print("Origin line on x axis, point lies on positive y axis")
elif y==0 and x >0:
    print("Origin line on y axis, point lies on positive x axis")
elif x==0 and y <0:
    print("Origin line on x axis, point lies on negative y axis")
elif y==0 and x <0:
    print("Origin line on y axis, point lies on negative x axis")
elif x>0 and y>0:
    print("top right Quadrent")
elif x>0 and y<0:
    print("bottom right Quadrent")
elif x<0 and y<0:
    print("bottm left Quadrent")
else:
    print("Top left Quadrent")

#abloute values
userNum = float(input("Please enter a number:"))
if userNum == 0 :
    print("Zero")
else:
    if userNum>0:
        print("positive")
    else:
        print("negative")
    if abs(userNum) < 1:
        print(" VERY SMALL ")
    elif abs(userNum) > 100000:
        print("very large")

# solve quad equaion
a = float(input(" please eneter a value: "))
b = float(input(" please eneter a value: "))
c = float(input(" please eneter a value: "))
discriminant = b**2-(4*a*c)
if discriminant<0:
    print("No roots")
elif discriminant == 0:
    root = (-b + math.sqrt(discriminant))/(2*a)
    print("Your single root is: " + str(root))
else:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b + math.sqrt(discriminant))/(2*a)
    print("Your single root is: " + str(root1)+ " and " + str(root2))

#Write a Python program to convert temperatures to and from celsius, fahrenheit. The user will enter in the unit in the form of a string and a temperature
choice = input("Eneter 1 to convert to celcius, enter 2 to convert to farenhight")
firstTemp = float(input("Please enter a temprature:"))
convertedTemp = float(0)
if choice == '1':
    convertedTemp = ((firstTemp - 32)/9)*5
    print("Temp in celsius is: "+ str(convertedTemp))
elif choice == '2':
    convertedTemp = ((9*firstTemp)/5)+32
    print("Your temprature in ferenhieght is: " + str(convertedTemp))
else:
    print(" FOLLOW INSTRUCTIONs YOU NINCOMPOOP")

# takes in a number from user and determines whether or not that number is odd or even
userNumIsOddOrEven = int(input("Please enter a random number: "))
if userNumIsOddOrEven%2 :
    print("Your number is odd")
else:
    print("Your number is even")


# takes in three numbers from a user and prints out the largest number
a = float(input("Please enter number A: "))
b = float(input("Please enter number B: "))
c = float(input("Please enter number C: "))
if a > b and a > c:
    print("A is the largest number")
elif b > a and b > c:
    print("B is the largest number")
elif c > b and c > a:
    print("C is the largest number")
elif a > c and a == b:
    print("A and b are the same number and larger than C  ")
elif c > b and a == c: 
    print("A and C are the same numbers and larger than B")
elif b > a and b == a:
    print("C and B are the same number and larger than A")
else:
    print("All numbers were even")

# takes in a title and last name from a user and, if the the title is either “Excellency”,”Highness”, or “Lord”  to output an appropriately lavish greeting where all others get a normal greeting

userTitle = input("What is your title? ")
userName = input("What is your lastname? ")
if userTitle.lower() == 'excellency' :
    print("GREETING YOUR EXELANCE!")
elif userTitle.lower() =="lord":
    print("GREETINGS MY LORD "+ userName.upper() +" HOW IST THOW?")
elif userTitle.lower() == "highness":
    print("GREETINGS YOUR ROYAL HIGHNESS "+ userName.upper() +" IT IS OUR PLEASEURE TO SEE YOU!!!!!!")
else:
    print("Welcome")