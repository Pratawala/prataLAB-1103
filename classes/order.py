from OrderLine import OrderLine
from product import Product
from classes.DiscountStrategy import DiscountStrategy
from classes.Nodiscount import Nodiscount


class Order: #order is context, DO NOT inherit from discount strategy 
    def __init__(self, order_id: int, discount_strategy: DiscountStrategy):
        self.order_id: int = order_id
        self.order_lines: list[OrderLine] = []
        self.discount_strategy: DiscountStrategy = discount_strategy or Nodiscount() # pass specified discount strategy, defaults to Nodiscount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) #creating orderline object
        self.order_lines.append(order_line)

    def set_discount_strategy(self, discount_strategy: DiscountStrategy) -> None: # pass discount strategy
            self.discount_strategy = discount_strategy

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)