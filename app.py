import json
from modules import Product, Inventory, File
file = File() #creats a file object "inventory.json"
file.initialise_database() #creates the file if it doesnt exist 
inventory = Inventory(file) # creating the inventory object from the Inventory class passing file 

# first commit kinda nervous!

def get_valid_id():
    while True:
        id_value = input("What is your product ID? (or type 'quit'): ")

        if id_value == "quit":
            return None

        try:
            id_value = int(id_value)
        except ValueError:
            print("------Invalid input, please enter an id of 1000 or more, or type 'quit' to exit------")
            continue

        if id_value < 1000:
            print("------Id starts from 1000!------")
            continue

        return id_value


def get_valid_description():
    while True:
        description_value = input("What item are you processing: ")

        if description_value == "quit": #make sure to call reportfunction 
            print("Cannot quit whilst inputting inventory!")

        try: #nothing to check, string input 
            str(description_value) #just in case 
            return description_value

        except (ValueError, TypeError):
            print("------Please enter a string------")


def get_valid_price():
    while True:
        price_value = input("How much are you selling for?")

        if price_value == "quit":
            print("Cannot quit whilst inputting inventory!")
            continue

        try:
            float(price_value)
            return price_value

        except(ValueError,TypeError):
            print("-----Please enter an valid price!------")


def get_valid_quantity():
    #failed_attempts=0 #place it outside the loop, this variable will be returned once function finish
    while True:
        quantity_value = input("How much quantity do you want to input?")

        if quantity_value == "quit":
            print("-----Cannot quit after entering product description!------")
        try:
            quantity_value = int(quantity_value)

            if quantity_value <= 0:
                print("------Inventory cannot be less than zero------")
                #failed_attempts+=1

            # elif quantity_value + current_product[2] > 500:
            #     print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
            #     failed_attempts +=1

            else:
                return quantity_value


        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            #failed_attempts += 1

def get_physical():
    is_physical = input("Digital or Physical product? ").lower().strip()

    if is_physical == "digital":
        download_size = float(input("How large is your digital product? (MB): "))
        return download_size, False

    elif is_physical == "physical":
        weight = float(input("How heavy is your product? (grams): "))
        return weight, True

    else:
        print("INVALID input! Enter PHYSICAL or DIGITAL.")
        return get_physical()


def update_stock(product_id):
    for product in inventory:
        if product.get_id() == product_id:
            print()
            print("Product found!")
            product.display_information()
            quantity = int(input("Input new stock quantity:"))
            product.update_stock(quantity)
            print()
            print("Stock update successfully!")
            return
        
    # this will only be reached when if statement not touched    
    print("Stock not found!")


# product_id = current_i
# name = product_description
# price = float(price_value)
# stock = int(quantity_value)


def process_delivery(current_id,product_description,price_value,quantity_value): #collect all 3 values of list, quantity tally done here
    good_attempts = 0
    for product in inventory: #current product[id,productName,Quantitytoadd]
        if product[0] == current_id: #grabbing the any product that matches
            product[1] = str(product_description) #updating product name (if any)
            product[2] = float(price_value)
            product[3] = int(current_product[3]) + int(quantity_value) #adds current amount with new amount
            with open("inventory.json", "w") as f:
                    json.dump(inventory, f, )
            print(current_product)
            print("\norders successfully saved to orders.txt")
            # good_attempts+=1
            # return good_attempts#exits loop so we dont clone list by accident 

        else: #is this not just creating new list and assigning vlaues?
            current_product = [
            current_id,
            str(product_description),
            float(price_value),
            int(quantity_value)
        ]
            inventory.append(current_product) # add list 
            with open("inventory.json", "w") as f:
                json.dump(inventory, f, )
            print(current_product)
            print("\nProduct added successfully!")
            # good_attempts+=1
            # return good_attempts



            
#load inventory verified!
#pull json file
#final save verified!
def persistence(): 
    try:
        with open("inventory.json","r") as f:#variable f will be assigned the file opened with flag -r
            print("inventory.json found\nInventory loaded sucessfully")
        inventory=  json.load(f) #convert json file into python, load the python value as "inventory"
        return inventory 

    except (FileNotFoundError):
        inventory = [[1000, "nil",0.0, 0]] #create a variable called inventory
        print("inventory.json created\n Inventory loaded successfully")
        f = open("inventory.json", "w") #create inventory.json file , -w is important
        json.dump(inventory, f) #convert the python value of Inventory into Json 
        f.close()

        return inventory


