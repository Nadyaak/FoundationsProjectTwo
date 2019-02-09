# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.Nadya.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores :
        print("- %s" %(store.name))

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name == store_name  :
            return store
    return False    

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    my_store = input("Pick a store by typing its name. Or \"checkout\" to pay your bills and say your goodbyes\n")
    while my_store.lower() != "checkout":
        if get_store(my_store.capitalize()):
            return get_store(my_store.capitalize())
        else :
            my_store = input("We don't have this store try agine\n")
    return "checkout"      

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print ("-------------------------------------------")
    print(picked_store.name.capitalize()+":")
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above. Type \"back\" to go back to the main menu where you can checkout.")
    pchoooes = input("")
    while pchoooes.lower() !="back":
        for product in picked_store.products:
            if pchoooes.lower() == product.name.lower() :
                cart.add_to_cart(product)
                print("Successfully added")  
        pchoooes = input()     

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    while True:
        store = pick_store()
        if store == "checkout" :
            break
        elif store != False:
            pick_products(cart,store)
    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
