# Component interface (Base food item)
class FoodItem:
    def get_description(self):
        pass

    def get_cost(self):
        pass


# Concrete Component (Basic Food Item)
class BasicFoodItem(FoodItem):
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


# Decorator abstract class
class FoodDecorator(FoodItem):
    def __init__(self, food_item):
        self._food_item = food_item

    def get_description(self):
        return self._food_item.get_description()

    def get_cost(self):
        return self._food_item.get_cost()


# Concrete Decorator (Extra Topping)
class ExtraTopping(FoodDecorator):
    def __init__(self, food_item, topping_description, topping_cost):
        super().__init__(food_item)
        self._topping_description = topping_description
        self._topping_cost = topping_cost

    def get_description(self):
        return f"{self._food_item.get_description()}, {self._topping_description}"

    def get_cost(self):
        return self._food_item.get_cost() + self._topping_cost


# Concrete Decorator (Discount)
class Discount(FoodDecorator):
    def __init__(self, food_item, discount_percentage):
        super().__init__(food_item)
        self._discount_percentage = discount_percentage

    def get_cost(self):
        discounted_cost = self._food_item.get_cost() * (1 - self._discount_percentage / 100)
        return round(discounted_cost, 2)


def create_food_item(description, cost):
    # Create a basic food item with the given description and cost
    return BasicFoodItem(description, cost)


if __name__ == "__main__":
    # Create a dictionary of food items and their prices
    menu = {
        "burger": 5.99,
        "pizza": 8.99,
        "salad": 3.49,
        "cheese": 1.50,
    }

    # Get user input for food item name
    food_item_name = input("Enter the food item name: ").lower()

    # Check if the entered food item is in the menu
    if food_item_name in menu:
        # Create a basic food item with the selected description and cost
        food_item = create_food_item(food_item_name, menu[food_item_name])

        # Add extra toppings and discounts using decorators (if desired)
        while True:
            extra = input("Add extra topping or discount (enter 'done' to finish): ").lower()
            if extra == "done":
                break
            elif extra in menu:
                food_item = ExtraTopping(food_item, extra, menu[extra])
            else:
                print("Extra not found in the menu. Please enter a valid extra.")

        # Calculate and display the final cost and description
        print(f"Item: {food_item.get_description()}")
        print(f"Cost: ${food_item.get_cost():.2f}")
    else:
        print("Food item not found in the menu.")
