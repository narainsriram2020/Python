# Python Shopping Cart
#
# Description: Shopping Cart Runner File
#
# Author: Narain Sriram

import Python_grocery_item
import Python_cart

# The following are my three grocery items
eggs = Python_grocery_item.Python_grocery_item("eggs", False, False, 75, 2.95)

cheese = Python_grocery_item.Python_grocery_item("\n\ncheese", True, False, 150, 3.85)

milk = Python_grocery_item.Python_grocery_item("\n\nmilk", True, False, 120, 2.34)

# This is my main statement where I notify the parameters in what I am trying to print
python_shopping_cart = Python_cart.Python_cart([eggs, cheese, milk], 1)

print(python_shopping_cart)
#python_shopping_cart.purchase(milk)
print(python_shopping_cart)
eggs.coupon(20)
print(python_shopping_cart)