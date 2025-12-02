"""
Lara Atanasova
Basics Assignment
"""
import math;

#The integer value
intValue = 5;
print("This value is the integer value: " + str(intValue));
#The float
floatValue = 5.5;
print("This value is the float value: " + str(floatValue));
#The double value
doubleValue = 5.5555555555555555555;
print("This value is the double value: " + str(doubleValue));
#The char value
charValue = 'k';
print("This value is the char value: " + str(charValue));
#The string value
stringValue = "Lara is Awesome";
print("This value is the string value: " + str(stringValue));
#The boolen value
boolenValue = False ;
print("This value is the boolen value: " + str(boolenValue));

# This is the addition operator
sum = intValue + floatValue;
print("The sum of our integer and float is: " + str(sum));

# This is the minus operator
diffrence = intValue - floatValue;
print("The diffrence of our integer and float is: " + str(diffrence));

# This is the mutiplication operator
prod = intValue*floatValue;
print("The product of our integer and float is: " + str(prod));

# This is the divison operator
division = intValue/floatValue;
print("When our integer is divided by our float the value is: " + str(division));

# This is the exponent operator
power = intValue**5;
print("The integer to the power 5 is: " + str(power));

# This is the square root operator
root = math.sqrt(intValue);
print("The square root of the integer is: " + str(root));

# This is the remainder value operator
remander = intValue%2;
print("The remainder of the division between our integer and 2 is: " + str(remander));

# User values for the Discriminant equation
a = input("Enter the value of A: ");
b = input("Enter the value of B: ");
c = input("Enter the value of c: ");

# Results of the Discriminant equation
discrimint = int(b)**2-4*int(a)*int(c);
# printing results
print("The Discriminant is: " + str(discrimint));

# user input for length of cube and printing result of calculation 
lengthOfCube = input("Enter the length of an egdge for your cube: ");
volOfCube = int(lengthOfCube)**3;
print("The volume of your cube is: " + str(volOfCube));

# user input for radius of shpere and printing result of calculation 
radiusOfSphere = input("Enter the radius of your sphere: ");
volOfSphere = (4/3)*3.1416*int(radiusOfSphere)**3;
print("The volume of your sphere is: " + str(volOfSphere));

# user input for radius and height of cone and printing result of calculation 
radiusOfCone = input("Enter the radius of your cone's base : ");
heightOfCone = input("Enter the height of your cone: ");
volOfCone = (1/3)*3.1416*int(radiusOfCone)**2*int(heightOfCone);
print("The volume of your cone is: " + str(volOfCone));

# user input for radius and height of the cylander and printing result of calculation 
radiusOfCylinder = input("Enter the radius of your cylinder's base : ");
heightOfCylinder = input("Enter the height of your cylinder: ");
volOfCylinder = 3.1416*int(radiusOfCylinder)**2*int(heightOfCylinder);
print("The volume of your cube is: " + str(volOfCylinder));