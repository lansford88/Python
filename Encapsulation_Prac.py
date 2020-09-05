#Encapsulation practice

class hero_speed:
    def __init__(self,speed):
        self.speedA = 5
        self._speedB = 10
        self.__speedC= 15

speed = hero_speed('speed')
print(speed.speedA)
print(speed._speedB)            #still private, but nothing stops you from accessing the attribute
print(speed.__speedC)           #this will make the attribute private
