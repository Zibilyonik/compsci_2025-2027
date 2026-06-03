dispatch_line = []
shipped_stack = []

def add_shipment(item_name, order_address):
    dispatch_line.append([item_name, order_address])
    print(f"Added {item_name}, {order_address} to the shipement queue")
    return None

#add_shipment()

def process_next_shipement():
    if len(dispatch_line) == 0:
        print("No pending orders")
    else:
        shipped_stack.append(dispatch_line.pop(0))
        print(f"Shipped: {shipped_stack[-1][0]}")
    return None

#process_next_shipement()

def verify_last_address():
    if len(shipped_stack) == 0:
        print("No shipments have been processed yet")
    else:
        print(f"The last package was sent to {shipped_stack[-1][1]}")
    return None

#verify_last_address()

def cancel_shipment():
    if len(shipped_stack) == 0:
        print("No shipped items to cancel")
    else:
        dispatch_line.insert(0, shipped_stack.pop(-1))
        print(f"Shipping canceled: {dispatch_line[0][0]} returned to processing")
    return None

#cancel_shipment()

def view_manifest():
    print("Dispatch line: ")
    for item in dispatch_line:
        print(item)
    print("Shipped stack: ")
    for item in shipped_stack:
        print(item)
    return None

#view_manifest()

def Logistics_manager():
    while True:
        print("Logistics manager main menu")
        print("To add a shipment, please press 1")
        print("To process the next shipment, please press 2")
        print("To verify the last address, please press 3")
        print("To cancel the last shipement, please press 4")
        print("To view manifest, please press 5")
        print("To exit, please press 0")
        choice = input("select option:")
        if choice == "1":
            item_name = input("Please enter the name of your order: ")
            order_address = input("Please enter the adress: ")
            add_shipment(item_name, order_address)
        elif choice == "2":
            process_next_shipement()
        elif choice == "3":
            verify_last_address()
        elif choice == "4":
            cancel_shipment()
        elif choice == "5":
            view_manifest()
        elif choice == "0":
            print("Exiting logistics manager")
            break
        else:
            print("invalid command")

Logistics_manager()