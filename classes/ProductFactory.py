from classes.supplier import Supplier
from classes.product import Product
from classes.physicalproduct import PhysicalProduct
from classes.digitalproduct import DigitalProduct
from classes.abletoship import AbleToShip


class ProductFactory:
    @staticmethod
    def create( self,product_id :str, name: str, price: float, stock: int, supplier: Supplier, product_type: str) -> Product:
        if product_type == "physical":
            return PhysicalProduct(AbleToShip, product_id, name, price, stock, supplier)
        elif product_type == "digital":
            return DigitalProduct(AbleToShip, product_id, name, price, stock, supplier)
        else:
            raise ValueError(f"Unknown Product Type: {product_type}")