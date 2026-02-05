user_count = int(input("How many iterations? "))
for x in range (1, user_count): #[0, 2, 4, 5]: 
    if x % 2 == 0:
        print(f"number {x} is divisible by 2")
    else:
        print(f"number {x} is not divisible by 2")

user_while_count = int(input("what's the max value? "))
counter = 0

while counter <= user_while_count:
    if counter % 2 == 0:
        print(f"number {counter} is divisible by 2")
    else:
        print(f"number {counter} is not divisible by 2")
    counter = counter + 1
 
