from classes.DiscountStrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.__percentage = percentage # define attributes unique to each subclass here

    def apply(self, total: float) -> float: 
        total *= 1- self.__percentage 
        return total 