def search_product():
    product_query = int(input("Enter product ID you are searching for?: "))
    for product in inventory: #iterates through inventory
        if product_query == product[0]: # compare id with ids of product in inventory
             print("-------------------------\n",
             "Product Found!\n" \
             "ID:", product[0],
            "| Name:", product[1],
            "| Price:$", product[2],
            "| stock", product[3])

        else:
            print("Product not found!")

        
def load_inventory(inventory):
    print("\n------ Current Inventory ------")

    for product in sorted(inventory, key=lambda product: product[0]):
        print("ID:", product[0],
              "| Name:", product[1],
              "| Price:$", product[2],
              "| stock", product[3])


def welcome_screen():

    while True:
        

        
        welcome_screen_input=input("\nSelect option:")

        try:
            welcome_screen_input = int(welcome_screen_input) #changing value into an integer
            if welcome_screen_input >0 and welcome_screen_input <7:
                return welcome_screen_input #only break condition to break the loop     

            else:
                print("Select an option within menu!")

        except TypeError, ValueError:
            print("Select an option within menu!")


def save_inventory():
    print("Saving Inventory...," \
    "Inventory saved successfully to inventory.json")



def exit_message():
    print("\n Saving inventory before exit..." \
    "Inventory saved successfully."\
        \
    "Thank you for using Inventory Management System."\
    "Program terminated")


#init values 
failed_attempts = 0
total_tax = 0
total_good_attempts = 0
failed_id = 0
failed_quantity = 0
total_units = 0

print("\n----------- MENU -----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4."
            "Search Product\n5. Save Inventory\n6. Exit\n----------------------------")

while True:
    #reset variabele (so you dont carry value of each iteration over)
    current_product = []
    product_description = " "
    quantity_value = 0
    price_value = 0.0

    
    option = welcome_screen()

    if option == 1:
        inventory.display_all()
        continue


# sample of creating inventory in OOP
# product1 = Product("P001", "Laptop", 1200.00, 15) # creating product from Product class, via init
# product2 = Product("P002", "Mouse", 25.50, 40)
# inventory.add_product(product1) # pass the product to inventory class to store in a list
# inventory.add_product(product2)
# each action already saves itself
    if option == 2:

        print("add new product")
        
        current_id = get_valid_id()
        product_description = get_valid_description()
        price_value = get_valid_price()
        quantity_value = get_valid_quantity()
        weight_or_size, is_physical = get_physical() #unpacking [size, boolean]
       
        
        product = inventory.search_product(current_id)

        if product is None and is_physical == True:
            inventory.add_physical_product(current_id, product_description, price_value, quantity_value, weight_or_size)
            print("PHYSICAL product added successfully!")
            product = inventory.search_product(current_id) #search for the product after it already exist to call child method
            product.get_fulfilment_info()
            print(f"shipping fee: ${product.shipping_cost()}")

        elif product is None and is_physical == False:
            inventory.add_digital_product(current_id, product_description, price_value, quantity_value, weight_or_size)
            print("digital Product added successfully!")
            product = inventory.search_product(current_id)
            product.get_fulfilment_info()

        else:
            product.update_details(product_description, price_value)
            product.add_stock(quantity_value)
            inventory.save_product(product)
            print("Delivery recorded successfully!")

        continue

    if option == 3:
        print("update stock")
        current_id = get_valid_id()
        if current_id is None:
            continue
        product = inventory.search_product(current_id)
        if product is None:
            print("Stock not found!")
        else:
            product.display_information() #calss display information method from class prduct
            product.add_stock(int(input("Input new stock quantity: ")))
            inventory.save_product(product)
            print("Stock updated successfully!")
        continue

    if option == 4:
        product_id = get_valid_id()
        product = inventory.search_product(product_id)
        if product is None:
            print("Product not found!")
        else:
            print("-------------------------")
            print("Product Found!")
            product.display_information()
        continue

    if option == 5:
        print("Inventory saved successfully!")
        continue

    if option ==6: 
        exit_message()
        break




  

    # ----------------------------------------------------------------
    # done
    # persistent() is done (load inventory function is this )
    # id funciton is done
    #added the two other function
    #converted the rest of quantity funciton to grep 

    #existing list value should be overwritten, not create a new one!
    #fix whatever is making my code print instead of amend

    # ----------------------------------------------------------------
    #to do
    #finish up report generation
    

    
