import json
from pathlib import Path
from abc import ABC, abstractmethod

class AbleToShip(ABC):
    @abstractmethod
    def shipping_cost(self):
        pass #lets all user of interface decide how they want to implement this

class Product(ABC):
    def __init__(self,product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @abstractmethod #this has to be implemented by child class in its own way
    def get_fulfilment_info():
        pass

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

    def get_price(self):
        return int(self.__price) 

class PhysicalProduct(Product, AbleToShip): #inheriting interfaces
    def __init__(self, product_id, name, price, stock, weight): #inherit parents attributes, along with self attri, weight
        super().__init__(product_id, name, price, stock) #if we dont init parents attri, attribute error will be raised if Physical product tries display info, since parent attributes wont be init
        self.__weight = weight #new attribute added 

    def shipping_cost(self):
        shipping_cost = self.__weight * 0.1 + self.get_price() * 0.1 #calls get_price function from inherited method
        return shipping_cost
    
    def to_list(self):
        return super().to_list() + ["physical", self.__weight]

    def display_information(self):
        super().display_information()
        print(f"Weight : {self.__weight}") #calls parent method and adds own own method

    def get_fulfilment_info(self):
        print("Product has to be shipped physically")


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size #Defining child's own attribute 

    def to_list(self):
        return super().to_list() + ["digital", self.__download_size] #appends digital and downlaod size when loading into list 

    def display_information(self): #child method will always take precedence 
        super().display_information() #specify to use parent method here 
        print(f"Download Size: {self.__download_size}") #adds own method on top of parent downlaod size

    def get_fulfilment_info(self):
        print("Product has to be shipped DIGITALLY")



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
            data = json.load(f)

        products = []
        #creating Physical/Digitalproduct object according to phy/dig
        for row in data:
            if row[4] == "physical":
                products.append(PhysicalProduct(*row[:4], row[5]))

            elif row[4] == "digital":
                products.append(DigitalProduct(*row[:4], row[5])) #append product object, use list slicing to feed values into object attributes

            else:
                raise ValueError(f"Unknown product type: {row[4]}")

        return products

    def save_products(self, products):
        with open(self.__filename, "w") as f:
            json.dump([p.to_list() for p in products], f)#p to list converts each iteration from object to python list
            #json.dump finishes the job and apend it into json