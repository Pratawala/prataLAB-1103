#first commit kinda nervous!

def add_inventory():
    inventory = 0
    input_value = "0" 
    ""
    Fe = 0 #failed entry 
    while str(input_value) != "quit":
        try:
            input_value = input(  "Current inventory: " + str(inventory) + "\n" + "how much inventory do you want?:")

            if  str(input_value) == "quit":
                        print("total unit processed:", inventory)
                        print("failed entries:", Fe)
                        break 

            else:
                input_value = int(input_value)

            
            if input_value + inventory >= 500:
                print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
                break
                
            elif input_value < 0:
                print("------Inventory cannot be negative------")
                Fe += 1

            else:
                inventory += input_value


        except(ValueError, TypeError): 
                print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
                Fe += 1




add_inventory()
