import json
from pathlib import Path
from abc import ABC, abstractmethod
from abletoship import AbleToShip


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







