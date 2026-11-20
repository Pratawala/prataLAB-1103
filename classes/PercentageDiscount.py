from classes.DiscountStrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.__percentage = percentage # define attributes unique to each subclass here

    def apply(self, total: float) -> float: 
        if total <= 0:
            raise ValueError("Total must be greater than zero")

        elif self.__percentage <= 0 or self.__percentage>= 1:
            raise ValueError("Discount must be ≥ 0 or ≤ 1 !")

        else:
            total *= 1- self.__percentage 
            return total 