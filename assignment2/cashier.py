class Cashier:
    def __init__(self):
        pass

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
