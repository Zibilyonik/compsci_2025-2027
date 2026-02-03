def purchase():
    user_input = int(input("How much money does your wallet contain? "))
    price =  int(input("What's the price of your item? "))
    money_left = user_input - price
    while money_left < user_input:
        print("Your purchase is complete! Are you done? ")
        if price == 'done' or 'DONE' or 'Done':
            print("Amount of money left in wallet: ", money_left,)
            break
        if money_left > user_input or money_left == 0:
            print("Amount of money left in wallet: ", money_left, )
            break
purchase()




