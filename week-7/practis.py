# write the pythone faction to desplay following 2 student data student id, student name, 1 percantage ask the user to enter id,name and three subject marks

def calculate_percentage(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def display_student(student_id, student_name, percentage):
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Percentage:", percentage, "%")

def main():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    
    mark1 = float(input("Enter marks for subject 1: "))
    mark2 = float(input("Enter marks for subject 2: "))
    mark3 = float(input("Enter marks for subject 3: "))
    
    percentage = calculate_percentage(mark1, mark2, mark3)
    
    display_student(student_id, student_name, percentage)

main()