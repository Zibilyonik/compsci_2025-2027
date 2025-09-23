
def membership_status(paid):
    if paid == "yes":
        return True
    else:
        return False

membership = membership_status(input("did you pay yet?"))

def total_cost(price):
     if membership == True:
        fullprice = (price * 0.8)//1
        return "because of your membership all you have to do is pay " + str(fullprice) + " dollars"
     else:
        return str(price) + " that's a lot. You can have it 20% cheaper if you join our app. All you have to do is name your future child by our brand name"

print(total_cost(int(input("gimme the price"))))


