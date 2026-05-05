def welcome_message():
    print("Welcome to Python Lab")

# Call the function
welcome_message()

#2

def name(name):
    print("Hello", name)
    
name("Meet")

#3

def sum(a,b):
    c=a+b
    print(c)
    
sum(10,15)

#4

def check(number):
    if number %2 == 0: 
        print("even number", number)
    else:
        print("odd number", number)
        
check(10)
check(39)
    
# Task 5: Print numbers from 1 to 5
print("Numbers from 1 to 5")
i = 1
while i <= 5:
    print(i)
    i += 1

# Task 6: Ask user numbers until 0, print total
print("Sum of numbers (enter 0 to stop)")
total = 0
num = int(input("Enter a number: "))

while num != 0:
    total += num
    num = int(input("Enter a number: "))

print("Total =", total)

# Task 7: Password check until correct
print("Password Check")
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access Granted!")

# Task 8: Item entry system and calculate total
print("Item Entry System")
total_cost = 0

price = float(input("Enter item price (0 to stop): "))

while price != 0:
    total_cost += price
    price = float(input("Enter item price (0 to stop): "))

print("Total cost =", total_cost)
 # Task 9: Print numbers from 1 to 10
print("Numbers from 1 to 10")
for i in range(1, 11):
    print(i)

# Task 10: Calculate total from list
print("Total of list")
numbers = [100, 200, 300]
total = 0

for num in numbers:
    total += num

print("Total =", total)

# Task 11: Print items from list
print("Print items")
items = ["Apple", "Banana", "Mango"]

for item in items:
    print(item)

# Task 12: Print items with index
print("Items with index")
for index, item in enumerate(items):
    print(index, item)
    

# Task 13
def add():
    t=0
    n=int(input("Enter (0 to stop): "))
    while n!=0:
        t+=n
        n=int(input("Enter (0 to stop): "))
    return t

print("Total =", add())


# Task 14
def total(l):
    return sum(l)

print("Total =", total([10,20,30]))


# Task 15
def show(i,p):
    for x,y in zip(i,p):
        print(x,"=",y)

print("Task 15 Output:")
show(["Pen","Book","Bag"],[1.5,5,20])

i=[]
while True:
    x=input("Price or done: ")
    if x=="done": break
    i.append(float(x))

t=0
for n in i: t+=n

while True:
    print("Total:",t)
    print("Approved" if t>500 else "Not Approved")
    break