
def the_final_algorythm(paid,price):
   def membership_status(paid):
    if paid == "yes":
        return True
    else:
        return False
   def total_cost(price):
     if membership_status(paid) == True:
        fullprice = price ** 0.8
        return fullprice   
     else:
        fullprice = price
        return fullprice
     
print(the_final_algorythm(input("did you pay yet?"),int((input("gimme the price")))))