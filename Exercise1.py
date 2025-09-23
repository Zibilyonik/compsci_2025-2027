def discount_calculate(basket_value):
    discount_total = basket_value * 0.1
    return discount_total

def membership_discount_calculate(basket_value):
    membership_discount_total = basket_value * 0.2
    return membership_discount_total

def membership_discount_check(is_member,membership_discount_total,discount_total,basket_value):
    if is_member==True:
        return membership_discount_total 
    else:
        return basket_value
    
def discount_check(basket_value):
        if basket_value>100:
            return True
        else:
            return False
        
def shopping_experience_old(basket_value):
     total_cost = basket_value
     if discount_check(basket_value):
          discount_total = discount_calculate(basket_value)
          total_cost = basket_value - discount_total
          return total_cost
     
def final_disocunt(basket_value, is_member):
    if is_member==True and basket_value>100:
        return basket_value - (basket_value * 0.2)
    elif is_member==True or basket_value>100:
        return basket_value - (basket_value * 0.1)
    else:
        return basket_value

        
