

# first commit kinda nervous!

def get_valid_input(inventory):
    while True:
        input_value = input(
            "Current inventory: " + str(inventory) +
            "\nHow much inventory do you want?: "
        )

        if input_value == "quit":
            return "quit"

        try:
            input_value = int(input_value)

            if input_value <= 0:
                print("------Inventory cannot be less than zero------")
                return False

            elif input_value + inventory > 500:
                print("------!!!!Inventory cannot exceed 500, OVERSTOCK ALERT!!!------")
                return False

            return input_value

        except (ValueError, TypeError):
            print("------Invalid input, please enter a digit greater than 0 or type 'quit' to exit------")
            return False


def process_delivery(current_total, new_value):
    new_total = current_total + new_value


    return new_total


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("------Inventory Report------")
    print("Total unit processed:", total_units)
    print("Failed entries:", failed_attempts)


inventory = 0
failed_attempts = 0
total_tax = 0
input_value=0

while True:
    if input_value!= 0:
        print("taxable amount:$", calculate_tax(input_value))

    input_value = get_valid_input(inventory)


    if input_value == "quit":
        generate_report(inventory, failed_attempts)
        break

    if input_value is False:
        failed_attempts += 1
        continue

    new_inventory = process_delivery(inventory, input_value)


    inventory = new_inventory
    total_tax += calculate_tax(input_value)