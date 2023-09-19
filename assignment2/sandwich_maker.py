
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for k in ingredients:
            # Iterate all ingredients
            if self.machine_resources[k] < ingredients[k]:
                # If any resource is less than the required amount, return False
                print(f"Sorry, there is not enough {k}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for k in order_ingredients:
            # Iterate order ingredients and deduct resources
            self.machine_resources[k] -= order_ingredients[k]