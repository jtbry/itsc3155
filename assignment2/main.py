import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    ###  write the rest of the codes ###
    choice = ""
    sandwich_sizes = ["small", "medium", "large"]
    while choice != "off":
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice in sandwich_sizes:
            # If it is a valid sandwich size select the recipe
            recipe = recipes[choice]
            if sandwich_maker_instance.check_resources(recipe["ingredients"]):
                # If we have enough resources process coins
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipe["cost"]):
                    # If we are given enough money make the sandwich
                    sandwich_maker_instance.make_sandwich(choice, recipe["ingredients"])
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
            for k in sandwich_maker_instance.machine_resources:
                print(f"{k}: {resources[k]}")
        else:
            # If the user enters something else, do nothing
            print("Sorry, I don't understand that.")
    

if __name__=="__main__":
    main()
