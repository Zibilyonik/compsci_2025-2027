class SmartDevice:
    def __init__(self, name, device_id, is_on, base_power_draw):
        self.__name = name
        self.__device_id = device_id
        self.__is_on = False
        self.__base_power_draw = 0
    def GetName(self):
        return self.__name
    def GetID(self):
        return self.__device_id
    def GetActivityStatus(self):
        return self.__is_on
    def GetBasePowerDraw(self):
        return self.__base_power_draw
    def setID(self, device_id):
        self.__device_id = device_id
    def setIsOn(self, is_on):
        if is_on == bool:
            self.__is_on = is_on
        else:
            print(f"Has to be a boolean")
    def setBasePowerDraw(self, base_power_draw):
        if base_power_draw >= 0:
            self.__base_power_draw = base_power_draw
        else:
            print(f"Base power draw cannot be negative")
    def toggle_power(self, is_on):
        if is_on == True:
            is_on = False
        else:
            is_on = True
    def get_current_usage(self, base_power_draw, is_on):
        if is_on == True:
            return base_power_draw
        else:
            return 0
    
obj1 = SmartDevice("TV", 76500, True, 50)
obj2 = SmartDevice("Fan", 89453, False, 20)
obj3 = SmartDevice("Speaker", 66620, True, 10)

#calculating the total power usage of all the devices combined
def total_power_usage(total_usage):
    total_usage = obj1.get_current_usage + obj2.get_current_usage + obj3.get_current_usage #add all of the power usage up
    print(f"the devices are currently using {total_usage}") 

obj1.toggle_power() #TV gets turned off
obj2.toggle_power() #Fan gets turned on
obj3.toggle_power() #Speakers get turned off



        
        



    
    
    