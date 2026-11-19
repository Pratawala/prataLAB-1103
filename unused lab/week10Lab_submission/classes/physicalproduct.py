from classes.abletoship import AbleToShip
from classes.product import Product 


class PhysicalProduct(Product, AbleToShip): #inheriting interfaces
    def __init__(self, product_id, name, price, stock, weight, supplier): #inherit parents attributes, along with self attri, weight
        super().__init__(product_id, name, price, stock, supplier) #if we dont init parents attri, attribute error will be raised if Physical product tries display info, since parent attributes wont be init
        self.__weight = weight #new attribute added 

    def shipping_cost(self):
        shipping_cost = self.__weight * 0.1 + self.get_price() * 0.1 #calls get_price function from inherited method
        return shipping_cost
    
    def to_list(self):
        return (["physical"] + super().to_list() + 
                [self.__weight, self.get_supplier().to_list()])

    def display_information(self):
        super().display_information()
        print(f"Weight : {self.__weight}") #calls parent method and adds own own method

    def get_fulfilment_info(self):
        print("Product has to be shipped physically")
