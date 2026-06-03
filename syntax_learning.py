
#balance
#History
#Name
#show_balance()
#withdraw
#deposit()
#object = BankAccount("username")

class BankAccount: #class names start with capital latters, and have capital letters 
    def _init_(self, name, balance= 0, history= []): #double under functions aka Dunder functions, they remove default behaviour of functionality
        self.name= name 
        self.history = history
        self.balance = balance 
    def show_balance(self):
        print(f"Your bank account has {self.balance} money")
    def diposit(self, amount):
        self.balance += amount
        print(f"Deposit successful, you now have  {self.balance} in your account")
    def withdraw(self, amount):
        if self.balance < amount: 
            print(f"You only have {self.balance} in your account, you cannot whitdraw {amount}")
        else:
            self.balance -= amount
            print(f"You whitdrew {amount}, you now have {self.balance}")


my_account = BankAccount("NAC")
my_account.balance 

#my own attempt:
class Backpack:
    def _init_(self, name, contents = 0):
        self.name = name
        self.contents = contents
    def show_contents(self):
        print(f"your backpack has {self.contents} inside")
    def insert(self, item):
        self.contents += item
        print(f"you have put {self.contents} in your backpack")
    def remove(self, item):
        if self.contents < item:
            print(f"there is nothing in your backpack to retrieve")
        else:
            self.contents -= item
            print(f"you retrieved {item} from your backpack")

#diff shi
class Actor:
    number_of_actors = 0
    Actors = []
    def __init__(self, name):
        self.name =  name
        self.__charisma = 0
        self.__popularity = 0
        self.__availability = True 
        self.number_of_actors += 1
    def getCharisma(self):
        return self.__charisma
    def getPopularity(self):
        return self.__popularity
    def setAvailability(self, availability):
        self.__availability = availability
        if self.__availability == True:
            print(f"{self.name} is available")
        else:
            print(f"{self.name} is unavailable")
    def __str__(self):
        return f"{self.name} has {self.__charisma} and {self.__popularity}. {self.__availability}"

    

