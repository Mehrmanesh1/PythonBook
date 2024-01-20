
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")
    def open(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self,n):
        self.number_served = n
        print(f"You served {n} customers")

if __name__ == "__main__":
    kabab_restaurant = Restaurant("Kabab Shop", "Persian")
    kabab_restaurant.open()
    kabab_restaurant.describe_restaurant()

    honey_bakery = Restaurant("Honey Bakery", "American")
    honey_bakery.open()
    honey_bakery.describe_restaurant()

    Bills_Breakfast = Restaurant("Bill's Breakfast", "American")
    Bills_Breakfast.open()
    Bills_Breakfast.describe_restaurant()

    sam_burger = Restaurant("Samburger", "American")
    sam_burger.open()
    sam_burger.describe_restaurant()