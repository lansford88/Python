
class characters:
    name = "Unknown"
    ability = ' '
    speed = 0

    def info(self):
        msg = "\nName: {}\nAbility: {}\nSpeed: {}".format(self.name,self.ability,self.speed)
        return msg

#child class instance
class Fighter_A(characters):
    name = "Boba"
    ability = 'Flight and Fire'
    speed = 9

        
    def flight_based(self):
        msg = "\nBoba has the ability to fly and create fire balls to rain down on his foes"
        return msg
    

#child class instance
class Fighter_B(characters):
    name = "Lizzy"
    ability = 'Corruption and Traps'
    speed = 4
        
    
    def pure_corruption(self):
        msg = "\nLizzy has the ability to spread corruption and weaken her enemies and make them vulnerable to her deadly traps"
        return msg
        



if __name__ == "__main__":
    fighterA = Fighter_A()
    print(fighterA.info())
    print(fighterA.flight_based())
    

    fighterB = Fighter_B()
    print(fighterB.info())
    print(fighterB.pure_corruption())
    





    
