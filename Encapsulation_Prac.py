#Encapsulation practice

class hero_speed:
    def __init__(self,speed):
        self.speedA = 5
        self._speedB = 10
        self.__speedC= 15
    def printSpeedC(self):
        print(self.__speedC)

speed = hero_speed('speed')
print(speed.speedA)
print(speed._speedB)
speed.printSpeedC()
