class Person():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def greeting(self,geustName):
        print(f"Hello {geustName}, my name is {self.name}")