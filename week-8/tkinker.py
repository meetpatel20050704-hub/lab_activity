import tkinter as tk

root = tk.Tk()
root.title("My first GUI app")
root.geometry("200x300")

label = tk.Label(root, text="Enter your name")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="click me")
button.pack()

checkbutton1 = tk.Checkbutton(root, text="Playing cricket")
checkbutton2 = tk.Checkbutton(root, text="Playing hokey")
checkbutton3 = tk.Checkbutton(root, text="Playing football")
checkbutton4 = tk.Checkbutton(root, text="Playing basketball")

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
checkbutton4.pack()

radiobutton1 = tk.Radiobutton(root, text="male", value = 1)
radiobutton2 = tk.Radiobutton(root, text="female", value = 2)

radiobutton1.pack()
radiobutton2.pack()

root.mainloop()
