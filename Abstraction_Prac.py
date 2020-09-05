from abc import ABC, abstractmethod

class guild(ABC):
    def gdebt(self,amount):
        print("You have borrowed: ",amount)
    @abstractmethod
    def payup(self,amount):
        pass

class currencyTransfer(guild):
    def payup(self,amount):
        print("You have borrowed {} and need to pay up".format(amount))

obj = currencyTransfer()
obj.gdebt("50 Exalted")
obj.payup("50 Exalted")
