from classes.product import Product


class OrderLine:
    def __init__(self,product: Product, quantity: int):
        super.product = product 
        super.quantity = quantity

    def calculate_subtotal(product,quantity) -> float:
        return product * quantity 