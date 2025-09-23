
def membership_status(paid):
    if paid == "yes":
        return True
    else:
        return False

membership = membership_status(input("did you pay yet?"))
payment = 0 
if membership == True:
    payment = str("membership")
else:
    payment = str("high spending habits")

def total_cost(price):
    if membership == True and price > 100:
        fullprice = (price * 0.8)//1
        return "because of your membership and your spending habits all you have to do is pay " + str(fullprice) + " dollars"
    elif membership == True or price > 100:
        fullprice = (price * 0.9)//1
        return "because of your " + payment + " all you have to do is pay " + str(fullprice) + " dollars"
    else:
        return str(price) + " that's a lot. You can have it 20% cheaper if you join our app and spend 100 bucks in here. All you have to do is name your future child by our brand name"

print(total_cost(int(input("gimme the price"))))


