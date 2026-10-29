import json

class Product:
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_id(self):
        return self.__product_id #returns product id to exe code so idn to do name mangling 

    def update_stock(self, quantity):#updating stock count of product object
        self.__stock += quantity

    def update_details(self, name, price): #updating attribues of product object
        self.__name = name
        self.__price = price

    def to_list(self): #returning as list so json can handle
        return [self.__product_id, self.__name, self.__price, self.__stock]

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} "
              f"| Price: {self.__price:.2f} | Stock: {self.__stock}")


class Inventory:
    def __init__(self):
        self.__products = []          # starts empty

    def to_list(self):
        return [product.to_list() for product in self.__products] #converting the whole product to list for JSON

    def add_product(self, product_id, name, price, stock): 
        new_product = Product(product_id, name, price, stock) # calls product class -> has attributes of items defined
        self.__products.append(new_product) #appends new product to the product list

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    def display_all(self):
        for product in self.__products:
            product.display_information()


class File:
    def __init__(self, filename="inventory.json"):
        self.__filename = filename

    def initialise_database(self):
        try:
            with open(self.__filename, "r"):
                print("inventory.json found")
        except FileNotFoundError:
            with open(self.__filename, "w") as f:
                json.dump([], f)
            print("inventory.json created")

    def save_item(self, data):
        with open(self.__filename, "w") as f:
            json.dump(data, f)

    def load_item(self):
        with open(self.__filename, "r") as f:
            return json.load(f)