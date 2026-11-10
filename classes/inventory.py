from classes.digitalproduct import DigitalProduct
from classes.physicalproduct import PhysicalProduct
from classes.product import Product

class Inventory:
    def __init__(self, file):
        self.products: list[Product] = [] #init attribute called product, type hint it as a list that should contain product object and create the list
        self.__file = file

    def add_product(self,product: Product):
        products = self.__file.load_products()
        products.append(product)
        self.__file.save_products(products)
        return products

    # def add_digital_product(self, product):
    #     products = self.__file.load_products()
    #     products.append(product)
    #     self.__file.save_products(products)
    #     return products 

    def search_product(self, product_id: int):
        for product in self.__file.load_products():
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self):
        products = self.__file.load_products()
        if not products:
            print("Inventory is empty!")
            return

        print("\nPhysical Product")
        for product in products:
            if isinstance(product, PhysicalProduct):
                product.display_information()  # same, using self.__file.load_products()

        print ("\nDigital product")
        for product in products:
            if isinstance(product, DigitalProduct):
                product.display_information()

    def save_product(self, updated: bool):
        products = self.__file.load_products()
        for i, product in enumerate(products):
            if product.get_id() == updated.get_id():
                products[i] = updated
                break
        self.__file.save_products(products)

