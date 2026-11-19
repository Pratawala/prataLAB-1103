from product import Product 

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

