from classes.product import Product 

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size,supplier):
        super().__init__(product_id, name, price, stock,supplier)
        self.__download_size = download_size #Defining child's own attribute 

    def to_list(self):
        return (["digital"] + super().to_list()
                + [self.__download_size, self.get_supplier().to_list()])

    def display_information(self): #child method will always take precedence 
        super().display_information() #specify to use parent method here 
        print(f"Download Size: {self.__download_size}") #adds own method on top of parent downlaod size

    def get_fulfilment_info(self):
        print("Product has to be shipped DIGITALLY")

