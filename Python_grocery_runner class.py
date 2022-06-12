# Python_grocery_runner class
#
# Runner file for the Python Grocery project
#
# Author: Narain Sriram

import Python_grocerry_item

# The first test where all the parameters are changed
eggs = Python_grocerry_item.Python_grocerry_item("eggs", False, False, 75, 2.95)
print(eggs)

print("")

# The second test where the item is made vegan but not vegetarian
cheese = Python_grocerry_item.Python_grocerry_item("cheese", True, False, 150, 3.85)
print(cheese)

print("")

# The third test where it is all default except the name
default = Python_grocerry_item.Python_grocerry_item("milk")
print(default)

print("")

# The fourth test where a 20% coupon is applied on the cheese product
cheese.coupon(20)
print(cheese)