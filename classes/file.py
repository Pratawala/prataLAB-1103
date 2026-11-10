import json
from pathlib import Path
from classes.physicalproduct import PhysicalProduct
from classes.digitalproduct import DigitalProduct
from classes.supplier import Supplier




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
            kind, *fields = row # first item of row goes into physical/digital. everything else to fields
            *basic , supplier_row = fields # slice basic rows from supplier row
            supplier = Supplier(*supplier_row)  # creates supplier object
            if kind == "physical":
                products.append(PhysicalProduct(*basic, supplier))
            elif kind == "digital":
                products.append(DigitalProduct(*basic, supplier))

            else:
                raise ValueError(f"Unknown product type: {kind}")

        return products

    def save_products(self, products):
        rows = [p.to_list() for p in products]   # if this raises, the file is untouched
        with open(self.__filename, "w") as f:
            json.dump(rows, f)
            #json.dump finishes the job and apend it into json