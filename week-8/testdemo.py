import tkinter as tk

root =tk.Tk()
root.title("Generat the welcome message")
root.geometry("500x500")

def display_message():
    user_name = entry.get()
    if user_name == "":
        display_lable.configure(text="Enter the name first!")
    else:
        display_lable.configure(text=f"welcome {user_name}")

label = tk.Label(root, text ="enter your name")
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(root, text="genret", command=display_message)
button.pack()

display_lable = tk.Label(root, text="")
display_lable.pack()

root.mainloop()
