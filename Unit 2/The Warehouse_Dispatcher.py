### Practice task  the software for an Amazon-style warehouse.


Dispatch_Line=[]
Loa_Bay=[]
Issue=False

def place_order(order_id):
    item=input("What item are you shipping today?")
    ids=[order_id, item] 
    Dispatch_Line.append(ids)
    print(f"Order recieved: {ids} is added to queue")
    

def ship_next():
    for m in Dispatch_Line:
        if len(Dispatch_Line)==0:
            print("No orders are in line")
            Num_orderID=int(input("Provide ID of the order: "))
        else:
            x=Dispatch_Line[0]
            Dispatch_Line.pop(0)
            Loa_Bay.append(x)
            print(f"Shipped: {x} is loaded onto truck")
            quality=input(f"Is an order {x} not damaged and has correct adress")
            if quality=="yes" or quality=="Yes":
                break
            else:
                Issue=True
                cancel_last_shipment()
                
        

def cancel_last_shipment():
    if len(Loa_Bay)==0:
        ship_next()
    else:
        k=Loa_Bay.pop()
        Dispatch_Line.insert(0,k)
        print(f"Shipping Cancelled: {k} returned to the front of line")


def view_manifest():
    problem=0
    for id in Dispatch_Line:
            print(f"order {id} is in the Dispatch line")
    for id in Loa_Bay:
        print(f"order {id}  is in the Loading Bay ")
    if Issue==True:
        problem+=1
        print(f"There were {problem} issues")

a=True
while a==True :
    Num_orderID=input("Provide ID of the order: ")
    if Num_orderID=="None":
        a=False
        ship_next()
    else:
        place_order(Num_orderID)



