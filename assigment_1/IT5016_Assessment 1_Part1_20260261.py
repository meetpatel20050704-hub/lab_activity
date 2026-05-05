import tkinter as tk
from tkinter import messagebox

# make the main window
root = tk.Tk()
root.title("Requisition System")   # title
root.geometry("500x600")           # size

# virable
counter = 1              # make the uniq id and add 1 every time requisition ID
item_entries = []        # total emety store


# function start
def add_item_fields():

    # check the condiction the staff name and id are add or not 
    if not entry_staff_id.get() or not entry_staff_name.get():
        messagebox.showerror("Error", "Enter Staff ID and Name first")
        return

    # for the row creat farme
    frame = tk.Frame(frame_items)
    frame.pack(pady=2)

    # placeholder
    entry_name = tk.Entry(frame, width=20)
    entry_name.insert(0, "Enter item name")
    entry_name.pack(side=tk.LEFT, padx=5)

    # worke when we click the placeholder item_name
    def clear_name(event):
        if entry_name.get() == "Enter item name":
            entry_name.delete(0, tk.END)

    entry_name.bind("<FocusIn>", clear_name)

    # invisibale placeholder for the price
    entry_price = tk.Entry(frame, width=20)
    entry_price.insert(0, "Enter item price")
    entry_price.pack(side=tk.LEFT, padx=5)

    # when we click it is work
    def clear_price(event):
        if entry_price.get() == "Enter item price":
            entry_price.delete(0, tk.END)

    entry_price.bind("<FocusIn>", clear_price)

    # store all the item list
    item_entries.append((entry_name, entry_price))


# total price 
def calculate_total():

    # all the staff details 
    if not entry_staff_id.get() or not entry_staff_name.get():
        messagebox.showerror("Error", "Enter Staff ID and Name first")
        return

    total = 0

    # Loop 
    for name_entry, price_entry in item_entries:
        try:
            price = int(price_entry.get())  # in int price
            total += price                 # total
        except:
            continue  # not give answer inviled input

    # update the total
    label_total.config(text=f"Total: ${total}")
    return total


# check approveal resualt
def check_approval():
    global counter

    # valid input
    if not entry_staff_id.get() or not entry_staff_name.get():
        messagebox.showerror("Error", "Enter Staff ID and Name first")
        return

    total = calculate_total()

    # add the id in end
    req_id = 10000 + counter
    counter += 1

    staff_id = entry_staff_id.get()

    # approvel<500
    if total < 500:
        status = "Approved"
        ref_id = staff_id + str(req_id)[-3:]   # print last 3 digit
    else:
        status = "Pending"
        ref_id = "Not Assigned"

    # give the output
    output_box.delete(1.0, tk.END)

    # show resualt
    output_box.insert(tk.END, "Printing requisitions:\n\n")
    output_box.insert(tk.END, f"Requisition ID: {req_id}\n")
    output_box.insert(tk.END, f"Staff ID: {staff_id}\n")
    output_box.insert(tk.END, f"Staff Name: {entry_staff_name.get()}\n")
    output_box.insert(tk.END, f"Total $ {total}\n")
    output_box.insert(tk.END, f"Status: {status}\n")
    output_box.insert(tk.END, f"Approval Reference Number: {ref_id}\n")


# staffe information
tk.Label(root, text="Date").pack()
entry_date = tk.Entry(root)
entry_date.pack()

tk.Label(root, text="Staff ID").pack()
entry_staff_id = tk.Entry(root)
entry_staff_id.pack()

tk.Label(root, text="Staff Name").pack()
entry_staff_name = tk.Entry(root)
entry_staff_name.pack()


#item for frame
frame_items = tk.Frame(root)
frame_items.pack(pady=10)


# button fram
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# button in worke mode
tk.Button(frame_buttons, text="Add Item", command=add_item_fields).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Calculate Total", command=calculate_total).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Check Approval", command=check_approval).pack(side=tk.LEFT, padx=5)


# show total
label_total = tk.Label(root, text="Total: $0")
label_total.pack()


# outputbox
output_box = tk.Text(root, height=12)
output_box.pack(pady=10)


# call the fuction worke all windo
root.mainloop()