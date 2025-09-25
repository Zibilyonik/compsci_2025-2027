
FullPrice = 10
FoodPriceCalc1 = 0 
FIL = ["Burger","hot Dog","chicken","kfc","Strips"]
Inp = "x"

def FoodPrice(FoodInput): 
    continueation = False
    while continueation == False:
        Inp = input("Try again")
        if Inp in FIL:
            continueation = True
        else:
            continueation = False

    if continueation == True:

        if FoodInput == "Burger":
            FoodPriceCalc = 20.99
            return FoodPriceCalc
        elif FoodInput == "hot Dog":
            FoodPriceCalc = 1.99 
            return FoodPriceCalc
        elif FoodInput == "chicken" or "kfc" or "Strips":
            FoodPriceCalc = 15.99
            return FoodPriceCalc
        else:
            continueation = False
            return continueation
        


NewInp = (input("What food you want"))
Food = FoodPrice(Inp)
FoodPriceCalc1 += Food

def eating(now): 
        
    if now == "yes":
        FoodPrice (input("what else do you want to eat?"))
    else: 
        Inp = "BOOOOOOOMM"
        return Inp
NewInp = eating()

    
while Inp in FIL:
        eating(input("wanna continue?"))
        
       


        