import json

# first commit kinda nervous!

def get_valid_id():
    failed_attempts_id = 0
    while True:
        id_value = input("What is your product ID ?")

        if id_value == "quit":
            return "quit", failed_attempts_id

        try:
            id_value = int(id_value)

            if id_value < 1000:
                print("------Id starts from 1000!------")
                failed_attempts_id +=1

            else:
                for product in inventory: #product is the inner list of the list inventory 
                    if id_value == product[0]: #search the id of each inner list against the list of product
                        return product, failed_attempts_id
                        

                    else:
                        new_product = id_value
                        return new_product , failed_attempts_id
                     
        except (ValueError, TypeError):
            print("------Invalid input, please enter an id greater than 1000 or type 'quit' to exit------")
            failed_attempts_id += 1


def get_valid_description(description_value):
    while True:
        description_value = input("What item are you processing: ")

        if description_value == "quit": #make sure to call reportfunction 
            print("Cannot quit whilst inputting inventory!")

        try: #nothing to check, string input 
            str(description_value) #just in case 
            return description_value

        except (ValueError, TypeError):
            print("------Please enter a string------")


def get_valid_price(price_value):
    while True:
        price_value = input("How much are you selling for?")

        if price_value == "quit":
            print("Cannot quit whilst inputting inventory!")

        try:
            float(price_value)
            return price_value

        except(ValueError,TypeError):
            print("-----Please enter an valid price!------")


def get_valid_quantity(quantity_value):
    failed_attempts=0 #place it outside the loop, this variable will be returned once function finish
    while True:
        quantity_value = input("How much quantity do you want to input?")

        if quantity_value == "quit":
            print("-----Cannot quit after entering product description!------")
        try:
            quantity_value = int(quantity_value)

            if quantity_value <= 0:
                print("------Inventory cannot be less than zero------")
                failed_attempts+=1

            # elif quantity_value + current_product[2] > 500:
            #     print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
            #     failed_attempts +=1

            else:
                return quantity_value,failed_attempts


        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            failed_attempts += 1


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

def update_stock(product_id):
    for product in inventory:
        if product_id == product[0]:
            print()
            print("Product found | Name:",product[1],"| Current Stock:",product[3])
            product[3] = input("Input new stock Quantity: ")
            print()
            print("Stock update successfully!")
            return
        
    # this will only be reached when if statement not touched    
    print("Stock not found!")
            
#load inventory verified!
#pull json file
#final save verified!
def persistence(): 
    try:
        f = open("inventory.json", "r") #variable f will be assigned the file opened with flag -r
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
inventory = persistence() #loads inventory from json file, create file if not there

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
        load_inventory(inventory)
        continue

    if option == 2:
        print("add new product")
        current_id = get_valid_id()[0]#specify first value as function returns >1 value
        product_description = get_valid_description(product_description)
        price_value = get_valid_price(price_value)
        quantity_value = get_valid_quantity(quantity_value)[0]#specify first value as function returns >1 value
        process_delivery(current_id,product_description,price_value,quantity_value) 
        continue

    if option == 3:
        print("update stock")
        current_id = get_valid_id()[0]#specify first value as function returns >1 value
        update_stock(current_id)
        continue

    if option == 4:
        search_product()
        continue

    if option == 5:
        save_inventory()
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
    

    
