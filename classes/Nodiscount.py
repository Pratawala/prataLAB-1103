from classes.DiscountStrategy import DiscountStrategy

class Nodiscount(DiscountStrategy):
    # no attributes to define

    def apply(self, total): #no discount, do nothing
        return total 

    