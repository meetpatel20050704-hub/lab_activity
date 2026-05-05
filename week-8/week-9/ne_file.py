def add_requisition(counter):
    
    print("Enter your information:")
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    requisition_id = 10000 + counter
    print("Requisition ID:", requisition_id)

    items = []
    total = 0

    print("\nAdd items:")

    for i in range(100):
        print("\nItem", i + 1)

        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price ($): "))

        items.append({"name": item_name, "price": item_price})
        total += item_price

        choice = input("Add another item? (yes/no): ")

        if choice.lower() == "yes":
            continue
        else:
            break

    print("\nTotal cost: $", total)

    return {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id,
        "items": items,
        "total": total
    }
    