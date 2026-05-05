#write a pogram to print the square of number between 1 to 5

for i in range(6):
    sum = i * i
    print(f"square{1} x {i} = {i*i}")
    
# Multiplication table of 5

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

for i in range(1, 6):
    print("*" * i)

for i in range(5,0,-1):
    print("*" * i)


    
rows = 5

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    