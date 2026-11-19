from abc import ABC, abstractmethod

class AbleToShip(ABC):
    @abstractmethod
    def shipping_cost(self):
        pass #lets all user of interface decide how they want to implement this
