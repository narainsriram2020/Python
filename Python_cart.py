# Python Shopping Cart
#
# Description: Represent a grocery store shopping cart
#
# Author: Narain Sriram

# This is my main class
class Python_cart:
    # Groceries and funds are my two main attributes
    def __init__(self, groceries, funds):
        self.groceries = groceries
        self.funds = funds

    def total_cost(self):
        # The total cost method tallies up the total amount of the items in the grocery list
        total_cost = 0
        for grocerie in self.groceries:
            total_cost += grocerie.price
        return total_cost

    def can_afford(self):
        # The can afford method uses the total_cost method to see whether all the items in the list are affordable or not
        self.funds == can_afford
        if can_afford > total_cost or can_afford == total_cost:
            can_afford == True
        else:
            can_afford == False

    def add_grocery(self, grocery):
        # If a grocery needs to be added then this method will hepl do that
        self.groceries.append(grocery)


    def purchase(self, grocery):
        # The purchase method is used to signify that the user bought something and relies on the 
        if can_afford > total_cost or can_afford == total_cost:
            purchase == True
        else:
            purchase == False


    def __repr__(self):
        # This is the repr method that displays the code
        result = ""
        result = "GROCERY LIST: \n\n"
        for grocerie in self.groceries:
            result += str(grocerie)
        result += "\n\nAvailable Funds: $" + str(self.funds)
        # If statements to determine the affordibility based on the can_afford method
        if Python_cart.can_afford == True:
            result += "\nAffordable: YES"
        else:
            result += "\nAffordable: NO\n"
        # If statement to check whether the purchase can go thrugh with the remaining funds
        if Python_cart.purchase == True:
            for grocerie in groceries:
                groceries.pop(grocerie)
        if Python_cart.purchase == False:
            print("Insufucient Funds")
        return result
        
        
        
        
        #result += "\nAffordable?: " + "True"
        #return result
    