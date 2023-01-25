"""
Helen Hammond,January 24, 2023, Module 2-Functions and Statistics

"""

import math

# define some functions

def get_area_of_lot(length, width):
    # """
    # Return area of a lot given the length and width of the lot.

    # Could this fail?

    # """
   #Area 
    return math.floor(length * width)





def get_taxed_price(price, tax_rate):
#     """
# food price after applying tax rate
#     """
    return price * (1 + tax_rate)

def get_amount(tax, quantity):
    # """
    # Total dog food order
    # """
    return math.fsum([tax * quantity]) 


def get_donations(donation):
    """
    sum of donation
    """
    return math.fsum(donation)

    # Call functions
print("Area : ", get_area_of_lot(98, 9))
print("Price of dog food with tax: ", get_taxed_price(90, 0.95))
print("Order amount: ", get_amount(19, 9))
print("Sum of donations: ", get_donations([9.50, 1.20,98.9]))