#Rand array for slice removal
import random
from random import randInt

rando = []
for i in range(0,10):
    rando.append(1,100)
print(rando)
del rando[2:5] #excludes five
print(rando)

classList = ["Thor","Loki","Pacard","Freakes"]
classList.appened("The Hulk")

print(classList[0])
print(classList[4])

# ind = int(input("Please enter index of item: ")) 
# place = int(input("Please enter place value of item: "))-1 
# oor = int(input("Please enter number larger than size of list: ")) 

# print(class_list[ind]) 
# print(class_list[place]) 
# print(class_list[oor]) 

# for i in range(0,len(class_list)):
#     print(class_list[i])

# for item in class_list:
#     print(item)

#Random array for slice removal
rando =[]
for i in range(0,10):
    rando.append(randint(1,100))
print(rando)
del rando[2:5]
print(rando)

prices = []
size = int(input("How many prices do you have? "))
for i in range(0,size):
    price = float(input("Please enter a price in USD: "))
    prices.append(price)
exchange = 1.41
for price in prices:
    print("Your price $"+str(price)+" USD is $"+str(price*exchange)+" CAD") 

removed_item = prices.pop(2)
print(removed_item)
print(prices)

prices.remove(13.15)
print(prices)

del prices[0]
print(prices)

prices.clear()
print(prices)