# This function prints a simple message
def my_function():
    print("Hello from a function")

# Calling the function once
my_function()


# This function prints another message (fixed function call)
def my_namew():
    print("Hello from my_namew function")

# Calling my_namew function (instead of calling my_function again by mistake)
my_namew()
my_namew()
my_namew()


# This function takes a name as input and prints it
def my_name(name):
    print("My name is:", name)

# Calling the function with an argument
my_name("Meet Patel")


# This function displays student data (fixed spelling: display_data)
def display_data(std_id, std_name):
    print("Student ID is:", std_id)
    print("Student name is:", std_name)

# Calling the function with student ID and name
display_data(20260261, "Meet")

def data_name(name):
    print("Hello I am here to learn python")
    return name
data_name("meet") 