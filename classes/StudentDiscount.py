from classes.DiscountStrategy import DiscountStrategy
from classes.PercentageDiscount import p

class StudentDiscount(DiscountStrategy):
    def __init__(self, student: bool):
        self.__student = student

    def apply(self, total: float ) -> float:
        if self.__student :
            total *= 0.75 # students get 25% off

        return total

    

