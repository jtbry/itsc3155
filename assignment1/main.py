### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for k in ingredients:
            # Iterate all ingredients
            if self.machine_resources[k] < ingredients[k]:
                # If any resource is less than the required amount, return False
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickles = int(input("how many nickles?: "))

        # Calculate dollar amount from coins
        return dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickles * 0.05

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            # calculate potential change by rounding the difference to 2 decimal places
            change = coins - cost
            if change > 0:
                # if there is change, print it
                print(f"Here is ${change} in change.")
            return True
        return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for k in order_ingredients:
            # Iterate order ingredients and deduct resources
            self.machine_resources[k] -= order_ingredients[k]


### Make an instance of SandwichMachine class and write the rest of the codes ###
choice = ""
sandwich_sizes = ["small", "medium", "large"]
sandwich_maker = SandwichMachine(resources)
while choice != "off":
    choice = input("What would you like? (small/medium/large/off/report): ")
    if choice in sandwich_sizes:
        # If it is a valid sandwich size select the recipe
        recipe = recipes[choice]
        if sandwich_maker.check_resources(recipe["ingredients"]):
            # If we have enough resources process coins
            coins = sandwich_maker.process_coins()
            if sandwich_maker.transaction_result(coins, recipe["cost"]):
                # If we are given enough money make the sandwich
                sandwich_maker.make_sandwich(choice, recipe["ingredients"])
                print(f"{choice} sandwich is ready. Bon appetit!")
            else:
                # If we are not given enough money, do nothing
                print("Sorry that's not enough money. Money refunded.")
        else:
            # If there is not enough resources, do nothing
            print(f"Not enough ingredients to make a {choice} sandwich.")
    elif choice == "off":
        # If the user wants to turn off the machine, break the loop
        break
    elif choice == "report":
        # If the user wants to see the report, print the resources
        for k in sandwich_maker.machine_resources:
            print(f"{k}: {resources[k]}")
    else:
        # If the user enters something else, do nothing
        print("Sorry, I don't understand that.")
