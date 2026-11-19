

class Supplier:
    def __init__(self, supplier_id, supplier_name, contact_email):
        self.__supplier_id = supplier_id 
        self.__supplier_name = supplier_name
        self.__contact_email = contact_email 

    def get_id(self): # allows accessing of attributes by other classes
        return self.__supplier_id

    def to_list(self):
        return [self.__supplier_id, self.__supplier_name, self.__contact_email]

    def display_information(self):
        print(f"supplier id: {self.__supplier_id}, name: {self.__supplier_name}, contact email: {self.__contact_email}")