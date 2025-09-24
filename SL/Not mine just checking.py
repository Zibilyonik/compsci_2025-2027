user_continue = True
while user_continue:
    validInput = False
    while not validInput:
        # Get user input
        try:
            num1 = int(input("What is number 1?"))
            num2 = int(input("What is number 2?"))
            operation = int(input("What do you want to do with these? 1. add, 2. subtract, 3. multiply 4. divide. Enter number:"))
            validInput = True
        except:
            print("Invalid Input. Please try again.")
    if(operation == 1):
        print("Adding...")
        print(add(num1, num2))
    elif(operation == 2):
        print("Subtracting...")
        print(sub(num1, num2))
    elif(operation == 3):
        print("Multiplying...")
        print(mul(num1, num2))
    elif(operation == 4):
        print("Dividing...")
        print(div(num1, num2))
    else:
        print("I don't understand. Please try again.")
    user_yn = input('Would you like to do another calculation? ("y" for yes or any other value to exit.)')
    if(user_yn == 'y'):
        continue
    else:
        break