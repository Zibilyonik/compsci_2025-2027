
def membership_status(paid):
    if paid == "yes":
        return True
    else:
        return False

membership = membership_status

def total_cost(price):
    if membership == True:
        fullprice = price ** 0.8
        return fullprice   
    else:
        fullprice = price
        return fullprice

def the_final_algorythm(paid,price):
    membership_status(paid)
    total_cost(price)

print(total_cost)
print(the_final_algorythm(input("did you pay yet?"),(input("gimme the price"))))