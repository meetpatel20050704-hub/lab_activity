class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        c = self.a + self.b
        print("Addition is", c)
        
    def subtraction(self):
        c = self.a - self.b
        print("Subtraction is", c)


# create object
obj = Calculator(10, 5)

# call methods
obj.addition()
obj.subtraction()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Student("meet", 30)

print(p1.name)
print(p1.age) 