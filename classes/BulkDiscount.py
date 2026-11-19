from classes.DiscountStrategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self,threshold: int, discount: int):
        self.__threshold = threshold
        self.__discount = discount

    def apply(self, total: float) -> float: 
        count = total // self.__threshold
        bulk_discount = self.__discount * count 
        total -= bulk_discount 
        return total
        