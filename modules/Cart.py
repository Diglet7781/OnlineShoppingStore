import json
class Cart:
    def __init__(self):
        Cart = []
        self.Cart = Cart

    def addToCart(current_Cart, item, quantity, price):

        current_Cart.append([item, quantity, price])
        print ("\nSuccessfully Added to Cart!\n")


    def get_cart(self):
        cart = self.Cart
        return cart

    def ShowCart(curr_cart):
        print ("\nYour Current Cart: \n")
        Total_P = 0
        for item in range(len(curr_cart)):
            print ("Item: ",curr_cart[item][0], "Quantity: ", curr_cart[item][1])
            Total_P += int(curr_cart[item][1])*float(curr_cart[item][2])
        print ("Total Price: ", Total_P)
        print ("\n")
