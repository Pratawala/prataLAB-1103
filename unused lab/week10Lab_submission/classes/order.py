from OrderLine import OrderLine
from product import Product


class Order:
    def __init__(self, order_id: int):
        self.order_id: int = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) #creating orderline object
        self.order_lines.append(order_line)
