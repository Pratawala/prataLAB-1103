import json
from pathlib import Path

class Product:
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_id(self):
        return self.__product_id #returns product id to exe code so idn to do name mangling 


    def add_stock(self, quantity):
        self.__stock += quantity

    def update_details(self, name, price): #updating attribues of product object
        self.__name = name
        self.__price = price

    def to_list(self): #returning as list so json can handle
        return [self.__product_id, self.__name, self.__price, self.__stock]

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} "
              f"| Price: {self.__price} | Stock: {self.__stock}")


class Inventory:
    def __init__(self, file):
        self.__file = file

    def add_product(self, product_id, name, price, stock):
        products = self.__file.load_products()
        products.append(Product(product_id, name, price, stock))
        self.__file.save_products(products)

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
        for product in products:
            product.display_information()  # same, using self.__file.load_products()


    def save_product(self, updated):
        products = self.__file.load_products()
        for i, product in enumerate(products):
            if product.get_id() == updated.get_id():
                products[i] = updated
                break
        self.__file.save_products(products)


class File:
    def __init__(self, filename="inventory.json"):
        base_dir = Path(__file__).resolve().parent #sets the creation directory to module's directory
        self.__filename = base_dir / filename

    def initialise_database(self): #trys inventory.json, creates it if not found
        try:
            with open(self.__filename, "r"):
                print("inventory.json found")
        except FileNotFoundError:
            with open(self.__filename, "w") as f:
                json.dump([], f)
            print("inventory.json created")

    def load_products(self):
        with open(self.__filename, "r") as f:
            return [Product(*row) for row in json.load(f)]

    def save_products(self, products):
        with open(self.__filename, "w") as f:
            json.dump([p.to_list() for p in products], f)