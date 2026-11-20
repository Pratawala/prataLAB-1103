from classes.product import Product


class OrderLine:
    def __init__(self,product: Product, quantity: int):
        super.product = product 
        super.quantity = quantity
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def calculate_subtotal(product,quantity) -> float:
        return product * quantity 