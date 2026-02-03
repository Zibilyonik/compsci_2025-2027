#Define function which calculates discount against provided amount
#function shall take 2 parameters as input: amount and discount_type
#function shall return discounted amount dependent from discount_type
#for discount_type equal to 'small' it shall consider 10% of discount, for 'medium' 20% and for 'high' 30% of the discount

def discount_calculator(amount, discount_type):
  

    if discount_type == 'small':
        discounted_amount = 0.9 * amount 
    elif discount_type == 'medium':
        discounted_amount = 0.8 * amount
    elif discount_type == 'high':
        discounted_amount = 0.7 * amount
    else:
        discounted_amount = amount 

    return discounted_amount 

print("Discounted amount: ", discount_calculator(900,'small')) 
print("Discounted amount: ", discount_calculator(9,'medium'))
print("Discounted amount: ", discount_calculator(9,'high')) 
print("Discounted amount: ", discount_calculator(9,'ass'))  

#new
def character_counter(random_stuff ):
    return len(random_stuff.strip())


print(character_counter(' Ala ma duck   '))

#new
user_input = input("Podaj swój tekst: ")
print("Twój tekst to: ", user_input, " , długość tekstu bez zewnętrznych spacji to: ", character_counter(user_input))

