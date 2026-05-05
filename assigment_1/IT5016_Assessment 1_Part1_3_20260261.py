def add_requisition():
    
    # say to user to inter details
    print("Enter your information:")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")
    
    # make the req_id
    counter = 1
    req_id = 10000 + counter
    print("Requisition ID:", req_id)

    # emty list to store total
    items = []

    # first item appear
    item_name = input("Enter item name: ")
    item_price = int(input("Enter item price: "))

    # adding item to list distionary
    items.append({"name": item_name, "price": item_price})
    
    # add the first item price
    total = item_price  

    # Loop add mor item
    for i in range(1000000):
        next_item = input("Add another item (yes/no): ")

        # user add more item
        if next_item.lower() == "yes":
            name = input("Enter item name: ")
            price = int(input("Enter item price: "))
            
            # add item price and update total
            items.append({"name": name, "price": price})
            total += price
        else:
            # stop loop
            break

    # total appear
    print("Total: $", total)

    # Call function
    status, ref_id = requisition_approval(staff_id, req_id, total)

    # Display all details
    display_requisitions(date, staff_id, staff_name, req_id, total, status, ref_id)


def requisition_approval(staff_id, req_id, total):

    # ststus
    status = "Pending"

    # If total less then 500 so approved
    if total < 500:
        status = "Approved"
        # Create reference ID last 3 desit
        ref_id = staff_id + str(req_id)[-3:]
    else:
        # else panding
        status = "Pending"
        ref_id = "Not Assigned"

    return status, ref_id


def display_requisitions(date, staff_id, staff_name, req_id, total, status, ref_id):

    # praint all the details
    print("\nPrinting requisitions:")
    print("Date:", date)
    print("Requisition ID:", req_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total $", total)
    print("Status:", status)
    print("Approval Reference Number:", ref_id)


# Start the program
add_requisition()