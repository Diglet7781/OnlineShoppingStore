import json
class Cart:
    def __init__(self):
        Cart = []
        self.Cart = Cart

    def addToCart(current_Cart, item, quantity, price):

        cart = current_Cart.get_cart()
        cart.append([item, quantity, float(quantity)*float(price)])
        


    def get_cart(self):
        cart = self.Cart
        return cart


    def showCart(Curr_cart):
        total_price = 0
        cart = Curr_cart.get_cart()
        for item in range(len(cart)):
            print ("Item: ", cart[item][0])
            print ("Quantity: ", cart[item][1])
            total_price += cart[item][2]
            print ("\n")
        print ("Total Price: ", total_price)

    def removeQuantity(Curr_cart, remove_item, remove_quantity):

        cart = Curr_cart.get_cart()

        for item in range(len(cart)):

            if cart[item][0].lower() == remove_item.lower().strip():

                if cart[item][1] > remove_quantity:
                    cart[item][1] = str(int(cart[item][1]) - int(remove_quantity))
                    print ("Cart Updated")
                    break

                if cart[item][1] == remove_quantity:
                    del cart[item]
                    print ("Cart Updated")
                    break
