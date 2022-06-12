# Python Grocery Item
#
# Class that represents a grocery item
#
# Author: Narain Sriram

# This is my class variable that the whole program depends upon
class Python_grocerry_item:
    item = "None"
    DEFAULT_NAME = item
    MIN_CALORIES = 0
    MIN_PRICE = 0.01 

# The code below is my init method where I define all of my parameters
    def __init__(self, name = "Item", vegan = False, vegetarian = False, calories = MIN_CALORIES, price = MIN_PRICE):
        # After listing the parameters I create my if statements
        self.name = name

        # This is the code for checking the limits of the calories
        if calories < Python_grocerry_item.MIN_CALORIES:
            print("Error: intended grade out of bounds;")
            self.calories = 0
        else:
            self.calories = calories
        
        #This is the code for checking the limits of the price
        if price < Python_grocerry_item.MIN_PRICE:
            print("Error: intended grade out of bounds;")
            self.price = 0.01
        else:
            self.price = price

        # This is the code for checking the limits of the vegan and vegetarian parameter
        if vegan == True:
            vegetarian == True
        
        self.vegan = vegan
        self.vegetarian = vegetarian
    
# This repr method helps print the actual statements in the code
    def __repr__(self):
        result = self.name + "\nSpecial Diets: "
        if self.vegan:
            result += "Vegan"
        if self.vegetarian:
            result += "Vegetarian"
        if not self.vegetarian and not self.vegan:
            result += "None"
        
        result += "\nCalories: " + str(self.calories) + "\nPrice: $" + str(self.price)

        return result
    
    # The eq method is the method for all equal items with one being self and the other being other
    def __eq__ (self, other):
        if self.calories == other.calories and self.price == other.price:
            return True
        else:
            return False
    
    # The following code is for the coupon parameter where the computation is already completed. In the runner file, a whole number needs to be but in a parenthesis for the coupon to be completed
    def coupon(self, discount_pct):
        self.price = self.price * ((100 - discount_pct) / 100)
