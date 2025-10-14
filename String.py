userName = input("Please enter your name: ");
greeting = "Hello "+ userName;
print(greeting);

messasge = input("Please enter message to be manipulated")
print(messasge.capitalize())
print(messasge.upper())
print(messasge.lower())
print(messasge.swapcase())
print(messasge.title())

stripMessage = "                 THIS IS SOME TEXT WITH WHITESPACE        "
print(stripMessage)
print(stripMessage.strip())
print(stripMessage.lstrip())
print(stripMessage.rstrip()) 

# Finding a certain charachter or portion of string and changing it's value
findMessage = "Twas brilling and the slithy toad"
print(findMessage.replace("toad","toave"))
# Finding a certain charachter or portion of string 
print(findMessage.find("brilling"))
print(findMessage.rfind("t"))

#substring 
sub_message = "You may not be interested in war, but war is intersted in you" 
#We are splitting on the caracter ' ' (an empty space). This is called a delimiter
sub_string = sub_message.split(" ")
print(sub_string[2])