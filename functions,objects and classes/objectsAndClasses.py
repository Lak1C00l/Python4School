from Person import Person

people = []
numPeople = int(input("How many people?"))
for i in range(numPeople):
    age = int(input("Please enter age of person: "))
    name = input("Please enter name of person: ")
    salary = int(input("Please enter salary of person: "))
    person = Person(name,age,salary)
    people.append(person)

test = ""
myName = "Lara"
for person in people:
    person.greeting(myName)