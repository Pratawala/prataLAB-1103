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
                        new_product = [id_value,"---Pending Description---",0]
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

            elif quantity_value + current_product[2] > 500:
                print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
                failed_attempts +=1

            else:
                return quantity_value,failed_attempts


        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            failed_attempts += 1


def process_delivery(current_id,product_description,quantity_value): #collect all 3 values of list, quantity tally done here
    good_attempts = 0
    for product in inventory: #current product[id,productName,Quantitytoadd]
        if product[0] == current_id: #grabbing the any product that matches
            product[1] = str(product_description) #updating product name (if any)
            product[2] = int(current_product[2]) + int(quantity_value) #adds current amount with new amount
            with open("inventory.json", "w") as f:
                    json.dump(inventory, f, )
            print(current_product)
            print("\norders successfully saved to orders.txt")
            good_attempts+=1
            return good_attempts#exits loop so we dont clone list by accident 

    else:
            current_product[1]= str(product_description)
            current_product[2]= int(quantity_value)
            inventory.append(current_product) #add list if no match
            with open("inventory.json", "w") as f:
                json.dump(inventory, f, )
            print(current_product)
            print("\norder successfully saved to orders.txt")
            good_attempts+=1
            return good_attempts


    


def calculate_tax(quantity_value):
    taxable_amount = quantity_value *0.10
    return taxable_amount 
#staged

def generate_report(failed_id,failed_quantity,total_units,total_good_attempts):
    print("------Inventory Report------")
    print("Total transaction processed:", total_good_attempts)
    print("Total unit processed:", total_units)
    print("Failed entries:", int(failed_id) + int(failed_quantity))

#ask if can use Json , yes i can
def persistence(): 
    try:
        f = open("inventory.json", "r") #variable f will be assigned the file opened with flag -r
        inventory=  json.load(f) #convert json file into python, load the python value as "inventory"
        return inventory 

    except (FileNotFoundError):
        inventory = [[1000, "nil", 0]] #create a variable called inventory

        f = open("inventory.json", "w") #create inventory.json file , -w is important
        json.dump(inventory, f) #convert the python value of Inventory into Json 
        f.close()

        return inventory
        
def load_inventory(inventory):
    print("\n------ Current Inventory ------")

    for product in sorted(inventory, key=lambda product: product[0]):
        print("ID:", product[0],
              "| Description:", product[1],
              "| Quantity:", product[2])


inventory = persistence() #pulls out the whole Json inventory file to compare
failed_attempts = 0
total_tax = 0
total_good_attempts = 0
failed_id = 0
failed_quantity = 0
total_units = 0

while True:
    current_product = []
    product_description = " "
    quantity_value = 0
    # if quantity_value!= 0:
    #     print("taxable amount:$", calculate_tax(quantity_value))

    load_inventory(inventory)

    return_get_valid_id = get_valid_id() #saved output of function to a list (no need call function eveyrthing you need variable)
    if return_get_valid_id[0] == "quit": #user can only quit while editing ID
            # failed_id = return_get_valid_id[1] #add failed attempt from failed_id 
            # failed_quantity = return_quantity_value[1]
            generate_report(failed_id,failed_quantity,total_units,total_good_attempts)
            break 

    else: #initate inventory process 
        current_product = return_get_valid_id[0]
        current_id = current_product[0]
        product_description = get_valid_description (current_product[1])
        return_quantity_value = get_valid_quantity(current_product[2]) #assigning function return to variable 
        quantity_value = return_quantity_value[0] #ignoring failed variable again
       
        total_units += quantity_value # adding this for report
        delivery_information = process_delivery(current_id,product_description,quantity_value) #not editing ID, only send these twol_good_attempts += delivery_information #saving delivery information to a variable (in case we need to scale)
        total_good_attempts += int(delivery_information) #currently an integer as only one variable, no neeed to [x]

    

  

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
    

    
