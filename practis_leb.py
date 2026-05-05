import tkinter as tk
from tkinter import messagebox

items = []
counter = 1

def add_item():
    name = entry_item_name.get()
    
    try:
        price = float(entry_item_price.get())
    except:
        messagebox.showerror("Error", "Enter valid price")
        return

    items.append({"name": name, "price": price})
    listbox.insert(tk.END, f"{name} - ${price}")

    entry_item_name.delete(0, tk.END)
    entry_item_price.delete(0, tk.END)


def calculate_total():
    total = 0
    for item in items:
        total += item["price"]

    label_total.config(text=f"Total: ${total}")
    return total


def check_approval():
    global counter

    total = calculate_total()

    req_id = 10000 + counter
    counter += 1

    staff_id = entry_staff_id.get()

    if total < 500:
        status = "Approved"
        ref = staff_id + str(req_id)[-3:]
    else:
        status = "Pending"
        ref = "Not Assigned"

    label_status.config(text=f"Status: {status}")
    label_ref.config(text=f"Approval Ref: {ref}")


root = tk.Tk()
root.title("Requisition System")
root.geometry("500x600")

tk.Label(root, text="Date").pack()
entry_date = tk.Entry(root)
entry_date.pack()

tk.Label(root, text="Staff ID").pack()
entry_staff_id = tk.Entry(root)
entry_staff_id.pack()

tk.Label(root, text="Staff Name").pack()
entry_staff_name = tk.Entry(root)
entry_staff_name.pack()

tk.Label(root, text="Item Name").pack()
entry_item_name = tk.Entry(root)
entry_item_name.pack()

tk.Label(root, text="Item Price").pack()
entry_item_price = tk.Entry(root)
entry_item_price.pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack()

tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=5)

label_total = tk.Label(root, text="Total: $0")
label_total.pack()

tk.Button(root, text="Check Approval", command=check_approval).pack(pady=5)

label_status = tk.Label(root, text="Status: ")
label_status.pack()

label_ref = tk.Label(root, text="Approval Ref: ")
label_ref.pack()

root.mainloop()