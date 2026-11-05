import json
from pathlib import Path
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct




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