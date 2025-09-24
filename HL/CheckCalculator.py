
FoodPriceCalc = 0
FullPrice = 10


def FoodPrice(FoodInput):
    try: 

    
    except:
      FoodPrice = False 
    if FoodInput == "Burger":
        FoodPriceCalc1 += 20.99 
        return FoodPriceCalc1
    elif FoodInput == "hot Dog":
        FoodPriceCalc2 += 1.99 
        return FoodPriceCalc2
    elif FoodInput == "chicken" or "kfc" or "Strips":
        FoodPriceCalc3 += 15.99
        return FoodPriceCalc3
    
       return FoodPrice
while FoodPrice == False:
    FoodPrice(input("Go again"))


def eating(now): 
    Expense = Food + FullPrice 
    FullPrice = Expense
    if now == "yes":
        FoodPrice (input("what else do you want to eat?"))
    else: 
        print("your total is " + FullPrice + "dollarinoes")

Food = FoodPrice(input("What food you want"))




while FoodPrice == 15.99 or 1.99 or 20.99:
    eating(input("wanna continue?"))