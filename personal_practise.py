class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack 
    def getName(self):
        return self.__name
    def getBasic_attack(self):
        return self.__basic_attack
    def getHealth(self):
        return self.__health
    def setHealth(self, health):
        if health < 0:
            health = 0
        else:
            self.__health = health
    def is_alive(self):
        if self.__health > 0:
            return True
        else:
            return False
    def take_damage(self, damage):
        self.__health = self.__health - damage

char1 = Character("god", 100, 12)
char2 = Character("Stacey", 100, 17)

turn = 0
while char1.is_alive() and char2.is_alive():
    #god attacks
    print("Turn: ",turn)
    if turn % 2 == 0:
        char2.take_damage(char1.getBasic_attack())
        print(f"{char1.getName()} deals {char1.getBasic_attack()} damage to {char2.getName()}")
        print(f"{char2.getName()} has {char2.getHealth()} health left")
    #Stacey attacks
    else:
        char1.take_damage(char2.getBasic_attack())
        print(f"{char2.getName()} deals {char2.getBasic_attack()} damage to {char1.getName()}")
        print(f"{char1.getName()} has {char1.getHealth()} health left")

    turn +=1

if char1.is_alive():
    print(f"{char1.getName()} wins")
else:
    print(f"{char2.getName()} wins")
    


        
        


    


        
        

