import tkinter as tk

root = tk.Tk()
root.title("student profile")
root.geometry("500x500")

def display_result():
    name = name_entry.get()
    college = college_entry.get()

    if name == "" or college == "":
        result_label.configure(text="Enter all details first!")
    else:
        try:
            s1 = int(sub1_entry.get())
            s2 = int(sub2_entry.get())
            s3 = int(sub3_entry.get())

            total = s1 + s2 + s3
            percentage = total / 3

            result_label.configure(
                text=f"Welcome {name}\n"
                     f"College name: {college}\n"
                     f"Total: {total}\n"
                     f"Percentage: {percentage:}\n%"
            )
            
    print("resualt")

label = tk.Label(root, text="student name")
label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

label = tk.Label(root, text="student collge name")
label.pack()
college_entry = tk.Entry(root)
college_entry.pack()

label = tk.Label(root, text="subject 1")
label.pack()
sub1_entry = tk.Entry(root)
sub1_entry.pack()

label = tk.Label(root, text="subject 2")
label.pack()
sub2_entry = tk.Entry(root)
sub2_entry.pack()

label = tk.Label(root, text="subject 3")
label.pack()
sub3_entry = tk.Entry(root)
sub3_entry.pack()

button= tk.Button(root, text="Generate Result", command=display_result)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
