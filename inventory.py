from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct

class Inventory:
    def __init__(self, file):
        self.__file = file

    def add_physical_product(self, product_id, name, price, stock, weight):
        products = self.__file.load_products()
        products.append(
            PhysicalProduct(product_id, name, price, stock, weight) #creates object P product based on class P product
            )
        self.__file.save_products(products)
        return products

    def add_digital_product(self, product_id, name, price, stock, download_size):
        products = self.__file.load_products()
        products.append(
            DigitalProduct(product_id, name, price, stock, download_size) #same  but for digital
            )
        self.__file.save_products(products)
        return products 

    def search_product(self, product_id):
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



    def save_product(self, updated):
        products = self.__file.load_products()
        for i, product in enumerate(products):
            if product.get_id() == updated.get_id():
                products[i] = updated
                break
        self.__file.save_products(products)

